# -*- coding: utf-8 -*-
"""Fix round 2: shorten 2-line P8 key notes to 1 line (notes print only in
keys, so exercise pages are unaffected) + P7 col3 cuts so the teaser
clears the footer band. All replacements asserted."""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = [
    ("content12.py", "Cette année, beaucoup de marchandises sont soldées directement.",
     "Cette année, les marchandises baissent directement."),
    ("content12.py", "Les ventes de stock de Taobao et Tmall ont commencé le 20 octobre.",
     "Ventes de stock Taobao et Tmall dès le 20 octobre."),
    ("content12.py", "xiànhuò — marchandises en stock, prêtes à être expédiées.",
     "xiànhuò — marchandises en stock, prêtes à partir."),
    ("content56.py", "xiànhuò — marchandises en stock, prêtes à être expédiées.",
     "xiànhuò — marchandises en stock, prêtes à partir."),
    ("content12.py", "qīzhōng — examens de mi-trimestre début novembre dans certaines écoles.",
     "qīzhōng — examens de mi-trimestre, début novembre."),
    ("content34.py", "shuǐ shǐ bīng — l'eau commence à geler, 1re micro-saison.",
     "shuǐ shǐ bīng — l'eau commence à geler."),
    ("content34.py", "tāngyuán — boules de riz gluant mangées dans certains endroits du Sud.",
     "tāngyuán — boules de riz gluant du Sud."),
    ("content34.py", "La finale commence à 03 h 00, heure de Pékin, le 15 novembre.",
     "Finale le 15 novembre, 03 h 00, heure de Pékin."),
    ("content8.py", "La finale commence à 03 h 00, heure de Pékin, le 15 novembre.",
     "Finale le 15 novembre, 03 h 00, heure de Pékin."),
    ("content34.py", "táotài — trois victoires envoient une équipe en éliminatoires.",
     "táotài — trois victoires, direction les éliminatoires."),
    ("content34.py", "Trois victoires qualifient une équipe issue de la phase suisse.",
     "Trois victoires pour passer la phase suisse."),
    ("content56.py", "shùzì — les personnages du film sont des images numériques.",
     "shùzì — personnages du film en images numériques."),
    ("content56.py", "piàofáng — recettes au box-office, environ 1,192 million de yuans.",
     "piàofáng — recettes, environ 1,192 million de yuans."),
    ("content56.py", "Cette année, les ventes de stock sont bien plus importantes.",
     "Cette année, bien plus de ventes de stock."),
    ("content56.py", "guǎnggào — le « prix le plus bas » d'une publicité doit être vérifié.",
     "guǎnggào — le « prix le plus bas » est à vérifier."),
    ("content7.py", "「最低价」 est une affirmation publicitaire, pas une donnée mesurée.",
     "「最低价」 : affirmation publicitaire, pas donnée mesurée."),
    ("content7.py", "Les données et la page de caisse d'abord ; le titre en dernier.",
     "Données et page de caisse d'abord, titre en dernier."),
    ("content8.py", "Les marchandises en stock partent sans attendre un acompte.",
     "Marchandises en stock : départ sans acompte."),
    ("content8.py", "Les quarts de finale commencent à 06 h 00, heure de Pékin.",
     "Quarts de finale : 06 h 00, heure de Pékin."),
    ("content8.py", "À midi le 26 octobre, Maoyan affichait environ 1,192 million de yuans.",
     "Maoyan, 26 oct. à midi : environ 1,192 million de yuans."),
    ("content8.py", "shùzì — les personnages du film IA sont des images numériques.",
     "shùzì — personnages du film IA en images numériques."),
    ("content8.py", "f\"Tâche ouverte — le modèle est imprimé dans la section F ci-dessus, {NCHARS} caractères\"",
     "f\"Tâche ouverte — modèle section F, {NCHARS} caractères\""),
    ("content12.py", "L'opération de la boutique WeChat dure 35 jours au total.",
     "Boutique WeChat : 35 jours au total."),
    # P7 col3 cuts
    ("content7.py", "Nombre + classificateur + nom. Le 个 final est en trop ; les pulls prennent 件.",
     "Nombre + classificateur + nom. Le 个 est en trop."),
    ("content7.py", "Les heures vont du grand au petit : le jour de semaine en dernier.",
     "Du grand au petit, le jour de semaine en dernier."),
    ("content7.py", "「先看评价,再下单。」(Vérifiez les avis, puis commandez.) La structure 先…再… donne l'ordre des actions. Plus : 「先看天气,再出门。」",
     "「先看评价,再下单。」(Vérifiez les avis, puis commandez.) La structure 先…再… donne l'ordre des actions."),
    ("content7.py", "Note de la rédaction : le VOL.1 avait promis de vraies lettres et la meilleure rédaction du VOL.1 dans ce VOL.2. Aucune n'est arrivée : ce coin publie encore un exemple de la rédaction. Reporté, pas annulé. Et vous, écrivez-nous ! Envoyez votre lettre en chinois, nous la publierons ici.",
     "Note de la rédaction : le VOL.1 avait promis pour ce numéro de vraies lettres et la meilleure rédaction du VOL.1. Aucune n'est arrivée : ce coin publie encore un exemple de la rédaction. Reporté, pas annulé. Et vous, écrivez-nous ! Envoyez votre lettre en chinois, nous la publierons ici."),
]
failed = []
for fn, old, new in FIX:
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
print("fixup2 OK")
