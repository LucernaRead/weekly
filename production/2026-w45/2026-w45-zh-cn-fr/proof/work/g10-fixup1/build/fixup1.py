# -*- coding: utf-8 -*-
"""Fix round 1 on the zh-cn x fr build copy (never on the core):
band titles per W43 FR shipped precedent, 2 missed notes, comma
NOTE 2026-10-28: SUPERSEDED by the folded transform.py (Gate 10 path is transform alone).
Kept for build history only; do not re-run on post-fix sources (entries already applied).
rewordings (kill the 4 added full-width commas at source), head
shortenings, P7 col3 shortening, P8-keys shortening."""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = [
    ("content12.py", "生活 · Life", "生活 · Vie quotidienne"),
    ("content34.py", "文化 · Culture", "文化 · Culture"),  # already French-identical; no-op guard below
    ("content34.py", "体育 · Sport", "体育 · Sport"),
    ("content56.py", "青年 · Youth", "青年 · Jeunesse"),
    ("content56.py", "深读 · Deep read", "深读 · Lecture approfondie"),
    ("content7.py", "词语 · Language focus", "词语 · Focus langue"),
    ("content8.py", "测验与答案 · Test & keys", "测验与答案 · Test et réponses"),
    # missed notes (English remnants in build 1)
    ("content56.py", "The WeChat shop event runs 35 days.", "L'opération de la boutique WeChat dure 35 jours."),
    ("content8.py", "The WeChat shop event runs 35 days.", "L'opération de la boutique WeChat dure 35 jours."),
    ("content8.py", "The new film opens on Nov 7.", "Le nouveau film sort le 7 novembre."),
    # comma rewordings: no comma adjacent to a cited CJK word (svglib turns it into ，)
    ("content12.py", "Après 立冬, le temps devient plus froid de jour en jour.",
     "Après 立冬 le temps devient plus froid de jour en jour."),
    ("content56.py", "Avec 直降, le prix à la caisse est celui que vous payez.",
     "Avec 直降 le prix à la caisse est celui que vous payez."),
    ("content7.py", "06 h 00, c'est 早上, le matin, pas le soir.",
     "06 h 00 correspond à 早上 et non au soir."),
    ("content8.py", "Pour 立冬, elle a fait des raviolis avec sa mère.",
     "Pour 立冬 elle a fait des raviolis avec sa mère."),
    # head shortenings (measured: 424.2 and 402.5 vs 434 column)
    ("content56.py", "C · 时间与数字 · Heures et nombres", "C · 时间与数字 · Heures, nombres"),
    ("content56.py", "C · 练习篮子算一算 · Calcul des paniers", "C · 练习篮子算一算 · Les paniers"),
    # P7 col3 shortening: clinic #3, frame, readers' corner French note
    ("content7.py",
     "Ordre : nombre + classificateur + nom. Le 个 final est un de trop ; les pulls prennent 件.",
     "Nombre + classificateur + nom. Le 个 final est en trop ; les pulls prennent 件."),
    ("content7.py",
     "「先看评价,再下单。」(D'abord vérifier les avis, puis commander.) La structure 先…再… donne l'ordre des actions. Autre exemple : 「先看天气,再出门。」",
     "「先看评价,再下单。」(Vérifiez les avis, puis commandez.) La structure 先…再… donne l'ordre des actions. Plus : 「先看天气,再出门。」"),
    ("content7.py",
     "Note de la rédaction : le VOL.1 avait promis de vraies lettres de lecteurs et la meilleure rédaction du VOL.1 dans ce VOL.2. Aucune n'est arrivée, donc ce coin publie encore un exemple de la rédaction. Ce n'est pas annulé, c'est reporté. Et vous, écrivez-nous ! Envoyez votre lettre en chinois et votre rédaction : nous les publierons ici dès qu'elles arriveront.",
     "Note de la rédaction : le VOL.1 avait promis de vraies lettres et la meilleure rédaction du VOL.1 dans ce VOL.2. Aucune n'est arrivée : ce coin publie encore un exemple de la rédaction. Reporté, pas annulé. Et vous, écrivez-nous ! Envoyez votre lettre en chinois, nous la publierons ici."),
    # P8-keys shortening: save wrapped lines (notes print only in keys)
    ("content12.py", "Les ventes de stock de JD.com ont commencé le 12 octobre.",
     "Ventes de stock JD.com dès le 12 octobre."),
    ("content12.py", "Les préventes de Taobao et Tmall ont commencé le 15 octobre.",
     "Préventes Taobao et Tmall dès le 15 octobre."),
    ("content12.py", "Les ventes de stock durent jusqu'au 13 novembre.",
     "Ventes de stock jusqu'au 13 novembre."),
    ("content12.py", "L'opération de la boutique WeChat dure jusqu'au 15 novembre.",
     "Boutique WeChat jusqu'au 15 novembre."),
    ("content56.py", "À midi le 26 octobre, Maoyan affichait environ 1,192 million de yuans.",
     "Maoyan, 26 oct. à midi : environ 1,192 million de yuans."),
    ("content56.py", "Les 24 et 25 octobre, chaque séance comptait en moyenne 2 spectateurs.",
     "24 et 25 oct. : 2 spectateurs en moyenne par séance."),
    ("content12.py", "L'opération de la boutique WeChat dure 35 jours au total.",
     "Boutique WeChat : 35 jours au total."),  # REPAIRED 2026-10-28: was content56.py (stale — string never existed there; proof B3)
]
failed = []
for fn, old, new in FIX:
    if old == new:
        continue
    p = os.path.join(HERE, fn)
    s = io.open(p, encoding="utf-8").read()
    c = s.count(old)
    print(f"{fn}: {c} x {old[:60]}")
    if c == 0:
        failed.append((fn, old))
    else:
        io.open(p, "w", encoding="utf-8").write(s.replace(old, new))
if failed:
    print("FAILED:")
    for f in failed:
        print("  !!", f)
    sys.exit(1)
print("fixup1 OK")
