# A Lucerna VOL.1 — Édition PT × FR (W43)

- **Pairing** : texte en portugais (brésilien) + explications en français — l'édition pour les lecteurs francophones.
- **Week** : 2026-W43 · Semana de 19 a 25 de outubro de 2026 · VOL.1
- **Source** : édition noyau PT × zh-CN (`files/weekly-report-pt-vol1/`, fichiers livrés après les correctifs géométriques P7/P8 de l'audit du programme). Le texte portugais est **gelé** : seul le niveau d'explication a été réécrit, en français natif et intégral (gloses, notes de grammaire, consignes, et la totalité des notes de réponses page 8).
- **Build dir** : `hidden_files/weekly-report-pt-fr-build/` (copie du build du noyau). La copie non modifiée a d'abord reproduit les 8 SVG livrés du noyau **à l'octet près** (md5 vérifiés avant toute modification).

## Specs

- 8 pages, 1950×2700, 4 colonnes, ivoire chaud #f7f1e2, accents olive profond / rouge brique #a4553a.
- **150 exercices** — A2 44 · B1 75 · B2 31 ; par page 10/18/18/18/18/18/12/38. Registre (n°, page, niveau, type) **identique** au noyau, vérifié par dump des deux registres.
- Masthead : **A Lucerna**. Ligne d'édition page 1 : « JOURNAL PORTUGAIS · VOL.1 · O SEGUNDO TURNO · O DEBATE FINAL · O ENEM VEM AÍ » (36 pt, encre mesurée 1612 px ≤ 1820 — la variante HEBDOMADAIRE tient aussi sur cette page, 1600 px, mais le format JOURNAL est celui des éditions sœurs EN×FR/IT×FR).
- **Badge page 1** (rouge brique, remplace la ligne de signature du noyau) : « TEXTES EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES »
- Bandeau supérieur page 1 : « TODA SEMANA EM PORTUGUÊS · CHAQUE SEMAINE · LE PORTUGAIS QUE LIT LE BRÉSIL » ; bandeau noir à droite : « DIMANCHE, JOUR DE DÉCISION » / « Second tour de la présidentielle · voir page 6 ».
- **Pieds de page (8 pages)** : « A Lucerna · HEBDOMADAIRE PORTUGAIS VOL.1 · TEXTE EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS » et « Page N sur 8 ».
- Préfixe des boîtes de gloses : « Note — ». Typographie des réponses : espace avant chaque parenthèse de note, parenthèses demi-chasse uniquement.

## Key-diff registry (FR vs noyau — seuls les items documentés diffèrent)

Le corps des réponses est identique au noyau pour 147 items sur 150. Différences, toutes dans la couche lecteur :

| # | Type | Noyau (zh-CN) | Cette édition (FR) |
|---|------|---------------|--------------------|
| 137 | Traduire (PT→langue du lecteur) | clé = traduction chinoise de la phrase PT | clé = « Dimanche, le Brésil retourne aux urnes. » — note « (titre page 1) » |
| 138 | Traduire (PT→langue du lecteur) | clé = traduction chinoise de la phrase PT | clé = « Vérifiez votre bureau de vote avant de partir de chez vous. » — note « Confira = vérifiez » |
| 139 | Traduire — **consigne réorientée** | PT→chinois | consigne en français : « Les recherches de « guitarra » ont augmenté de 53 %. » → réponse en portugais « As buscas por guitarra cresceram 53%. » (corps PT identique au noyau) |
| 140 | Traduire — **consigne réorientée** | PT→chinois | consigne en français : « Quand vous arriverez, vérifiez votre bureau de vote. » → réponse en portugais « Quando você chegar, confira a seção. » (corps PT identique au noyau) |
| 150 | Écrire — ligne d'appareil | « Question ouverte — texte modèle ci-dessous… » (appareil chinois dans le noyau) | clé « Question ouverte — texte modèle ci-dessous sur cette page », note « Texte modèle dans la section H de cette page (92 mots) » |

Aucune autre clé ne diffère. Les types d'exercices dans le code (完成句子/单选/词汇配对/造句/判断对错/完形单选/翻译/写作) sont des métadonnées de registre, jamais imprimées — identiques dans toutes les éditions sœurs.

## Fit shortenings (couche française uniquement — texte portugais et géométrie du noyau intacts)

Trouvés par l'audit géométrique en cours de build, corrigés en raccourcissant l'appareil français :

1. **P1, boîte AS BUSCAS** : la note de bas de boîte dépassait la page (encre jusqu'à x=2230). Raccourcie : « Données Google : ce n'est pas un vote. » (336 px ≤ 390).
2. **P1, sous-titre AS BUSCAS** : dépassait le bord de boîte de 4,7 px. « Recherches du Brésil · as buscas no Google » (390 px).
3. **P1, A PALAVRA DA SEMANA** : la glose française sur 2 lignes plaquait sa 2e ligne sur le filet y=1844 (collision réelle, mesurée). Raccourcie en 1 ligne : « « Le bureau de vote » : l'endroit exact du vote. »
4. **P1, titre de boîte A SEMANA EM NÚMEROS · CHIFFRES** : dépassait le bord de 3,6 px à 23 pt → titre rendu à 21 pt (383 px).
5. **P7, titre ERROS COMUNS** : « · ERREURS FRÉQUENTES » dépassait le bord de boîte de 68,8 px et le bord de page. Titre : « ERROS COMUNS · ERREURS » (323 px).
6. **P7, colonne 3** : les notes françaises allongeaient la pile (fin à y=1810 contre 1663 dans le noyau), ce qui poussait la 4e rangée de citations sous le bandeau sombre « PRÓXIMA SEMANA » (citations couvertes à 69–100 % — défaut réel, attrapé par l'audit). 4 notes ERROS ramenées à 1 ligne chacune (« assistir (voir) prend a : ao debate. », « en et la : espagnol ; em + a = na. », « esquisito = bizarre, pas « délicieux ». », « mas = mais ; mais = plus. ») et note A PALAVRA raccourcie à 2 lignes → pile revenue à y=1663, géométrie des citations identique au noyau.
7. **P8, notes de réponses** : 12 notes raccourcies d'exactement 1 ligne chacune (vérifié avec le compteur de lignes de production) pour tenir le flux des clés dans la page : #32, #46, #69, #81, #89, #91, #100, #117, #135, #137, #139, #144. Deux raccourcissements essayés (#98, #134) n'économisaient aucune ligne — notes complètes conservées.
8. **P6, consignes** : A « Choisissez d'après les graphiques ci-dessus. », C « Complétez avec la forme verbale correcte. », D « Complétez : segundo turno · maioria absoluta · votos válidos · intenção de voto » (le flux P6 se termine à y=2519, bas de page 2580).

Espacements typographiques : espace ajoutée avant les gloses parenthétiques des encadrés P1 (×3) et P5 (×5), comme dans l'édition sœur PT×DE.

## Audits (gates SOP)

- **Audit d'occlusion géométrique** (ordre de peinture, métriques PIL/fonte réelle, boîtes de traits **étendues de la demi-épaisseur** — validé sur contrôles synthétiques positifs COVER/LINEX/FOOTER et un contrôle négatif propre) : **0 flag** sur les 8 pages. Audit titres-de-boîtes vs leurs bordures : **0 franchissement**. Audit texte-texte : 1 artefact de
...[truncated 2695 chars][motif de modèle — la phrase du constructeur est coupée dans le fichier d'origine]

## Relecture indépendante (gate SOP §8) — PASS, zéro problème (2026-10-21)

Relecteur indépendant, passe complète sur les artefacts livrés (SVG + cartes rendues), distincte des audits du constructeur ci-dessus. Note préalable : la section « Audits » du constructeur est tronquée dans le fichier (dernière phrase interrompue : « Audit texte-texte : 1 artefact de… »). Les vérifications ci-dessous couvrent et remplacent ce relevé manquant, y compris l'artefact texte-texte.

- **Registres** : les deux builds (noyau et FR) ré-exécutés en copie scratch — 150 exercices chacun ; n°/page/niveau/type identiques ; niveaux A2 44 · B1 75 · B2 31 ; par page 10/18/18/18/18/18/12/38. Diff de clés = exactement {#137, #138, #150} ; #139/#140 consignes en français, corps PT identiques ; toutes les autres clés à l'octet près. Les 150 notes FR relues contre les notes du noyau : fidèles intégralement.
- **Re-résolution complète** : les 150 exercices re-résolus un à un contre articles, tableaux et graphiques — zéro contradiction (dont 982+514+431+312 = 2.239 ; agrégé 3×2 Boca ; 900−250 = 650 ; barres du panneau P6 proportionnelles, géométrie des graphiques identique au noyau).
- **Gel du texte portugais** : diff multiset des chaînes visibles page par page — chaque différence est de l'appareil français ou du mobilier ; aucun texte portugais modifié. Éléments non-texte : seuls les hauteurs de boîtes de notes et les décalages de flux qui en découlent diffèrent (comptes d'éléments égaux des deux côtés, aucune suppression/ajout) ; images à l'octet près (payload P3 identique, 480 204 car. base64) ; lignes de crédit identiques, 4 photos placées.
- **Couche française** : CJK = 0 dans les 8 SVG ; aucun reste d'explication chinois/allemand/anglais ; parenthèses demi-chasse uniquement, espace avant chaque parenthèse de note (0 collée sur P8).
- **Mobilier** : badge exact (#a4553a), ligne d'édition exacte, pieds de page exacts ×8, « Page N sur 8 » ×8.
- **P7 phrases** : vérification programmatique — les 8 citations sont des extraits contigus mot à mot de leurs pages étiquetées (étiquettes 1,1,2,3,4,5,6,2), exactement 2 occurrences chacune dans l'édition.
- **Audit géométrique indépendant** (implémentation propre : ordre de peinture, métriques PIL/fonte réelle, boîtes de traits étendues de la demi-épaisseur ; validé sur 5 contrôles synthétiques positifs — COVER/LINEX/FOOTER/BOXFIT/EDGE tous déclenchés — et 1 négatif propre) : **0 flag** sur les 8 pages.
- **Vérifications pixel** (cartes 1950×2700) : note AS BUSCAS encre jusqu'à x=1814 (bord 1885) ; sous-titre AS BUSCAS 1867 ≤ 1885 ; titre CHIFFRES à 21 pt : 927 ≤ 961 ; titre ERROS : 1796 ≤ 1885 ; glose A PALAVRA : encre lignes 1801–1815, filet aux lignes 1843–1844 → ≥28 px d'air, non-défaut confirmé ; bas des flux de clés P8 : 2521 / 2552 / 2521 / 2475 (bande de pied à 2580) ; artefact texte-texte page 1 (wordmark 168 pt vs ligne d'édition) : encre réelle séparée par 2 lignes libres (301–302) → non-défaut.
- **Faits et calendrier 2026** : 15 affirmations jour/date revérifiées une à une (25 oct. = dimanche, 23 = vendredi, 21 = mercredi, 20 = mardi, 4/11/18 = dimanches, 31 = samedi, 1er nov. = dimanche, 2 = lundi, 8/15 = dimanches) — 15/15 correctes. Aucun pourcentage de sondage : uniquement des intérêts de recherche Google, légendés comme tels.
- **PDF** : web 3 698 531 o, sha256 dbbd0fb372f620ec7ca9e6f6b8da0f028bdce24f1396f5cd2a8e016ee51d09bb ; print 6 452 529 o, sha256 f4f12027f583c04d8c611cfd5ce927c7ae0082632385fc011eded7b326d8fbb9 ; 8 pages chacun.
- **Terme intermédiaire interdit** : 0 occurrence dans le papier, ce KIT et le code (vérifié par grep sur les deux formes, chinoise et anglaise).

Aucune correction n'a été nécessaire : rien n'a été re-rendu, le noyau n'a pas été touché. Verdict : **PASS — prêt pour l'insertion au dépôt** (diffusion Discord en pause sur instruction de l'utilisateur).
