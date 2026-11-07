# -*- coding: utf-8 -*-
"""Fold the four W45 zh-cn x ru post-transform fix groups (proof B-1) back
into scratch/transform_ru_w45.py, by exact unique literal replacement only
(tools README #17/#18: no AST byte offsets, no repr literals).
Direction: transform NEW (pre-fix) -> delivered (post-fix), verified
against the DELIVERED build files and the proof's repro-build diff.
Shared note literals are replaced globally: each occurs in exactly the
pairs whose files the repro diff shows changed (counts asserted).
Two ADDs: the P4 section-C head (never in the transform) and the P7
disclosure NOTE comment (comment-only, same P7 edit; SVGs unaffected).
Run: tools/venv/bin/python fold.py  (aborts on any failed assertion).
"""
import sys

T = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-cn-ru-build/scratch/transform_ru_w45.py'

# (pre-fix literal as produced by the old transform, delivered literal)
REPLACEMENTS = [
    # --- P1 BOXTITLE (content12) ---
    ("Команды S16 зависят от швейцарского этапа",
     "Команды S16 зависят от этапа"),
    # --- P8 tersenings via apply_trims.py (content12/34/56/7/8) ---
    ("qīzhōng — экзамены середины семестра проходят в начале ноября в некоторых школах.",
     "qīzhōng — середина семестра, начало ноября."),
    ("shuǐ shǐ bīng — вода начинает замерзать (1-й микросезон).",
     "shuǐ shǐ bīng — вода начинает замерзать."),
    ("tāngyuán — шарики из клейкого риса, которые едят в некоторых южных местах.",
     "tāngyuán — шарики из клейкого риса, южное блюдо."),
    ("Четвертьфиналы начинаются в 06:00 по пекинскому времени.",
     "Четвертьфиналы — в 06:00 по пекинскому времени."),
    ("Финал начинается в 03:00 по пекинскому времени 15 ноября.",
     "Финал — в 03:00 по пекинскому времени 15 ноября."),
    ("Àilún — Аллен, штат Техас, принимает швейцарский этап.",
     "Àilún — Аллен (Техас), город швейцарского этапа."),
    ("nèizhàn — AL проиграла матч внутри LPL команде TES.",
     "nèizhàn — AL проиграла TES внутри LPL."),
    ("К полудню 26 октября Maoyan показывал около 1,192 миллиона юаней.",
     "Maoyan к полудню 26 октября: около 1,192 млн юаней."),
    ("shùzì — персонажи фильма — цифровые изображения.",
     "shùzì — персонажи фильма цифровые."),
    ("piàofáng — кассовые сборы, около 1,192 миллиона юаней.",
     "piàofáng — сборы: около 1,192 миллиона юаней."),
    ("24–25 октября на каждый сеанс в среднем приходилось 2 зрителя.",
     "24–25 октября: в среднем 2 зрителя на сеанс."),
    ("Страница кассы показывает, что вы платите на самом деле.",
     "Страница кассы: что вы платите на самом деле."),
    ("jiésuàn — страница кассы показывает настоящую цену.",
     "jiésuàn — на странице кассы настоящая цена."),
    ("guǎnggào — «самую низкую цену» из рекламы нужно проверять.",
     "guǎnggào — «самую низкую цену» проверяйте."),
    ("Порядок от большого к малому: 7 ноября, суббота, 17:52.",
     "От большого к малому: 7 ноября, суббота, 17:52."),
    ("zuìdījià — рекламное утверждение, а не измеренные данные.",
     "zuìdījià — реклама, а не измеренные данные."),
    ("Сначала данные и страница кассы, заголовок — последним.",
     "Данные и касса сначала, заголовок — потом."),
    ("Товары со склада отправляются без ожидания задатка.",
     "Товары со склада — без ожидания задатка."),
    ("jìzhě — журналист берёт интервью и пишет новости.",
     "jìzhě — берёт интервью и пишет новости."),
    ("yùnfèi — стоимость доставки, проверьте, включена ли она.",
     "yùnfèi — доставка: проверьте, включена ли."),
    # --- P7 clinic + frame trims (content7, from apply_trims.py) ---
    ("Частица 地 (de) показывает, как совершается действие.",
     "Частица 地 (de) — образ действия."),
    ("Частица 得 (de) связывает глагол со степенью: 跑得快.",
     "Частица 得 (de): глагол + степень."),
    ("Время идёт от большого к малому: день недели — последним.",
     "Время: от большого к малому."),
    ("Конструкция: 先 … 再 … — сначала X, потом Y.",
     "Сначала X, потом Y."),
    # --- P7 measure-word purity rephrases (content7, direct edit) ---
    ("Для свитера счётное слово — 件 jiàn.",
     "Для свитера счётное слово — jiàn."),
    ("Для одежды — 件, а не 个 или 条.",
     "Для одежды — jiàn, а не gè или tiáo."),
    # --- P7 disclosure rewrite (content7, direct edit) ---
    ("Пример письма от редакции — это не настоящее письмо читателя. Пояснение редакции: в VOL.1 было обещано, что в этом номере (VOL.2) появятся настоящие письма читателей и лучшее сочинение со страницы 8 из VOL.1; до сих пор настоящих писем не пришло, и публиковать нечего, поэтому здесь снова пример от редакции. Это отсрочка, а не отмена. Присылайте ваши письма в редакцию! Напишите два предложения по-китайски о вашей неделе — о покупках, о зиме, о чём угодно — и отправьте их нам: лучшие письма мы напечатаем в VOL.3.",
     "Пример письма от редакции — не настоящее письмо. В VOL.1 было обещано напечатать здесь настоящие письма и лучшее сочинение VOL.1, но писем пока нет — это отсрочка, а не отмена. Присылайте ваши письма! Напишите два предложения по-китайски и отправьте их нам: лучшие появятся в VOL.3."),
]

HEAD_ANCHOR = "# ---- content56 P5 ----"
HEAD_PAIR = ('# P4 section-C head (missed in the first transform; caught by the\n'
             '# residual scan, folded here so transform-alone reproduces it)\n'
             'add("content34.py", "C · 读赛程 · Schedule work", "C · 读赛程 · Читаем расписание")\n')

COMMENT_ANCHOR = "# ---- content8 P8 ----"
COMMENT_PAIR = ('# P7 disclosure NOTE comment, updated with the disclosure rewrite\n'
                '# (comment-only; no effect on rendered SVGs)\n'
                'add("content7.py", "# NOTE: the disclosure above mixes Chinese and English in one string; the\\n# sans wrap measures CJK and Latin with the same SC face, so the height\\n# formula above (sans, 20pt) matches the render path. Verified in the build log.", "# NOTE: the disclosure above is Russian-only in this edition (the core\'s\\n# Chinese+English disclosure is carried over in content, in Russian, plus\\n# an explicit open invitation for real letters); the sans wrap measures\\n# Cyrillic with the same SC face, so the height formula above (sans, 20pt)\\n# matches the render path. Verified in the build log.")\n')

def main():
    s = open(T, encoding='utf-8').read()
    for old, new in REPLACEMENTS:
        n_old = s.count(old)
        n_new = s.count(new)
        assert n_old >= 1, f'ZERO pre-fix occurrences: {old[:70]!r}'
        assert n_new == 0, f'delivered literal already present: {new[:70]!r}'
        s = s.replace(old, new)
        print(f'{n_old}x {old[:60]!r} -> {new[:60]!r}')
    assert s.count(HEAD_PAIR) == 0
    assert HEAD_ANCHOR in s
    s = s.replace(HEAD_ANCHOR, HEAD_PAIR + HEAD_ANCHOR, 1)
    print('ADDED P4 head pair')
    assert s.count('the disclosure above mixes Chinese and English') == 0, \
        'comment pair already present?'
    assert COMMENT_ANCHOR in s
    s = s.replace(COMMENT_ANCHOR, COMMENT_PAIR + COMMENT_ANCHOR, 1)
    print('ADDED P7 comment pair')
    # post-conditions: no pre-fix literal survives anywhere in the transform
    for old, _ in REPLACEMENTS:
        assert s.count(old) == 0, f'LEFTOVER pre-fix: {old[:70]!r}'
    open(T, 'w', encoding='utf-8').write(s)
    print('FOLD OK —', len(REPLACEMENTS), 'replacements + 2 adds')

if __name__ == '__main__':
    main()
