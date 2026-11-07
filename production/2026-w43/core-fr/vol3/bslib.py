# -*- coding: utf-8 -*-
"""Broadsheet extension: 1560x2160 pages, 3 columns, dense newspaper flow."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import *

PW, PH = 1560, 2160
MX = 52                      # left/right margin
CW = 464                     # column width
GUT = 32
COLX = [MX, MX + CW + GUT, MX + 2 * (CW + GUT)]   # 52, 548, 1044
RIGHT = MX + 3 * CW + 2 * GUT                     # 1508

def span_x(i, n=1):
    """x and width for a block starting at column i spanning n columns."""
    return COLX[i], n * CW + (n - 1) * GUT

class BSPage(Page):
    def __init__(self):
        self.w, self.h = PW, PH
        self.parts = []
        self.add(f'<rect width="{PW}" height="{PH}" fill="{PAPER}"/>')
        self.add(f'<rect x="24" y="24" width="{PW-48}" height="{PH-48}" fill="none" stroke="{INK}" stroke-width="3.4"/>')
        self.add(f'<rect x="35" y="35" width="{PW-70}" height="{PH-70}" fill="none" stroke="{INK}" stroke-width="1.2"/>')

    def band(self, title_left, title_right, sub=""):
        self.rect(44, 44, PW - 88, 92, fill=DARK)
        self.text(68, 105, title_left, 34, "sans", True, "#f3edda")
        self.text(PW - 68, 105, title_right, 34, "serif", True, "#f3edda", anchor="end")
        if sub:
            self.text(PW - 68, 130, sub, 19, "sans", False, "#b3a06a", anchor="end")
        return 160

    def foot(self, n, total=5):
        self.hline(MX, RIGHT, 2052, GOLD, 1.6)
        self.text(MX, 2090, "每日一句 · 法语周报 VOL.1 · LUCERNA FRENCH WEEKLY", 20, "sans", False, GREY)
        self.text(RIGHT, 2090, f"第 {n} 版 / 共 {total} 版", 20, "sans", False, GREY, anchor="end")

    def shead(self, x, y, s, w, size=29, color=OLIVE):
        self.text(x, y, s, size, "sans", True, color)
        self.hline(x, x + w, y + 13, GOLD, 2)
        return y + 13

    def article(self, x, y, title, body, w, tsize=30, bsize=24, blh=1.5, tcolor=INK):
        y = self.para(x, y, title, tsize, "serif", True, tcolor, w, 1.25) + 6
        y = self.para(x, y, body, bsize, "serif", False, INK, w, blh)
        return y

    def item(self, x, y, head, body, w, hsize=24, bsize=23, blh=1.48, hcolor=INK):
        if head:
            y = self.para(x, y, head, hsize, "serif", True, hcolor, w, 1.3) + 3
        y = self.para(x, y, body, bsize, "serif", False, INK, w, blh)
        return y
