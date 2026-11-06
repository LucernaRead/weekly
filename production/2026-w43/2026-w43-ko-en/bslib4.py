# -*- coding: utf-8 -*-
"""V4 broadsheet library: 1950x2700, 4 columns, exercise registry + flow layout."""
import sys, os, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import *

PW, PH = 1950, 2700
MX = 65                       # left/right margin
CW = 434                      # column width
GUT = 28
COLX = [MX + i * (CW + GUT) for i in range(4)]      # 65, 527, 989, 1451
RIGHT = MX + 4 * CW + 3 * GUT                       # 1885
CONTENT_BOTTOM = 2540         # nothing below this except footer
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

LV_COLOR = {"A2": "#3e4c2a", "B1": "#8a6d3b", "B2": "#a4553a"}

# ---------------- exercise registry (keys on P8 are generated from this) ----------------
REG = []
CURPAGE = [0]

def reg_ex(level, typ, key, note=""):
    REG.append({"n": len(REG) + 1, "page": CURPAGE[0], "level": level,
                "type": typ, "key": key, "note": note})
    return len(REG)

# ---------------- images ----------------
def img_uri(path):
    ext = "png" if path.lower().endswith(".png") else "jpeg"
    with open(path, "rb") as f:
        return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode()

def image(p, fname, x, y, w, h, par="xMidYMid slice"):
    path = os.path.join(ASSETS, fname)
    p.add(f'<image x="{x}" y="{y}" width="{w}" height="{h}" '
          f'preserveAspectRatio="{par}" href="{img_uri(path)}"/>')
    p.rect(x, y, w, h, fill="none", stroke=LINE, sw=1.4)
    return y + h

def caption(p, x, y, w, fr, credit=""):
    y = p.para(x, y + 24, fr, 19, "serif", False, GREY, w, 1.35)
    if credit:
        y = p.para(x, y + 2, credit, 15.5, "sans", False, "#8a8168", w, 1.3)
    return y

def chip(p, x, ytop, level):
    p.rect(x, ytop, 60, 30, fill=LV_COLOR[level], rx=6)
    p.text(x + 30, ytop + 22, level, 19, "sans", True, "#fdfaf0", anchor="middle")
    return 60

# ---------------- page ----------------
class BSPage4(Page):
    def __init__(self):
        self.w, self.h = PW, PH
        self.parts = []
        self.add(f'<rect width="{PW}" height="{PH}" fill="{PAPER}"/>')
        self.add(f'<rect x="28" y="28" width="{PW-56}" height="{PH-56}" fill="none" stroke="{INK}" stroke-width="3.4"/>')
        self.add(f'<rect x="40" y="40" width="{PW-80}" height="{PH-80}" fill="none" stroke="{INK}" stroke-width="1.2"/>')

    def band(self, title_left, title_right, sub=""):
        self.rect(52, 52, PW - 104, 98, fill=DARK)
        self.text(78, 116, title_left, 36, "sans", True, "#f3edda")
        self.text(PW - 78, 116, title_right, 36, "serif", True, "#f3edda", anchor="end")
        if sub:
            self.text(PW - 78, 142, sub, 19, "sans", False, "#b3a06a", anchor="end")
        return 178

    def foot(self, n, total=8):
        self.hline(MX, RIGHT, 2580, GOLD, 1.6)
        self.text(MX, 2624, "Lucerna · KOREAN WEEKLY VOL.1 · Korean text · English explanations", 20, "sans", False, GREY)
        self.text(RIGHT, 2624, f"Page {n} of {total}", 20, "sans", False, GREY, anchor="end")

    def shead(self, x, y, s, w, size=29, color=OLIVE):
        self.text(x, y, s, size, "sans", True, color)
        self.hline(x, x + w, y + 13, GOLD, 2)
        return y + 13

    def strip(self, y, h, text, fill=DARK, tcolor="#f3edda", size=27):
        self.rect(MX, y, RIGHT - MX, h, fill=fill)
        self.text((MX + RIGHT) / 2, y + h / 2 + size * 0.36, text, size, "sans", True, tcolor, anchor="middle")
        return y + h

def span_x(i, n=1):
    return COLX[i], n * CW + (n - 1) * GUT

# ---------------- column flow ----------------
class Flow:
    """Flows text blocks down a column, then to the next. Heights pre-measured via wrap()."""
    def __init__(self, page, cols, top, bottom=CONTENT_BOTTOM, tag=""):
        self.p = page
        self.cols = cols            # list of (x, w)
        self.top = top
        self.bottom = bottom
        self.ci = 0
        self.y = top
        self.tag = tag

    def set_region(self, cols, top, bottom=CONTENT_BOTTOM):
        self.cols, self.top, self.bottom = cols, top, bottom
        self.ci, self.y = 0, top

    @property
    def x(self):
        return self.cols[self.ci][0]

    @property
    def w(self):
        return self.cols[self.ci][1]

    def _fit(self, h):
        if self.y + h > self.bottom:
            if self.ci < len(self.cols) - 1:
                self.ci += 1
                self.y = self.top
            else:
                print(f"  !! FLOW OVERFLOW [{self.tag}] col {self.ci} y={self.y:.0f} need {h:.0f} bottom {self.bottom}")
                self.y = self.bottom  # clamp; visual QA will catch

    def _ph(self, s, size, kind, bold, w, lh):
        return len(wrap(s, kind, bold, size, w)) * size * lh

    def para(self, s, size=25, kind="serif", bold=False, fill=INK, lh=1.52, gap=10, split=True):
        if not split:
            h = self._ph(s, size, kind, bold, self.w, lh)
            self._fit(h + gap)
            self.y = self.p.para(self.x, self.y + size, s, size, kind, bold, fill, self.w, lh) + gap
            return self.y
        lines = wrap(s, kind, bold, size, self.w)
        while lines:
            maxk = int((self.bottom - self.y - size) // (size * lh)) + 1
            if maxk < 1 and self.ci < len(self.cols) - 1:
                self.ci += 1
                self.y = self.top
                continue
            k = min(maxk, len(lines)) if maxk >= 1 else len(lines)
            take, lines = lines[:k], lines[k:]
            base = self.y + size
            for i, ln in enumerate(take):
                self.p.text(self.x, base + i * size * lh, ln, size, kind, bold, fill)
            self.y = base + k * size * lh
            if lines:
                if self.ci < len(self.cols) - 1:
                    self.ci += 1
                    self.y = self.top
                else:
                    base = self.y + size
                    for i, ln in enumerate(lines):
                        self.p.text(self.x, base + i * size * lh, ln, size, kind, bold, fill)
                    self.y = base + len(lines) * size * lh
                    lines = []
        self.y += gap
        return self.y

    def glossline(self, s, size=20.5, gap=9, fill=GREY):
        return self.para(s, size, "sans", False, fill, 1.45, gap)

    def head(self, s, size=30, fill=OLIVE, gap=13):
        if text_w(s, "sans", True, size) > self.w:
            print(f"  !! HEAD TOO WIDE [{self.tag}]: {s[:40]}")
        h = size + 14 + gap
        self._fit(h + 30)
        self.y = self.p.shead(self.x, self.y + size, s, self.w, size, fill) + gap
        return self.y

    def title(self, s, size=38, gap=9, fill=INK):
        return self.para(s, size, "serif", True, fill, 1.22, gap, split=False)

    def byline(self, s, gap=10):
        return self.para(s, 19, "sans", False, GREY, 1.3, gap)

    def rule(self, gap=10):
        self._fit(4 + gap)
        self.p.hline(self.x, self.x + self.w, self.y + 2, LINE, 1.2)
        self.y += 4 + gap
        return self.y

    def box(self, title, paras, fill=BOX, bsize=22, tsize=23, pad=18, gap=12):
        """paras: list of (text, kind, bold, fill, size, lh). Height pre-measured."""
        iw = self.w - 2 * pad
        total = pad + (tsize + 10 if title else 0)
        for (t, k, b, f, s, lh) in paras:
            total += self._ph(t, s, k, b, iw, lh) + 5 + s
        total += pad - 5
        self._fit(total + gap)
        x, y0 = self.x, self.y
        self.p.rect(x, y0, self.w, total, fill=fill, stroke=LINE, sw=1.4)
        yy = y0 + pad
        if title:
            self.p.text(x + pad, yy + tsize - 4, title, tsize, "sans", True, OLIVE)
            yy += tsize + 10
        for (t, k, b, f, s, lh) in paras:
            yy = self.p.para(x + pad, yy + s, t, s, k, b, f, iw, lh) + 5
        self.y = y0 + total + gap
        return self.y

    def gloss(self, s, gap=12):
        return self.box("", [("Note — " + s, "sans", False, GREY, 20.5, 1.45)], fill="#f1ead6", gap=gap)

    def ex(self, level, typ, key, note, body, opts=None, instr=None, size=24, gap=11):
        n = reg_ex(level, typ, key, note)
        hh = 36
        bh = self._ph(body, size, "serif", False, self.w, 1.45)
        oh = 0
        if opts:
            for o in opts:
                oh += self._ph(o, size - 1, "serif", False, self.w - 34, 1.4) + 3
        self._fit(hh + bh + oh + gap)
        x, y = self.x, self.y
        chip(self.p, x, y, level)
        self.p.text(x + 72, y + 23, f"{n}.", 24, "sans", True, OLIVE)
        if instr:
            self.p.text(x + 142, y + 23, instr, 19.5, "sans", False, GREY)
        self.y = self.p.para(x, y + hh + size - 4, body, size, "serif", False, INK, self.w, 1.45)
        if opts:
            for o in opts:
                self.y = self.p.para(x + 34, self.y + size - 6, o, size - 1, "serif", False, INK, self.w - 34, 1.4) + 3
        self.y += gap
        return n

    def match_set(self, level, typ, lefts, rights, keys, notes, instr=None, gap=14):
        """lefts numbered (each registered), rights lettered a/b/c... printed once."""
        nums = [reg_ex(level, typ, k, nt) for k, nt in zip(keys, notes)]
        # measure with the same math used to draw (explicit baselines)
        total = 40 + len(lefts) * 37 + 8
        for r in rights:
            total += len(wrap(r, "serif", False, 23, self.w - 34)) * 33 + 5
        total += gap
        self._fit(total)
        x, y = self.x, self.y
        chip(self.p, x, y, level)
        self.p.text(x + 72, y + 23, f"{nums[0]}–{nums[-1]}.", 24, "sans", True, OLIVE)
        if instr:
            self.p.text(x + 196, y + 23, instr, 19.5, "sans", False, GREY)
        yy = y + 40 + 24
        for num, l in zip(nums, lefts):
            self.p.text(x, yy, f"{num}. {l}", 24, "serif", False, INK)
            yy += 37
        yy += 8
        for i, r in enumerate(rights):
            for j, ln in enumerate(wrap(r, "serif", False, 23, self.w - 34)):
                self.p.text(x + 34, yy, (f"{chr(97+i)}. " if j == 0 else "") + ln, 23, "serif", False, GREY)
                yy += 33
            yy += 5
        self.y = yy + gap
        return nums

    def end_report(self):
        print(f"  flow[{self.tag}] ended col {self.ci}/{len(self.cols)-1} y={self.y:.0f} (bottom {self.bottom})")
