#!/usr/bin/env python3
"""Build a small TEXT-LAYER web PDF from an edition's 8 page SVGs.

Why this exists (2026-10-28): the old web PDF was 8 full-page JPEGs
(PIL save_all) with no text layer at all, so search engines index
nothing (pdftotext returns 0 bytes). The print PDF has full text but
is ~31 MB (full-res images + full CJK fonts). This tool produces the
third option: real vector text + downscaled images + fontTools-subset
fonts, typically 2-4 MB with text byte-identical to the print PDF.

Pipeline per edition:
  1. Collect the union of characters used in <text> elements.
  2. Resolve each font-family via fontconfig (fc-match) to a system
     font file + face index; subset it to the used chars with a
     renamed family (Lucerna*) so fontconfig picks the subset, never
     the system full font. Bold variants get their own subset.
  3. Downscale embedded base64 images to web-page resolution
     (display width x page_px / page_width, JPEG q85; PNG kept if
     it carries alpha).
  4. Rewrite font-family names in the SVGs, render each page with
     CairoSVG under an isolated fontconfig (FONTCONFIG_PATH pointing
     at the subset dir), merge with pypdf.
  5. Verify: pdftotext must return non-empty text; report size,
     embedded fonts, text bytes. Exit non-zero on empty text.

Usage:
  webpdf.py <svg-dir> <out.pdf> [--page-px 1400]

Requires: cairosvg, pillow, pypdf, fonttools, poppler-utils
(pdftotext/pdffonts, for verification only), fontconfig (fc-match,
fc-cache). All are in tools/venv except poppler/fontconfig, which
are system packages.
"""

import argparse
import base64
import glob
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

PAGE_W = 1950.0  # weekly page width in SVG units (tables.json page.width)


def collect_chars_and_families(svg_files):
    """Union of chars inside <text> elements + font families used."""
    chars = set()
    families = set()
    for f in svg_files:
        svg = open(f, encoding='utf-8').read()
        for m in re.finditer(r'<text\b[^>]*>(.*?)</text>', svg, re.S):
            inner = re.sub(r'<[^>]+>', '', m.group(1))
            chars.update(inner)
        for m in re.finditer(r'font-family="([^"]+)"', svg):
            for fam in m.group(1).split(','):
                fam = fam.strip().strip("'\"")
                if fam:
                    families.add(fam)
    chars.discard('\n')
    chars.discard('\t')
    return chars, families


def fc_match(family, bold=False):
    """Resolve a family to (file, index) via fontconfig, or None."""
    query = family + (':style=Bold' if bold else '')
    try:
        out = subprocess.run(
            ['fc-match', '-f', '%{file}|%{index}\n', query],
            capture_output=True, text=True, timeout=30)
        file_, index = out.stdout.strip().split('|')
        if file_ and os.path.exists(file_):
            return file_, int(index)
    except Exception:
        pass
    return None


def subset_font(src, index, chars, new_family, weight, subfam, out_path):
    """Subset one font file/face to chars, rename family, save TTF."""
    from fontTools.ttLib import TTFont
    from fontTools import subset
    font = TTFont(src, fontNumber=index, lazy=False)
    sub = subset.Subsetter()
    sub.populate(unicodes=[ord(c) for c in sorted(chars)])
    sub.subset(font)
    name = font['name']
    for nid in (1, 16):
        name.setName(new_family, nid, 3, 1, 0x409)
    name.setName(new_family + '-' + subfam, 6, 3, 1, 0x409)
    name.setName(new_family + ' ' + subfam, 4, 3, 1, 0x409)
    font['OS/2'].usWeightClass = weight
    if weight >= 700:
        font['OS/2'].fsSelection |= 0x20  # BOLD bit
    else:
        font['OS/2'].fsSelection &= ~0x20
    font.save(out_path)
    return os.path.getsize(out_path)


def build_subsets(chars, families, font_dir):
    """Subset every used family (regular + bold). Returns rename map."""
    from fontTools.ttLib import TTFont  # noqa: F401 (import check)
    rename = {}
    for fam in sorted(families):
        safe = re.sub(r'[^A-Za-z0-9]', '', fam)
        new_family = 'Lucerna' + safe
        ok = False
        for bold, subfam, weight in ((False, 'Regular', 400),
                                     (True, 'Bold', 700)):
            match = fc_match(fam, bold=bold)
            if not match:
                continue
            src, index = match
            out = os.path.join(font_dir, f'{new_family}-{subfam}.ttf')
            try:
                # Skip a bold subset identical to the regular one.
                if bold and match == fc_match(fam, bold=False):
                    continue
                size = subset_font(src, index, chars, new_family,
                                   weight, subfam, out)
                print(f'  font {new_family}-{subfam}: {size} bytes',
                      file=sys.stderr)
                ok = True
            except Exception as e:
                print(f'  WARN subset failed for {fam} {subfam}: {e}',
                      file=sys.stderr)
        if ok:
            rename[fam] = new_family
        else:
            print(f'  WARN no subset for {fam}; system font will be used '
                  f'(PDF still has text, but may be larger)',
                  file=sys.stderr)
    return rename


def downscale_images(svg, scale):
    """Downscale embedded base64 images to web resolution, in place."""
    def repl(m):
        tag = m.group(0)
        hm = re.search(
            r'(xlink:href|href)="data:(image/(?:jpeg|png));base64,([^"]+)"',
            tag)
        if not hm:
            return tag
        wm = re.search(r'\bwidth="([\d.]+)"', tag)
        if not wm:
            return tag
        disp_px = float(wm.group(1)) * scale
        try:
            b64raw = re.sub(r'\s+', '', hm.group(3))
            b64raw += '=' * (-len(b64raw) % 4)
            im = Image.open(io.BytesIO(base64.b64decode(b64raw)))
            w, h = im.size
            if w <= disp_px:
                return tag
            nw = int(disp_px)
            nh = max(1, int(h * disp_px / w))
            im2 = im.resize((nw, nh), Image.LANCZOS)
            buf = io.BytesIO()
            if im2.mode in ('RGBA', 'LA') or \
                    (im2.mode == 'P' and 'transparency' in im2.info):
                im2.save(buf, 'PNG', optimize=True)
            else:
                if im2.mode != 'RGB':
                    im2 = im2.convert('RGB')
                im2.save(buf, 'JPEG', quality=85)
            return (tag[:hm.start(3)] +
                    base64.b64encode(buf.getvalue()).decode() +
                    tag[hm.end(3):])
        except Exception as e:
            print(f'  WARN image downscale skipped: {e}', file=sys.stderr)
            return tag
    return re.sub(r'<image\b[^>]*>', repl, svg)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('svg_dir', help='directory with the 8 page SVGs')
    ap.add_argument('out_pdf', help='output PDF path')
    ap.add_argument('--page-px', type=float, default=1400.0,
                    help='web page width in px (default 1400)')
    args = ap.parse_args()

    svg_files = sorted(glob.glob(os.path.join(args.svg_dir, '*.svg')))
    if not svg_files:
        print('no SVGs in', args.svg_dir, file=sys.stderr)
        return 2
    print(f'{len(svg_files)} pages from {args.svg_dir}', file=sys.stderr)

    chars, families = collect_chars_and_families(svg_files)
    print(f'{len(chars)} distinct chars; families: {sorted(families)}',
          file=sys.stderr)

    tmp = tempfile.mkdtemp(prefix='webpdf-')
    font_dir = os.path.join(tmp, 'fonts')
    os.makedirs(font_dir)
    fc_dir = os.path.join(tmp, 'fc')
    os.makedirs(os.path.join(fc_dir, 'cache'))

    rename = build_subsets(chars, families, font_dir)

    # Isolated fontconfig: subsets first, system dirs as fallback.
    # (Renamed families never collide with system fonts.)
    home_fonts = os.path.expanduser('~/.local/share/fonts')
    conf = ('<?xml version="1.0"?>\n'
            '<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n'
            '<fontconfig>\n'
            f'  <dir>{font_dir}</dir>\n'
            '  <dir>/usr/share/fonts</dir>\n'
            f'  <dir>{home_fonts}</dir>\n'
            f'  <cachedir>{fc_dir}/cache</cachedir>\n'
            '</fontconfig>\n')
    open(os.path.join(fc_dir, 'fonts.conf'), 'w').write(conf)
    env = dict(os.environ, FONTCONFIG_PATH=fc_dir)
    subprocess.run(['fc-cache', '-f', font_dir],
                   env=env, capture_output=True)

    # Rewrite SVGs into the temp dir (so relative refs still resolve).
    scale = args.page_px / PAGE_W
    rewritten = []
    for f in svg_files:
        svg = open(f, encoding='utf-8').read()
        svg = downscale_images(svg, scale)
        for old, new in rename.items():
            svg = svg.replace(f'font-family="{old}"',
                              f'font-family="{new}"')
            svg = svg.replace(f'font-family:{old}',
                              f'font-family:{new}')
        out = os.path.join(tmp, os.path.basename(f))
        open(out, 'w', encoding='utf-8').write(svg)
        rewritten.append(out)

    # Render AFTER the env is set (fontconfig inits lazily on first use).
    os.environ['FONTCONFIG_PATH'] = fc_dir
    import cairosvg
    from pypdf import PdfWriter
    writer = PdfWriter()
    for f in rewritten:
        page_pdf = os.path.join(tmp, 'page.pdf')
        cairosvg.svg2pdf(url=f, write_to=page_pdf)
        writer.append(page_pdf)
    writer.write(open(args.out_pdf, 'wb'))

    # Verify.
    size = os.path.getsize(args.out_pdf)
    text_bytes = 0
    try:
        r = subprocess.run(['pdftotext', args.out_pdf, '-'],
                           capture_output=True, timeout=120)
        text_bytes = len(r.stdout)
    except Exception:
        pass
    print(f'WROTE {args.out_pdf}: {size} bytes, {text_bytes} text bytes')
    if text_bytes == 0:
        print('ERROR: no extractable text in output', file=sys.stderr)
        return 1
    shutil.rmtree(tmp, ignore_errors=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
