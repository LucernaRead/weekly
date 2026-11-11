# -*- coding: utf-8 -*-
"""Export a Lucerna Weekly core edition's readable text to Markdown.

Rebuilt 2026-11-10 for 2026-W47. The W46 original DOES exist
(`production/2026-w46/ru_textmd.py`, 230 lines) but it is an EARLIER
revision: it emits raw U+3000 in titles (no " · " + CJK-digit spacing),
includes the P1 deck as a ### line, and lacks the ✓ form for the writing
key — 58 diff hunks vs the shipped W46 file. This rebuild targets the
SHIPPED format (verified: regenerating the W46 file from the W46 core
sources yields 150 exercises / 200 blocks and differs from the shipped
file in exactly two places — see WEEKLY-KIT.md §5).

Usage:
    ru_textmd.py <build-dir> <out.md> "<title>" ["<writing_type>"]

    build-dir  core dir holding content12/34/56/7/8.py + bslib4.py
    out.md     Markdown file to write
    title      first line, e.g. "VOL.4 · Russian text · Simplified Chinese explanations"
    writing_type  accepted for CLI compatibility with the W46 regen
                  wrapper; unused (the H exercise type comes from the source).

How it works
-------------
1. AST-walks the five content files in reading order (the files are flat
   scripts; statements execute in source order, so the walk order is the
   reading order). Reading text is emitted wherever it is printed,
   including p.para/p.paraq: plain-string variables, literals and
   list-loop items (plain `for ... in <list>` and `enumerate(<list>)`)
   are all resolved through env. Only the `quotes` list is excepted from
   loop binding — it has its own export branch below, and the p.para
   loop over it prints the same quotes a second time.
2. Re-runs the five files in-process (save() patched to a no-op, bytecode
   writing disabled, so nothing on disk is touched) to populate the
   exercise registry REG in bslib4; the P8 answers appendix is built from
   REG, which is the single source of truth for numbering/keys/notes.

Emission rules (all verified against the shipped W46 .text.md)
--------------------------------------------------------------
* "# {title}", then "## Page N" at each CURPAGE[0] = N.
* Titles (### / ##): full-width space U+3000 becomes " · "; CJK<->digit
  boundaries get a space ("第8版" -> "第 8 版", "11月11日" -> "11 月 11 日").
  Body text (paragraphs, glosses, exercises, box items) is verbatim.
* p.band(left, right, sub) -> "### {left} — {sub}" (right is always the
  masthead word "Lucerna" and is dropped; if right were anything else it
  would be kept as "{left} — {right} · {sub}").
* p.text sans+bold size >= 24 -> "### {s}", EXCEPT light-on-cloth text
  (fill ONCLOTH) below 40pt, which is furniture (the P7 teaser) and is
  skipped. The P1 deck (serif, non-bold, 24-28pt, fill GREY) also becomes
  "### {s}". Everything else p.text is furniture and is skipped.
* f.para / p.para / p.paraq -> paragraph; f.gloss -> "> {s}";
  f.bridge -> "*{s}*"; f.head / e.head -> "## {s}"; e.bridge -> "*{s}*".
  Flow methods are dispatched by method name, not by receiver variable:
  the P7 column flows (a/b/c), the P1 snow box (f2) and the P1 quiz (qf)
  all count, and so does the Page (p) — its para prints real reading
  text on this issue (side-box facts, clinic rows, the reader letter,
  the week calendar, the P1 contents list, the word glosses), so the
  old "p is layout" exclusion is removed; only p.text keeps its
  size/fill furniture filter. A call wrapped in an assignment
  (cy2 = caption(...)) is dispatched too. A p.para paragraph still
  passes a prose filter (blank lines and the "— СТРАНИЦА" page-footer
  separator are not reading text).
* f.box(title, paras) -> "### {title}" + each para tuple's text as a
  plain line.
* caption(p, x, y, w, fr, credit) -> "*{fr}*" (credit is not exported).
* f.ex / e.ex -> "{n}. [{level} · {type}] {body} — key: {key} ({note})"
  + " [{instr}]" when instr is given (no note parens when note is empty).
* e.match_set(level, typ, lefts, rights, keys, notes, instr) ->
  "{n1}–{n2}. [{level} · {typ}] {instr}" + one line per item
  "{n}. {left} — {rights[key-index]} (key {letter} · {note})".
* chart = [(label, val), ...] -> "### Chart (practice data)" +
  "- {label}: {val}%" lines.
* quotes = [(ru, zh, "Страница N"), ...] -> "> «{ru}» — {zh} ({pg})".
  (In W47 the tuples carry the page as "Страница N" strings already.)
* The answers loop (`for pg in sorted(by_page):`) is replaced by the
  appendix built from REG: "— СТРАНИЦА ? —", "## Answers", then one
  block per page: "### Page {pg}" + "{n}. {key} — {note}" lines
  (writing exercise: "{n}. ✓ {note}").
* Blocks are joined by one blank line; the file ends with one "\n".
  Consecutive exercises (and matching blocks) share one block — no
  blank lines between them; a stand-alone emission flushes the run.
  A paragraph right after an exercise run joins that run (the H model
  text after ex 150). A box title is one block and EACH box item is
  its own block.

Known deliberate deviations from the W46 file
----------------------------------------------
* The W46 file places the P6 chart under "## Page 4". No page-tracking
  rule derivable from the sources puts it there; this exporter places
  it under its real page (Page 6).
* W47 sources follow SOP §1.1 (Chinese numerals take no spaces), so W47
  exercise notes/keys export unspaced ("11月17日"), where the W46 file
  has spaced notes because the W46 sources were spaced. Band/head
  titles still get CJK-digit spacing, exactly as in the W46 file.
* The W46 file omits the P4 first paragraph ("14-й тур чемпионата
  России сыграли 6–8 ноября. Но честно: ...") although it is an
  ordinary f.para in the W46 source, while the P2/P3/P5/P6 first
  paragraphs are all present — most plausibly the file was generated
  before that paragraph was added to the source. This exporter
  includes every article paragraph.
* The W47 P8 morozko caption is exported (it sits in an `if` block
  that this exporter walks into); the W46 sources have no such caption.
"""

import ast
import io
import os
import re
import runpy
import sys
from contextlib import redirect_stdout

FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

CJK = r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]"
RE_CJK_DIGIT = re.compile(r"(" + CJK + r")(\d)")
RE_DIGIT_CJK = re.compile(r"(\d)(" + CJK + r")")


def space_cjk_digits(s):
    """Insert a space at CJK<->digit boundaries (band/head titles only)."""
    return RE_DIGIT_CJK.sub(r"\1 \2", RE_CJK_DIGIT.sub(r"\1 \2", s))


def titleize(s):
    """Title transform: U+3000 -> ' · ' + CJK-digit spacing."""
    return space_cjk_digits(s.replace("\u3000", " · "))


# ---------------- constant-expression evaluator ----------------

class EvalError(Exception):
    pass


def ev(node, env):
    """Evaluate a small constant expression (str/int/bool/list/tuple)."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in env:
            return env[node.id]
        raise EvalError("unbound name %s" % node.id)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return ev(node.left, env) + ev(node.right, env)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -ev(node.operand, env)
    if isinstance(node, ast.JoinedStr):
        out = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                out.append(str(v.value))
            elif isinstance(v, ast.FormattedValue):
                val = ev(v.value, env)
                out.append(str(val))
            else:
                raise EvalError("bad JoinedStr part")
        return "".join(out)
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name) and f.id == "len" and len(node.args) == 1:
            arg = node.args[0]
            if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Attribute) \
                    and arg.func.attr == "split" and not arg.args:
                return len(ev(arg.func.value, env).split())
        raise EvalError("unsupported call")
    if isinstance(node, (ast.List, ast.Tuple)):
        vals = [ev(e, env) for e in node.elts]
        return vals if isinstance(node, ast.List) else tuple(vals)
    raise EvalError("unsupported node %s" % type(node).__name__)


def ev_str(node, env):
    v = ev(node, env)
    if not isinstance(v, str):
        raise EvalError("not a string")
    return v


def ev_num(node, env):
    v = ev(node, env)
    if not isinstance(v, (int, float)) or isinstance(v, bool):
        raise EvalError("not a number")
    return v


# ---------------- exporter ----------------

class Exporter:
    def __init__(self, build_dir):
        self.build_dir = build_dir
        self.blocks = []
        self.cur = None         # lines of the block being accumulated
        self.cur_is_run = False  # True when cur is an exercise run
        self.n = 0            # exercise counter
        self.curpage = 0
        self.env = {}         # per-file constant bindings
        self.reg = None

    def add(self, block):
        """Emit one stand-alone block (may be multi-line)."""
        self._flush()
        if block:
            self.blocks.append(block.split("\n"))

    def _flush(self):
        if self.cur:
            self.blocks.append(self.cur)
            self.cur = None
            self.cur_is_run = False

    def add_run(self, lines):
        """Append exercise lines to the current exercise run.

        Consecutive exercises (and matching blocks) share one block:
        no blank lines between them. Any stand-alone emission flushes
        the run.
        """
        if not self.cur_is_run:
            self._flush()
            self.cur = []
            self.cur_is_run = True
        self.cur.extend(lines)

    def add_para(self, text):
        """Emit a paragraph. It joins an open exercise run (the one
        place this happens is the H model text after ex 150); otherwise
        it is its own block."""
        if self.cur_is_run:
            self.cur.append(text)
        else:
            self.add(text)

    def finish(self):
        self._flush()
        return "\n\n".join("\n".join(b) for b in self.blocks) + "\n"

    # ---- exercises ----
    def ex_line(self, level, typ, key, note, body, instr):
        self.n += 1
        line = "%d. [%s · %s] %s — key: %s" % (self.n, level, typ, body, key)
        if note:
            line += " (%s)" % note
        if instr:
            line += " [%s]" % instr
        return line

    def do_ex(self, call, env):
        a = call.args
        kw = {k.arg: k.value for k in call.keywords}
        level = ev_str(a[0], env)
        typ = ev_str(a[1], env)
        key = ev_str(a[2], env)
        note = ev_str(a[3], env) if len(a) > 3 else ""
        body = ev_str(a[4], env)
        instr = ev_str(kw["instr"], env) if "instr" in kw else None
        self.add_run([self.ex_line(level, typ, key, note, body, instr)])

    def do_match_set(self, call, env):
        a = call.args
        kw = {k.arg: k.value for k in call.keywords}
        level = ev_str(a[0], env)
        typ = ev_str(a[1], env)
        lefts = ev(a[2], env)
        rights = ev(a[3], env)
        keys = ev(a[4], env)
        notes = ev(a[5], env)
        instr = ev_str(kw["instr"], env) if "instr" in kw else ""
        n1 = self.n + 1
        lines = []
        for i, (left, k, note) in enumerate(zip(lefts, keys, notes)):
            self.n += 1
            idx = ord(k) - ord("a")
            lines.append("%d. %s — %s (key %s · %s)"
                         % (self.n, left, rights[idx], k, note))
        head = "%d–%d. [%s · %s] %s" % (n1, self.n, level, typ, instr)
        self.add_run([head] + lines)

    # ---- p.para / p.paraq ----
    @staticmethod
    def is_prose_para(s):
        """Prose filter for p.para paragraphs (D6 fix).

        Everything p.para prints on this issue is reading text, so the
        filter only removes what is definitionally not: blank strings
        and the page-footer separator ("— СТРАНИЦА ..." — the answers
        appendix emits its own separator line, and no p.para call on
        this issue prints one; the rule is belt-and-braces for later
        issues).
        """
        t = s.strip()
        if len(t) < 2:
            return False
        if t.startswith("— СТРАНИЦА"):
            return False
        return True

    def do_p_para(self, call, env):
        """p.para / p.paraq -> paragraph, same handling as f.para.

        NOTE the signature differs from f.para: p.para(x, y, s, ...) puts
        the text third (args[2]), like p.text — not first (args[0]).
        (An earlier draft used args[0] and emitted nothing: args[0] is
        the x coordinate, ev_str rejects the number. The dry run caught
        it.) paraq has no definition or call sites on this issue; it is
        given the same args[2] convention as p.para.
        """
        if len(call.args) < 3:
            return
        try:
            s = ev_str(call.args[2], env)
        except EvalError:
            return
        if not self.is_prose_para(s):
            return
        self.add_para(s)

    # ---- p.text ----
    def do_p_text(self, call, env):
        a = call.args
        kw = {k.arg: k.value for k in call.keywords}
        if len(a) < 6:
            return  # e.g. the masthead (family= kwarg): furniture, skipped
        try:
            s = ev_str(a[2], env)
            size = ev_num(a[3], env)
            font = ev_str(a[4], env)
            bold = ev(a[5], env)
            fill = None
            if len(a) > 6:
                if isinstance(a[6], ast.Name):
                    fill = ("name", a[6].id)
                else:
                    fill = ("const", ev(a[6], env))
        except EvalError:
            return
        if font == "sans" and bold is True and size >= 24:
            # light-on-cloth furniture below 40pt (P7 teaser) is skipped;
            # the 46pt band main is content.
            if fill == ("name", "ONCLOTH") and size < 40:
                return
            self.add("### " + titleize(s))
            return
        if font == "serif" and bold is False and 24 <= size <= 28 \
                and fill == ("name", "GREY"):
            # the P1 deck line
            self.add("### " + titleize(s))
            return

    def do_p_band(self, call, env):
        a = call.args
        try:
            left = ev_str(a[0], env)
            right = ev_str(a[1], env) if len(a) > 1 else ""
            sub = ev_str(a[2], env) if len(a) > 2 else ""
        except EvalError:
            return
        if right and right != "Lucerna":
            self.add("### %s — %s · %s"
                     % (titleize(left), titleize(right), titleize(sub)))
        else:
            self.add("### %s — %s" % (titleize(left), titleize(sub)))

    # ---- calls ----
    def do_call(self, call, env):
        f = call.func
        if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name):
            recv, attr = f.value.id, f.attr
            if recv == "p" and attr == "text":
                self.do_p_text(call, env)
            elif recv == "p" and attr == "band":
                self.do_p_band(call, env)
            elif recv == "p" and attr in ("para", "paraq"):
                # D6 fix (2026-11-11): the Page's para prints real reading
                # text on this issue — side-box facts, clinic rows, the
                # reader letter, the week calendar, the P1 contents list,
                # the word glosses — so it is exported like f.para. The
                # old "p is layout" claim was disproved by census (see
                # FIX-LOG): every p.para string on this issue is prose.
                # paraq has no call sites yet; covered the same way.
                self.do_p_para(call, env)
            elif recv != "p" and attr in (
                    "para", "gloss", "bridge", "head", "box", "ex",
                    "match_set", "end_report"):
                # Any Flow/ExBlock object (f, e, af, f2, qf, a, b, c, ...):
                # the receiver name varies (per-column flows on P7, the
                # P1 snow box f2, the P1 quiz qf).
                if attr == "para":
                    if call.args:
                        try:
                            self.add_para(ev_str(call.args[0], env))
                        except EvalError:
                            pass
                elif attr == "gloss":
                    try:
                        self.add("> " + ev_str(call.args[0], env))
                    except EvalError:
                        pass
                elif attr == "bridge":
                    try:
                        self.add("*%s*" % ev_str(call.args[0], env))
                    except EvalError:
                        pass
                elif attr == "head":
                    try:
                        self.add("## " + titleize(ev_str(call.args[0], env)))
                    except EvalError:
                        pass
                elif attr == "box":
                    try:
                        title = ev_str(call.args[0], env)
                    except EvalError:
                        return
                    # Paras are (text, font, bold, fill, size, lh) tuples;
                    # fill/size are module constants (INK, ...) so the
                    # list is NOT evaluable as a whole — take each
                    # tuple's first element straight from the AST.
                    # The title is one block; EACH item is its own block
                    # (blank-separated in the shipped file).
                    self.add("### " + titleize(title))
                    try:
                        items = call.args[1].elts
                    except (AttributeError, IndexError):
                        items = []
                    for it in items:
                        try:
                            elts = it.elts
                            self.add(ev_str(elts[0], env))
                        except (AttributeError, EvalError, IndexError):
                            continue
                elif attr == "ex":
                    self.do_ex(call, env)
                elif attr == "match_set":
                    self.do_match_set(call, env)
                # end_report and the rest: nothing
        elif isinstance(f, ast.Name) and f.id == "caption":
            # caption(p, x, y, w, fr, credit="")
            try:
                self.add("*%s*" % ev_str(call.args[4], env))
            except (EvalError, IndexError):
                pass
        # every other call: layout or bookkeeping, skipped

    # ---- statements ----
    def do_assign(self, node, env):
        # A call wrapped in an assignment (cy2 = caption(...), or
        # yy3 = p.para(...) + 12) is still an emitted call — dispatch
        # every call nested in the assigned value. do_call ignores
        # anything it does not recognise (wrap/sum/len/...), so the
        # layout arithmetic around the call is harmless. (An earlier
        # draft only dispatched a bare Call value, which silently
        # dropped every `p.para(...) + N` site — 43 of the 74 p.para
        # lines on this issue, including the whole clinic column.)
        for sub in ast.walk(node.value):
            if isinstance(sub, ast.Call):
                self.do_call(sub, env)
        # CURPAGE[0] = N  -> new page header
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Subscript):
            sub = node.targets[0]
            if isinstance(sub.value, ast.Name) and sub.value.id == "CURPAGE":
                try:
                    pg = ev(node.value, env)
                except EvalError:
                    return
                if pg != self.curpage:
                    self.curpage = pg
                    self.add("## Page %d" % pg)
                return
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name == "chart":
                try:
                    items = ev(node.value, env)
                except EvalError:
                    return
                lines = ["### Chart (practice data)"]
                lines += ["- %s: %s%%" % (lab, val) for lab, val in items]
                self.add("\n".join(lines))
                return
            if name == "quotes":
                try:
                    items = ev(node.value, env)
                except EvalError:
                    return
                # One block: the quote lines are consecutive, no blanks.
                lines = []
                for q, cn, pg in items:
                    # The tuple already carries its own « » — do not add more.
                    lines.append("> %s — %s (%s)" % (q, cn, pg))
                self.add("\n".join(lines))
                return
            # record constant bindings for the evaluator
            try:
                env[name] = ev(node.value, env)
            except EvalError:
                pass

    # ---- for-loop binding (D6 fix) ----
    def loop_items(self, node, env):
        """Items a for-loop iterates over, or None if not a plain list loop.

        Only two shapes are executed per item: `for ... in <name>` where
        the name holds a list/tuple of constants, and `enumerate(<name>)`
        over the same (items come back as (index, value) pairs). Anything
        else (range, slices, sorted, REG-derived) returns None and the
        caller falls back to a single walk of the body, as before.
        The `quotes` list is never bound: it has its own export branch
        (do_assign) and the p.para loop over it prints the same quotes a
        second time — binding it would duplicate the quote block.
        """
        it = node.iter
        name = None
        enum = False
        if isinstance(it, ast.Name):
            name = it.id
        elif isinstance(it, ast.Call) and isinstance(it.func, ast.Name) \
                and it.func.id == "enumerate" and len(it.args) == 1 \
                and isinstance(it.args[0], ast.Name):
            name = it.args[0].id
            enum = True
        else:
            return None
        if name == "quotes":
            return None
        try:
            vals = ev(it, env) if not enum else ev(it.args[0], env)
        except EvalError:
            return None
        if not isinstance(vals, (list, tuple)):
            return None
        if enum:
            return [(i, v) for i, v in enumerate(vals)]
        return list(vals)

    @staticmethod
    def bind_target(target, value, env):
        """Bind one for-target (a Name, or a Tuple of targets, nested) to
        one loop item. Raises EvalError when shapes do not match."""
        if isinstance(target, ast.Name):
            env[target.id] = value
            return
        if isinstance(target, ast.Tuple) and isinstance(value, (list, tuple)) \
                and len(target.elts) == len(value):
            for t, v in zip(target.elts, value):
                Exporter.bind_target(t, v, env)
            return
        raise EvalError("cannot bind loop target")

    def walk_stmt(self, node, env):
        if isinstance(node, ast.Assign):
            self.do_assign(node, env)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            try:
                if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) \
                        and node.value is not None:
                    env[node.target.id] = ev(node.value, env)
            except EvalError:
                pass
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            self.do_call(node.value, env)
        elif isinstance(node, ast.For):
            # the answers loop -> appendix from REG (built separately)
            it = node.iter
            if isinstance(it, ast.Call) and isinstance(it.func, ast.Name) \
                    and it.func.id == "sorted" and len(it.args) == 1 \
                    and isinstance(it.args[0], ast.Name) \
                    and it.args[0].id == "by_page":
                self.do_appendix()
                return
            # D6 fix (2026-11-11): a loop over a constant list prints one
            # paragraph per item (facts boxes, clinic rows, day lists,
            # contents, word glosses). Walk the body once per item with
            # the target bound, so p.para loop variables resolve through
            # env exactly like plain-string variables. Any other iter
            # (range, slices, sorted, REG-derived) falls back to a single
            # walk of the body, as before. Loop-body bindings are
            # layout coordinates and do not leak out of the loop.
            items = self.loop_items(node, env)
            if items is None:
                for st in node.body:
                    self.walk_stmt(st, env)
            else:
                saved = dict(env)
                try:
                    for value in items:
                        env.clear()
                        env.update(saved)
                        try:
                            self.bind_target(node.target, value, env)
                        except EvalError:
                            continue
                        for st in node.body:
                            self.walk_stmt(st, env)
                finally:
                    env.clear()
                    env.update(saved)
            for st in node.orelse:
                self.walk_stmt(st, env)
        elif isinstance(node, ast.If):
            for st in node.body:
                self.walk_stmt(st, env)
            for st in node.orelse:
                self.walk_stmt(st, env)
        # imports, defs, returns, prints, while, etc.: skipped

    # ---- appendix from the live registry ----
    def do_appendix(self):
        reg = self.get_reg()
        self.add("— СТРАНИЦА ? —")
        self.add("## Answers")
        by_page = {}
        for e in reg:
            by_page.setdefault(e["page"], []).append(e)
        for pg in sorted(by_page):
            lines = ["### Page %d" % pg]
            for e in by_page[pg]:
                if e["type"] == "写作":
                    lines.append("%d. ✓ %s" % (e["n"], e["note"]))
                else:
                    lines.append("%d. %s — %s" % (e["n"], e["key"], e["note"]))
            self.add("\n".join(lines))

    def get_reg(self):
        if self.reg is not None:
            return self.reg
        # Re-run the five content files in-process so REG accumulates.
        # save() is patched to a no-op and bytecode writing is disabled,
        # so nothing on disk is touched.
        build_dir = os.path.abspath(self.build_dir)
        old_cwd = os.getcwd()
        old_dwb = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            import bslib4
            bslib4.REG.clear()
            bslib4.CURPAGE[0] = 0
            orig_save = bslib4.BSPage4.save
            bslib4.BSPage4.save = lambda self, *a, **k: None
            try:
                os.chdir(build_dir)
                buf = io.StringIO()
                with redirect_stdout(buf):
                    for fn in FILES:
                        runpy.run_path(os.path.join(build_dir, fn),
                                       run_name="__main__")
            finally:
                bslib4.BSPage4.save = orig_save
            self.reg = list(bslib4.REG)
        finally:
            sys.dont_write_bytecode = old_dwb
            os.chdir(old_cwd)
        return self.reg

    def seed_env(self, tree):
        """Copy module constants from the file's star-imports into env.

        Content files do `from bslib4 import *`; names like INK/OLIVE/GREY
        appear inside emitted structures (box paras). Without them the
        evaluator fails the whole call. Loading is best-effort and never
        writes bytecode.
        """
        env = {}
        for st in tree.body:
            if not (isinstance(st, ast.ImportFrom) and st.level == 0
                    and st.module):
                continue
            path = os.path.join(self.build_dir, st.module + ".py")
            if not os.path.isfile(path):
                continue
            try:
                import importlib.util
                old_dwb = sys.dont_write_bytecode
                sys.dont_write_bytecode = True
                try:
                    spec = importlib.util.spec_from_file_location(
                        "_textmd_seed_" + st.module, path)
                    mod = importlib.util.module_from_spec(spec)
                    old_path = sys.path[:]
                    sys.path.insert(0, os.path.abspath(self.build_dir))
                    try:
                        spec.loader.exec_module(mod)
                    finally:
                        sys.path[:] = old_path
                finally:
                    sys.dont_write_bytecode = old_dwb
                for k, v in vars(mod).items():
                    if k.startswith("_"):
                        continue
                    if isinstance(v, (str, int, float, bool, tuple, list)):
                        env.setdefault(k, v)
            except Exception:
                continue
        return env

    def run(self, title):
        self.add("# " + title)
        for fn in FILES:
            path = os.path.join(self.build_dir, fn)
            tree = ast.parse(open(path, encoding="utf-8").read(), filename=fn)
            env = self.seed_env(tree)
            for st in tree.body:
                self.walk_stmt(st, env)
        return self.finish()


def main(argv):
    if len(argv) < 4:
        print("usage: ru_textmd.py <build-dir> <out.md> \"<title>\" [writing_type]",
              file=sys.stderr)
        return 2
    build_dir, out, title = argv[1], argv[2], argv[3]
    exp = Exporter(build_dir)
    text = exp.run(title)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s (%d bytes, %d exercises, %d blocks)"
          % (out, len(text.encode("utf-8")), exp.n, len(exp.blocks)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
