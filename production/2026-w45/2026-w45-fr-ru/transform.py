# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 -> FR x RU edition transform. SINGLE SOURCE for
all explanation-layer edits (fix-round edits go here, never only into
content files). Every replacement is a whole line or a unique literal,
asserted. French target text is NEVER a replacement target. Registry
type names (internal metadata, never printed) are intentionally kept,
per the W43/W45 FR-family precedent; they are the only CJK allowed
to survive in code. Run from this directory:
  TRANSFORM_ROUND=1 ../../tools/venv/bin/python transform.py
It rewrites content12/34/56/7/8.py and bslib4.py in place. Re-running
round 1 after a first run fails loudly (old strings gone) -- restore
from the core copy first; never run twice on the same tree.
Fix rounds append section(N) blocks; run with TRANSFORM_ROUND=N.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROUND = int(os.environ.get("TRANSFORM_ROUND", "1"))
_SECTION = [1]
def section(n):
    _SECTION[0] = n

PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
assert len(PRINT_NOTES) == 97, len(PRINT_NOTES)

def rep(text, old, new, count=1):
    n = text.count(old)
    assert n == count, f"expected {count}x {old[:60]!r}, found {n}x"
    return text.replace(old, new)

def apply_file(fname, pairs):
    if _SECTION[0] != ROUND:
        print(f"skip section {_SECTION[0]} for {fname} (ROUND={ROUND})")
        return
    path = os.path.join(HERE, fname)
    text = open(path, encoding="utf-8").read()
    for old, new, *rest in pairs:
        text = rep(text, old, new, rest[0] if rest else 1)
    open(path, "w", encoding="utf-8").write(text)
    print(f"{fname}: {len(pairs)} replacements applied")

section(1)
apply_file("content12.py", [('os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg")', 'os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru/svg")')])
apply_file("content34.py", [('os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg")', 'os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru/svg")')])
apply_file("content56.py", [('os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg")', 'os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru/svg")')])
apply_file("content7.py", [('os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg")', 'os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru/svg")')])
apply_file("content8.py", [('os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg")', 'os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru/svg")')])
# ---------------- bslib4.py
apply_file("bslib4.py", [
    ('"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"', '"Le Lucerna · ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА ФРАНЦУЗСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"'),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"'),
    ('("译注｜" + s', '("Пояснение — " + s'),
])

# ---------------- content12.py
apply_file("content12.py", [
    ('# ================= P1 · 头版 (A2) =================', '# ================= P1 · первая полоса (A2) ================='),
    ('"VOL. 3 · 总第 3 期"', '"VOL. 3 · № 3"'),
    ('"HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语"', '"HEBDOMADAIRE EN FRANÇAIS · ФРАНЦУЗСКИЙ, КОТОРЫЙ ЧИТАЮТ ФРАНЦУЗЫ"'),
    ('"法 语 周 报 · VOL.3 · 决 赛 周 末"', '"ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · ФИНАЛЬНЫЙ УИК-ЭНД"'),
    ('"周一开学 · 全法同步复课"', '"ПОНЕДЕЛЬНИК · ВСЯ ФРАНЦИЯ ВОЗВРАЩАЕТСЯ В ШКОЛУ"'),
    ('"大师赛开赛 · 音乐节开幕 · 详见第 2 版"', '"Старт «Мастерса» · открытие фестиваля · см. стр. 2"'),
    ('"法语正文 · 简体中文讲解 — 给简体中文读者的版本"', '"ТЕКСТЫ НА ФРАНЦУЗСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ"'),
    ('"SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末"', '"SPORT · CULTURE · GASTRONOMIE · LA UNE · ФИНАЛЬНЫЙ УИК-ЭНД"'),
    ('f.gloss("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。")', 'f.gloss("se jouer решаться, разыгрываться · une finale финал · une demi-finale полуфинал · un quart de finale четвертьфинал · une nocturne ночное мероприятие · un frisson дрожь, азарт · la coquille Saint-Jacques гребешок.")'),
    ('f.box("LES DATES · 决赛周末日程"', 'f.box("LES DATES · ДАТЫ ФИНАЛЬНОГО УИК-ЭНДА"'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · ВАШ ХОД", 25)'),
    ('"周日 8 日举行决赛"', '"финалы в воскресенье 8-го"'),
    ('"周六 7 日晚是最后夜场"', '"последняя ночная программа в субботу 7-го"'),
    ('"波尔诺曼底卖扇贝"', '"в Пор-ан-Бессене продают гребешков"'),
    ('"周一 2 日全法复课"', '"вся Франция возвращается в школу в понедельник 2-го"'),
    ('"半决赛后才知道决赛选手"', '"финалисты станут известны только после полуфиналов"'),
    ('"三个决赛：网球、刺激、美味"', '"три финала: теннис, азарт, вкусы"'),
    ('"本周日程 · 11 月 2 日至 8 日"', '"НА ЭТОЙ НЕДЕЛЕ · 2–8 НОЯБРЯ"'),
    ('"周末决赛结果周六晚、周日揭晓。"', '"Результаты финального уик-энда станут известны в субботу вечером и в воскресенье."'),
    ('"DANS CE NUMÉRO · 本期目录"', '"DANS CE NUMÉRO · СОДЕРЖАНИЕ"'),
    ('"决出胜负；上演。本周末一切都将见分晓。"', '"решаться; разыгрываться. В этот уик-энд решится всё."'),
    ('"EN BREF · 快讯"', '"EN BREF · КОРОТКО"'),
    ('"QUIZ ÉCLAIR · 闪电问答"', '"QUIZ ÉCLAIR · БЫСТРЫЙ ОПРОС"'),
    ('"读头版，选出正确答案 · 答案见第 8 版"', '"Прочитайте первую полосу, выберите правильный ответ · ответы на стр. 8"'),
    ('"决赛在周日 8 日"', '"финалы в воскресенье 8-го"'),
    ('"扇贝节在滨海波尔"', '"фестиваль гребешка в Пор-ан-Бессене"'),
    ('"周一 2 日早上全区复课"', '"все зоны возвращаются в понедельник 2-го утром"'),
    ('"最后夜场周六 7 日"', '"последняя ночная программа в субботу 7-го"'),
    ('# ================= P2 · 生活 (A2) =================', '# ================= P2 · повседневная жизнь (A2) ================='),
    ('p.band("VIE QUOTIDIENNE · 生活", "Le Lucerna", "NIVEAU A2 · La rentrée · 开学复课")', 'p.band("VIE QUOTIDIENNE · ПОВСЕДНЕВНАЯ ЖИЗНЬ", "Le Lucerna", "NIVEAU A2 · La rentrée · ВОЗВРАЩЕНИЕ В ШКОЛУ")'),
    ('f.gloss("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。")', 'f.gloss("la rentrée возвращение в школу · reprendre начинать снова, возвращаться · un cartable портфель · un décalage сдвиг, разница во времени · en revanche напротив, зато · un rituel привычка, ритуал.")'),
    ('f.bridge("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。")', 'f.bridge("Пояснение — une valise чемодан · une ambiance атмосфера · le bilan итоги, обзор.")'),
    ('"说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。"', '"Расскажите о своём возвращении в школу: где вы были в понедельник утром и какую книгу прочитали на каникулах? Напишите два предложения по-французски и пришлите в редакцию."', 2),
    ('"ET VOUS ? · 说说你自己"', '"ET VOUS ? · РАССКАЖИТЕ О СЕБЕ"'),
    ('"DIRE LA DATE · 这样说日期"', '"DIRE LA DATE · КАК НАЗЫВАТЬ ДАТЫ"'),
    ('"lundi 2 novembre · 注意：1 日说 le premier，其余用基数词"', '"lundi 2 novembre · внимание: 1-е число — le premier, остальные — количественные числительные"'),
    ('("lundi 2 novembre", "11 月 2 日星期一 · la rentrée")', '("lundi 2 novembre", "понедельник, 2 ноября · la rentrée")'),
    ('("mardi 3 novembre", "11 月 3 日星期二 · votes à l\'Assemblée")', '("mardi 3 novembre", "вторник, 3 ноября · votes à l\'Assemblée")'),
    ('("mercredi 4 novembre", "11 月 4 日星期三 · sorties cinéma")', '("mercredi 4 novembre", "среда, 4 ноября · sorties cinéma")'),
    ('("samedi 7 novembre", "11 月 7 日星期六 · nocturne et demis")', '("samedi 7 novembre", "суббота, 7 ноября · nocturne et demis")'),
    ('("dimanche 8 novembre", "11 月 8 日星期日 · les finales")', '("dimanche 8 novembre", "воскресенье, 8 ноября · les finales")'),
    ('"EXERCICES · 第 2 版练习"', '"EXERCICES · УПРАЖНЕНИЯ СТР. 2"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Ответы на стр. 8 · упражнения разных уровней, ищите ответы по номерам"'),
    ('e.bridge("用法语补全日期（注意星期与数字）。")', 'e.bridge("Дополните даты по-французски (следите за днём недели и числом).")'),
    ('"复课在星期一"', '"возвращение в школу в понедельник"'),
    ('"11 月 1 日说 le premier"', '"1 ноября — le premier"'),
    ('"最后夜场在星期六"', '"последняя ночная программа в субботу"'),
    ('"决赛在星期日"', '"финалы в воскресенье"'),
    ('instr="填空"', 'instr="Вставьте"', 4),
    ('e.bridge("用 aller + 动词原形改写（最近将来时）。")', 'e.bridge("Перепишите с aller + инфинитив (ближайшее будущее, futur proche).")'),
    ('e.bridge("读第 2 版文章，选出正确答案。")', 'e.bridge("Прочитайте статью на стр. 2 и выберите правильный ответ.")'),
    ('"三区同一周一早上复课"', '"все три зоны возвращаются в одно и то же утро понедельника"'),
    ('"冬令时从 10 月 25 日开始"', '"зимнее время началось 25 октября"'),
    ('"11 月晚上天黑得早"', '"в ноябре вечером рано темнеет"'),
    ('["rentrée=开学 a", "reprendre=重新开始 b", "cartable=书包 c", "rituel=习惯 d"]', '["rentrée = возвращение в школу a", "reprendre = начинать снова b", "cartable = портфель c", "rituel = привычка d"]'),
    ('instr="把词和释义配对"', 'instr="Соедините"'),
    ('instr="改写"', 'instr="Перепишите"', 4),
])

# ---------------- content34.py
apply_file("content34.py", [
    ('# ================= P3 · 文化 (A2→B1) =================', '# ================= P3 · культура (A2→B1) ================='),
    ('p.band("CULTURE · 文化", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣")', 'p.band("CULTURE · КУЛЬТУРА", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · ХЭЛЛОУИН И ДЕНЬ ВСЕХ СВЯТЫХ")'),
    ('f.gloss("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。")', 'f.gloss("se déguiser переодеваться, наряжаться · un sort заклинание, проделка · une ambiance атмосфера · le souvenir воспоминание, память · confondre путать · discret сдержанный, тихий.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · ВАШ ХОД", 25)', 2),
    ('f.bridge("判断对错（Vrai / Faux）。")', 'f.bridge("Верно или неверно (Vrai / Faux).")'),
    ('"万圣节在 10 月 31 日星期六"', '"Хэллоуин был в субботу 31 октября"'),
    ('"诸圣节墓园摆满菊花"', '"в День всех святых кладбища полны хризантем"'),
    ('"菊花绝不能当礼物送人"', '"хризантемы никогда не дарят в подарок"'),
    ('"11 月 2 日是 jour des morts，不是诸圣节"', '"2 ноября — jour des morts, а не День всех святых"'),
    ('"文中：le rire d\'abord, le souvenir ensuite"', '"в тексте: le rire d\'abord, le souvenir ensuite"'),
    ('f.bridge("用 déguisement / tombe / citrouille / souvenir 填空。")', 'f.bridge("Вставьте déguisement / tombe / citrouille / souvenir.")'),
    ('"万圣节穿变装服装"', '"на Хэллоуин дети надевают костюмы"'),
    ('"花放在墓碑上"', '"цветы кладут на могилу"'),
    ('"南瓜是万圣节的象征"', '"тыква — символ Хэллоуина"'),
    ('"诸圣节是纪念之日"', '"День всех святых — день памяти"'),
    ('f.bridge("改写句子（用 ne...jamais / ne...plus / ne...pas）。")', 'f.bridge("Перепишите предложения (с ne...jamais / ne...plus / ne...pas).")'),
    ('"jamais + de（无冠词变化）"', '"jamais + de (без изменения артикля)"'),
    ('"ne...plus = 不再"', '"ne...plus = больше не"'),
    ('"n\'est pas = 不是"', '"n\'est pas = не"'),
    ('instr="改写"', 'instr="Перепишите"', 3),
    ('f.bridge("即学即练 · 公园万圣节小题。")', 'f.bridge("Ваш ход · короткие вопросы о парке на Хэллоуин.")'),
    ('"周六 7 日是最后夜场"', '"суббота 7-го — последняя ночная программа"'),
    ('"敏感儿童有免费驱怪徽章"', '"чувствительные дети получают бесплатный значок от монстров"'),
    ('"阿斯泰里克斯公园在 Plailly"', '"парк «Астерикс» находится в Плайи"'),
    ('"Peur sur le Parc 10 月 3 日至 11 月 8 日"', '"Peur sur le Parc проходит с 3 октября по 8 ноября"'),
    ('"恐惧等级用颜色区分"', '"шкала страха различается по цветам"'),
    ('"夜场从 19 点到凌晨 1 点"', '"ночная программа идёт с 19 часов до 1 часа ночи"'),
    ('"LES MOTS DES FÊTES · 节日词表"', '"LES MOTS DES FÊTES · СЛОВА ПРАЗДНИКОВ"'),
    ('"un saint — 圣人"', '"un saint — святой"'),
    ('"un cimetière — 墓园"', '"un cimetière — кладбище"'),
    ('"une tombe — 坟墓"', '"une tombe — могила"'),
    ('"un jour férié — 公共假日"', '"un jour férié — государственный праздник"'),
    ('"se souvenir — 纪念、想起"', '"se souvenir — помнить, вспоминать"'),
    ('"un déguisement — 变装服装"', '"un déguisement — костюм"'),
    ('"une citrouille — 南瓜"', '"une citrouille — тыква"'),
    ('"un bonbon — 糖果"', '"un bonbon — конфета"'),
    ('"un fantôme — 幽灵"', '"un fantôme — призрак"'),
    ('"un sort — 魔法、诅咒"', '"un sort — заклинание, проклятие"'),
    ('"10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。"', '"С 3 октября по 8 ноября: 12 ночных программ; последняя — 7 ноября; днём парк открыт с 10 до 19 часов."'),
    ('"DATES À RETENIR · 本周日历"', '"DATES À RETENIR · ДАТЫ НА ПАМЯТЬ"'),
    ('"注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。"', '"Внимание: ярмарка гребешка в Дьепе — 14–15 ноября, не на этой неделе."'),
    ('# ================= P4 · 体育 (B1) =================', '# ================= P4 · спорт (B1) ================='),
    ('p.band("SPORT · 体育", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")', 'p.band("SPORT · СПОРТ", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")'),
    ('f.gloss("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。")', 'f.gloss("un tournoi турнир, соревнование · sur dur на харде · en salle в зале · un tableau principal основная сетка · le tenant du titre действующий чемпион · basculer переломиться, качнуться · les tribunes трибуны.")'),
    ('f.bridge("读第 4 版文章，选出正确答案。")', 'f.bridge("Прочитайте статью на стр. 4 и выберите правильный ответ.")'),
    ('"决赛在周日 8 日"', '"финалы в воскресенье 8-го"'),
    ('"大师赛在室内硬地球场举行"', '"«Мастерс» проходит в зале, на харде"'),
    ('"2025 年卫冕冠军是辛纳"', '"действующий чемпион 2025 года — Синнер"'),
    ('"法甲第十轮大场面：朗斯–马赛"', '"главный матч выходных в Лиге 1: «Ланс» — «Марсель»"'),
    ('"周日 8 日还有轮椅单打决赛（中午）"', '"в воскресенье 8-го также финал на колясках (в полдень)"'),
    ('f.bridge("把网球词和释义配对。")', 'f.bridge("Соедините теннисные слова со значениями.")'),
    ('["tournoi=赛事 a", "raquette=球拍 b", "tribunes=看台 c", "tenant=卫冕者 d"]', '["tournoi = турнир a", "raquette = ракетка b", "tribunes = трибуны c", "tenant = действующий чемпион d"]'),
    ('instr="配对"', 'instr="Соедините"'),
    ('f.bridge("用比较级完成句子（plus / moins）。")', 'f.bridge("Дополните сравнительной степенью (plus / moins).")'),
    ('"室内球速更快"', '"в зале мяч летит быстрее"'),
    ('"大师赛是仅次于大满贯的级别"', '"«Мастерс-1000» — уровень чуть ниже «Большого шлема»"'),
    ('"室内赛季比室外短"', '"зальный сезон короче летнего"'),
    ('f.bridge("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。")', 'f.bridge("Пояснение — un choc главный матч · recevoir принимать, встречать · familier знакомый.")'),
    ('"« Allez ! » — 加油！ · « Quelle action ! » — 好球！"', '"« Allez ! » — Давай! · « Quelle action ! » — Вот это игра!"'),
    ('"« Il marque ! » — 他得分了！ · « C\'est gagné ! » — 赢了！"', '"« Il marque ! » — Он забивает! · « C\'est gagné ! » — Победа!"'),
    ('"« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！"', '"« Quel point ! » — Вот это розыгрыш! (теннис) · « Balle de match ! » — Матчбол!"'),
    ('"LES MOTS DU TENNIS · 网球词表"', '"LES MOTS DU TENNIS · ТЕННИСНЫЕ СЛОВА"'),
    ('"le tennis — 网球"', '"le tennis — теннис"'),
    ('"une balle — 球"', '"une balle — мяч"'),
    ('"un set — 一盘"', '"un set — сет"'),
    ('"un match — 比赛"', '"un match — матч"'),
    ('"un point — 一分"', '"un point — очко"'),
    ('"la finale — 决赛"', '"la finale — финал"'),
    ('"un adversaire — 对手"', '"un adversaire — соперник"'),
    ('"un titre — 冠军头衔"', '"un titre — титул"'),
    ('"À SUIVRE · 拭目以待"', '"À SUIVRE · ПРОДОЛЖЕНИЕ СЛЕДУЕТ"'),
    ('mf.head("MICRO-DRILLS · 即学即练", 24)', 'mf.head("MICRO-DRILLS · БЫСТРАЯ ПРАКТИКА", 24)'),
    ('mf.bridge("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。")', 'mf.bridge("Вставьте finale / quarts / demi-finales / tableau / fauteuil / choc.")'),
    ('"四分之一决赛在周五"', '"четвертьфиналы в пятницу"'),
    ('"半决赛在周六"', '"полуфиналы в субботу"'),
    ('"单打决赛在周日"', '"финал одиночного разряда в воскресенье"'),
    ('"正赛签表从周一开始"', '"основная сетка начинается в понедельник"'),
    ('"轮椅赛事周五至周日"', '"турнир на колясках — с пятницы по воскресенье"'),
    ('"朗斯–马赛是周末焦点战"', '"«Ланс» — «Марсель» — главный матч выходных"'),
    ('p.text(ix + 22, db4 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, db4 + 40, "LE DÉBAT · ДИСКУССИЯ", 23, "sans", True, OLIVE)'),
    ('"事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。"', '"Не знать финалистов заранее — интереснее или досаднее? Напишите два предложения «за» и два «против»."'),
])

# ---------------- content56.py
apply_file("content56.py", [
    ('# ================= P5 · 青年 (B1) =================', '# ================= P5 · молодёжь (B1) ================='),
    ('p.band("JEUNESSE & MUSIQUE · 青年", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 音乐节")', 'p.band("JEUNESSE & MUSIQUE · МОЛОДЁЖЬ", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · МУЗЫКАЛЬНЫЙ ФЕСТИВАЛЬ")'),
    ('f.gloss("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。")', 'f.gloss("un lieu место, площадка · une affiche афиша · les paroles слова песни · donner le ton задавать тон · se promener гулять, перемещаться · pile точно, как раз.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · ВАШ ХОД", 25)'),
    ('f.bridge("读第 5 版文章，选出正确答案。")', 'f.bridge("Прочитайте статью на стр. 5 и выберите правильный ответ.")'),
    ('"音乐节 11 月 2–8 日，整整一周"', '"фестиваль идёт 2–8 ноября, целую неделю"'),
    ('"15 届音乐节"', '"15-й фестиваль"'),
    ('"Avant-Garde 在巴士底各场地，周四至周六"', '"Avant-Garde — на площадках Бастилии, с четверга по субботу"'),
    ('"俱乐部之夜在周五、周六"', '"клубные ночи — в пятницу и субботу"'),
    ('"开幕夜：Headache、Iceage、DIIV"', '"вечер открытия: Headache, Iceage, DIIV"'),
    ('f.bridge("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。")', 'f.bridge("Вставьте lieux / paroles / affiche / ambiance / danse / découvre.")'),
    ('"10 个场地"', '"десять площадок"'),
    ('"歌词也是法语学习材料"', '"тексты песен тоже помогают учить французский"'),
    ('"海报上写着演出信息"', '"на афише — состав участников"'),
    ('"每晚气氛各不相同"', '"каждый вечер — своя атмосфера"'),
    ('"音乐节上人们跳舞"', '"на фестивале танцуют"'),
    ('"发现不认识的乐队"', '"открывать для себя незнакомые группы"'),
    ('f.bridge("把音乐词和释义配对。")', 'f.bridge("Соедините музыкальные слова со значениями.")'),
    ('["concert=音乐会 a", "scène=舞台 b", "groupe=乐队 c", "billet=门票 d"]', '["concert = концерт a", "scène = сцена b", "groupe = группа c", "billet = билет d"]'),
    ('instr="配对"', 'instr="Соедините"', 2),
    ('f.bridge("补全对话（音乐节门口）。")', 'f.bridge("Дополните диалог (у входа на фестиваль).")'),
    ('"今晚演出的乐队"', '"группа, выступающая сегодня вечером"'),
    ('"买两张票"', '"покупка двух билетов"'),
    ('"MOTS DE LA MUSIQUE · 音乐词表"', '"MOTS DE LA MUSIQUE · МУЗЫКАЛЬНЫЕ СЛОВА"'),
    ('"un festival — 音乐节"', '"un festival — фестиваль"'),
    ('"un concert — 音乐会"', '"un concert — концерт"'),
    ('"une chanson — 歌曲"', '"une chanson — песня"'),
    ('"un chanteur — 歌手"', '"un chanteur — певец"'),
    ('"danser — 跳舞"', '"danser — танцевать"'),
    ('"écouter — 聆听"', '"écouter — слушать"'),
    ('"une salle — 演出厅"', '"une salle — зал"'),
    ('"le public — 观众"', '"le public — публика"'),
    ('"PARIS CREATOR WEEK · 创作者周"', '"PARIS CREATOR WEEK · НЕДЕЛЯ КРЕАТОРОВ"'),
    ('"11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。"', '"4–5 ноября в Ла-Виллет: Неделя креаторов — авторы онлайн встречаются со своей публикой вживую."'),
    ('p.text(ix + 22, ty5 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, ty5 + 40, "LE DÉBAT · ДИСКУССИЯ", 23, "sans", True, OLIVE)'),
    ('"十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？"', '"Фестиваль на десяти площадках — лучше, чем один большой зал? Какую музыку вы слушаете, чтобы учить французский?"'),
    ('# ================= P6 · 时事 (B2) =================', '# ================= P6 · актуальные события (B2) ================='),
    ('p.band("POLITIQUE & CHIFFRES · 时事", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 预算周")', 'p.band("POLITIQUE & CHIFFRES · ПОЛИТИКА И ЦИФРЫ", "Le Lucerna", "NIVEAU B2 · Budget 2027 · БЮДЖЕТНАЯ НЕДЕЛЯ")'),
    ('f.gloss("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l\'unanimité 一致通过/否决 · un amendement 修正案。")', 'f.gloss("un budget бюджет · une mission (бюджетная) статья · un député депутат Национального собрания · rejeter отклонять · à l\'unanimité единогласно · un amendement поправка.")'),
    ('"LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）"', '"LE CALENDRIER PRÉVU · ПЛАН ГОЛОСОВАНИЙ (БЕЗ РЕЗУЛЬТАТОВ)"'),
    ('"本页日程为计划安排，结果尚未产生，下期跟进。"', '"Это расписание — план; результатов пока нет, продолжение — в следующем номере."'),
    ('e6.head("LIRE LE CALENDRIER · 读日程", 25)', 'e6.head("LIRE LE CALENDRIER · ПЛАН", 25)'),
    ('e6.bridge("读上图日程，选出正确答案。")', 'e6.bridge("Прочитайте расписание выше и выберите правильный ответ.")'),
    ('"周二 3 日：文化与媒体"', '"вторник 3-го: культура и СМИ"'),
    ('"周三 4 日：农业"', '"среда 4-го: сельское хозяйство"'),
    ('"周四 5 日：国土协调与科研"', '"четверг 5-го: территориальное развитие и наука"'),
    ('"周五 6 日：公共财政与经济"', '"пятница 6-го: государственные финансы и экономика"'),
    ('"10 月 23 日社保预算收入被 115–1 否决"', '"23 октября доходы бюджета соцобеспечения отклонены 115–1"'),
    ('"参议院从 11 月 9 日起审议"', '"Сенат рассматривает текст с 9 ноября"'),
    ('e6.head("LES MOTS · 词汇", 25)', 'e6.head("LES MOTS · СЛОВА", 25)'),
    ('["député=议员 a", "rejeter=否决 b", "vote=投票 c", "amendement=修正案 d"]', '["député = депутат a", "rejeter = отклонять b", "vote = голосование c", "amendement = поправка d"]'),
    ('"« Le texte part au Sénat. » — 法案送交参议院。"', '"« Le texte part au Sénat. » — Законопроект уходит в Сенат."'),
    ('"« Ce calendrier peut encore bouger. » — 日程仍可能变动。"', '"« Ce calendrier peut encore bouger. » — Расписание ещё может измениться."'),
    ('"« Les résultats ne sont pas connus. » — 结果尚未揭晓。"', '"« Les résultats ne sont pas connus. » — Результаты пока неизвестны."'),
    ('g.bridge("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。")', 'g.bridge("Пояснение — prévu запланированный · réaliser осуществлять · distinguer различать.")'),
    ('g2.bridge("用比较级完成句子。")', 'g2.bridge("Дополните сравнительной степенью.")'),
    ('"预算辩论比一场音乐会长"', '"дебаты о бюджете длиннее концерта"'),
    ('"预算比时间表复杂"', '"бюджет сложнее расписания"'),
    ('"文化预算与农业预算同样重要"', '"бюджет культуры так же важен, как бюджет сельского хозяйства"'),
    ('g2.head("MICRO-DRILLS · 即学即练", 25)', 'g2.head("MICRO-DRILLS · ПРАКТИКА", 25)'),
    ('g2.bridge("用 examine / ont rejeté / part / peut / connus 填空。")', 'g2.bridge("Вставьте examine / ont rejeté / part / peut / connus.")'),
    ('"国民议会审议预算"', '"Национальное собрание рассматривает бюджет"'),
    ('"议员们否决收入部分"', '"депутаты отклонили доходную часть"'),
    ('"法案送交参议院"', '"законопроект уходит в Сенат"'),
    ('"日程仍可能变动"', '"расписание ещё может измениться"'),
    ('"结果尚未揭晓"', '"результаты пока неизвестны"'),
    ('g2.head("LE DÉBAT · 讨论", 25)', 'g2.head("LE DÉBAT · ДИСКУССИЯ", 25)'),
    ('g2.bridge("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。")', 'g2.bridge("Дискуссия: стоит ли объявлять расписание до результатов? Различайте prévu (запланировано) и décidé (решено).")'),
])

# ---------------- content7.py
apply_file("content7.py", [
    ('p.band("LANGUE EN MAIN · 精讲", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 本周金句")', 'p.band("LANGUE EN MAIN · ЯЗЫК В РУКАХ", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · ФРАЗЫ НЕДЕЛИ")'),
    ('cA.head("NIVEAU A2 · 基础", 27)', 'cA.head("NIVEAU A2 · БАЗОВЫЙ", 27)'),
    ('cB.head("NIVEAU B1 · 进阶", 27)', 'cB.head("NIVEAU B1 · СРЕДНИЙ", 27)'),
    ('cC.head("NIVEAU B2 · 挑战", 27)', 'cC.head("NIVEAU B2 · УРОВЕНЬ-ВЫЗОВ", 27)'),
    ('cD.head("BOÎTE À OUTILS · 工具箱", 27)', 'cD.head("BOÎTE À OUTILS · В КАРМАНЕ", 27)'),
    ('cD.bridge("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。")', 'cD.bridge("В кармане: три фразы номера, по одной на уровень; все фразы недели — из статей номера, перечитайте статью — и фраза запомнится.")'),
    ('p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）", 27, "sans", True, OLIVE)', 'p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · ФРАЗЫ НЕДЕЛИ", 27, "sans", True, OLIVE)'),
    ('p.text(RIGHT, py + 26, "每句一个语法点 + 一道小题 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")', 'p.text(RIGHT, py + 26, "К каждой фразе — грамматика и мини-задание · ответы на стр. 8", 20, "sans", False, GREY, anchor="end")'),
    ('"语法点｜reprendre：复课、重新开始（pause 后）。"', '"Грамматика · reprendre: возвращаться, начинать снова (после паузы)."'),
    ('"语法点｜ne...pas encore：尚未、还不。"', '"Грамматика · ne...pas encore: ещё не."'),
    ('"pas encore 尚未"', '"pas encore = ещё не"'),
    ('"语法点｜passé composé 代动词：se + être + 过去分词。"', '"Грамматика · passé composé с возвратными глаголами: se + être + причастие."'),
    ('"语法点｜comparatif：plus + 形容词，ou 对举。"', '"Грамматика · comparatif: plus + прилагательное, два противоположных члена через ou."'),
    ('"plus + 形容词"', '"plus + прилагательное"'),
    ('"语法点｜se promener：代动词，漫步、穿梭。"', '"Грамматика · se promener: возвратный глагол, гулять."'),
    ('"语法点｜pouvoir + 动词原形：可能、可以。"', '"Грамматика · pouvoir + инфинитив: мочь."'),
    ('"语法点｜se jouer：决出胜负、上演（代动词）。"', '"Грамматика · se jouer: решаться, разыгрываться (возвратный глагол)."'),
    ('"语法点｜rencontrer：与观众见面；y 代指地点。"', '"Грамматика · rencontrer: встречаться со своей публикой; y заменяет место."'),
    ('cf.head("CLINIQUE DES ERREURS · 易错诊所", 25)', 'cf.head("CLINIQUE DES ERREURS · СТОП!", 25)'),
    ('cf.bridge("每句有一处错误：找出来并改正。")', 'cf.bridge("Клиника ошибок · В каждом предложении одна ошибка: найдите её и исправьте.")'),
    ('"jamais + de：否定句中 des 变 de"', '"jamais + de: в отрицании des становится de"'),
    ('"主谓一致：créateurs 复数 → rencontrent，不是 rencontre"', '"Согласование: créateurs во множественном числе → rencontrent, а не rencontre"'),
    ('"虚拟式：il examine，不加 s"', '"Сослагательное наклонение: il examine, без -s"'),
    ('"事实：决赛在 8 日，不是 7 日"', '"Факт: финал 8-го, а не 7-го"'),
    ('instr="改错"', 'instr="Исправьте"', 4),
    ('p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 读者园地", 24, "sans", True, OLIVE)', 'p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · ПОЧТА ЧИТАТЕЛЕЙ", 24, "sans", True, OLIVE)'),
    ('p.para(rx + 24, by7 + 196, "小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。", 20, "sans", False, GREY, rw - 48, 1.4)', 'p.para(rx + 24, by7 + 196, "Комментарий редакции: passé composé уверенный, точка с запятой хорошо соединяет два дня. Присылайте письма и лучшие сочинения со стр. 8 — для VOL.4!", 20, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.para(rx + 24, by7 + 336, "编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。", 19.5, "sans", False, GREY, rw - 48, 1.4)', 'p.para(rx + 24, by7 + 336, "Примечание редакции: настоящих писем и лучших сочинений VOL.2 со стр. 8 не поступило (номер W44 не вышел); здесь — помеченный пример редакции, а настоящие работы будут разобраны в VOL.4.", 19.5, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 下周预告", 24, "sans", True, "#f3edda")', 'p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 НА СЛЕДУЮЩЕЙ НЕДЕЛЕ", 24, "sans", True, "#f3edda")'),
    ('p.para(rx + 24, ty7 + 196, "下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！", 20, "sans", False, "#b3a06a", rw - 48, 1.4)', 'p.para(rx + 24, ty7 + 196, "На следующей неделе: Сенат рассматривает бюджет соцобеспечения, 11 ноября — День перемирия, ярмарка в Дьепе 14–15 ноября; и, наконец, ваши письма!", 20, "sans", False, "#b3a06a", rw - 48, 1.4)'),
])

# ---------------- content8.py
apply_file("content8.py", [
    ('p.band("EXERCICES & RÉPONSES · 练习与答案", "Le Lucerna", "综合评估 ÉVALUATION · 答案在本版下方")', 'p.band("EXERCICES & RÉPONSES · УПРАЖНЕНИЯ И ОТВЕТЫ", "Le Lucerna", "ТЕСТ · ОТВЕТЫ ВНИЗУ ЭТОЙ СТРАНИЦЫ")'),
    ('"11 月 8 日 2026 是星期日"', '"8 ноября 2026 года — воскресенье"'),
    ('"去南泰尔看决赛"', '"поехать в Нантер на финалы"'),
    ('"决赛选手周六晚才揭晓"', '"финалисты станут известны только в субботу вечером"'),
    ('"品尝语境（un régal）→ goûté"', '"контекст дегустации (un régal) → goûté"'),
    ('"se promener 漫步"', '"se promener = гулять"'),
    ('"avoir + 过去分词 goûté（不配合）"', '"avoir + причастие прошедшего времени goûté (без согласования)"'),
    ('"les finales 主语复数 → ont lieu"', '"les finales во множественном числе → ont lieu"'),
    ('"elle écrit 她写"', '"elle écrit = она пишет"'),
    ('bf.head("A · TEXTE À TROUS · 完形填空", 24)', 'bf.head("A · TEXTE À TROUS · ПРОПУСКИ", 24)'),
    ('bf.bridge("选项：")', 'bf.bridge("Варианты:")'),
    ('bf.head("B · CHOIX MULTIPLE · 单选", 24)', 'bf.head("B · CHOIX MULTIPLE · ВЫБОР", 24)'),
    ('"7 nov. = samedi（最后夜场）"', '"7 nov. = samedi (последняя ночная программа)"'),
    ('"nous → allons"', '"nous → allons"'),
    ('"s\'intéresser aux（à+les）"', '"s\'intéresser aux (à + les)"'),
    ('"si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j\' 是 je 在元音前的省音"', '"si + imparfait → conditionnel présent; j\' — je перед гласной"'),
    ('"主语 ce programme 三单 → semble"', '"подлежащее ce programme в 3-м лице ед. числа → semble"'),
    ('"将来时 aura lieu（决赛在周日）"', '"будущее время aura lieu (финал в воскресенье)"'),
    ('"三区同日复课"', '"все три зоны возвращаются в один день"'),
    ('"扇贝节在 11 月 7–8 日"', '"фестиваль гребешка 7–8 ноября"'),
    ('bf.head("C · LECTURE · 阅读理解", 24)', 'bf.head("C · LECTURE · ЧТЕНИЕ", 24)'),
    ('"夜场 19 点至凌晨 1 点"', '"ночная программа с 19 часов до 1 часа ночи"'),
    ('"小徽章给小 Léo 驱怪"', '"маленький значок для маленького Лео, от монстров"'),
    ('"周日先看决赛再吃扇贝"', '"в воскресенье сначала финалы, потом гребешки"'),
    ('"周日晚上早睡因为周一上学"', '"в воскресенье вечером рано спать, потому что в понедельник в школу"'),
    ('"周一是上学日（复课后正常周一）"', '"понедельник — учебный день (обычный понедельник после возвращения)"'),
    ('bf.head("D · PHRASES · 完成句子与转换", 24)', 'bf.head("D · PHRASES · ПРЕДЛОЖЕНИЯ", 24)'),
    ('"aller + 原形（futur proche）"', '"aller + инфинитив (futur proche)"'),
    ('"si + 半过去时 venais"', '"si + имперфект venais"'),
    ('"passé composé : a + 过去分词"', '"passé composé: a + причастие прошедшего времени"'),
    ('"selon moi = 在我看来"', '"selon moi = по-моему"'),
    ('"il est prévu que + 虚拟式"', '"il est prévu que + сослагательное наклонение"'),
    ('bf.head("E · TRADUCTION · 翻译", 24)', 'bf.head("E · TRADUCTION · ПЕРЕВОД", 24)'),
    ('"读一份日程，本身就是在了解法国。"', '"Читать программу — уже значит понимать Францию."'),
    ('"lire un programme = 读日程"', '"lire un programme = читать программу"'),
    ('"Traduisez : « Lire un programme, c\'est déjà comprendre la France. »"', '"Переведите на русский: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"比较级 plus vite + court"', '"сравнительная степень plus vite + court"'),
    ('"Traduisez : 他跑得比他哥哥更快。"', '"Переведите: Он бежит быстрее своего брата."'),
    ('"être en vacances + depuis"', '"être en vacances + depuis"'),
    ('"Traduisez : 学生们自 10 月 17 日起就在放假。"', '"Переведите: Ученики на каникулах с 17 октября."'),
    ('"futur proche + préparer"', '"futur proche + préparer"'),
    ('"Traduisez : 今晚，我们要准备书包。"', '"Переведите: Сегодня вечером мы будем собирать портфели."'),
    ('"ne...pas encore = 尚未"', '"ne...pas encore = пока не"'),
    ('"Traduisez : 人们尚不知道决赛选手是谁。"', '"Переведите: Пока неизвестно, кто финалисты."'),
    ('bf.head("F · LES MOTS · 词汇配对", 24)', 'bf.head("F · LES MOTS · СЛОВА", 24)'),
    ('["tournoi=赛事 a", "nocturne=夜场 b", "budget=预算 c", "coquille=扇贝 d", "festival=音乐节 e"]', '["tournoi = турнир a", "nocturne = ночная программа b", "budget = бюджет c", "coquille = гребешок d", "festival = фестиваль e"]'),
    ('instr="配对"', 'instr="Соедините"'),
    ('"11 月 7 日是星期六"', '"7 ноября — суббота"'),
    ('"在市场买扇贝"', '"покупать гребешков на рынке"'),
    ('"goûter 品尝（原形）"', '"goûter = пробовать (инфинитив)"'),
    ('"à la portaise 是一种做法"', '"à la portaise — способ приготовления"'),
    ('"Bon week-end ! 周末愉快"', '"Bon week-end ! = Хороших выходных!"'),
    ('bf.head("G · DIALOGUE · 对话补全", 24)', 'bf.head("G · DIALOGUE · ДИАЛОГ", 24)'),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")', 'reg_ex("B1", "写作", "Открытый вопрос — баллы в рамке для письма, а образец — в рамке MODÈLE на этой странице", "оценка по баллам")'),
    ('p.text(wx, wy + 26, "H · ÉCRITURE · 写作", 25, "sans", True, OLIVE)', 'p.text(wx, wy + 26, "H · ÉCRITURE · ПИСЬМО", 25, "sans", True, OLIVE)'),
    ('p.para(wx, wy + 190, "用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。", 20, "sans", False, GREY, ww, 1.4)', 'p.para(wx, wy + 190, "Напишите по-французски 80–100 слов: «Мои выходные 7–8 ноября». Расскажите об одном матче, одном празднике, одном блюде.", 20, "sans", False, GREY, ww, 1.4)'),
    ('p.text(mx2 + 22, wy + 38, "MODÈLE · 范文", 23, "sans", True, OLIVE)', 'p.text(mx2 + 22, wy + 38, "MODÈLE · ОБРАЗЕЦ", 23, "sans", True, OLIVE)'),
    ('p.text(MX, ky + 26, "RÉPONSES · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)', 'p.text(MX, ky + 26, "RÉPONSES · ВСЕ ОТВЕТЫ С ПРИМЕЧАНИЯМИ (СТРАНИЦЫ 1–8)", 26, "sans", True, OLIVE)'),
])

# ---------------- content8: P8 keys block
OLD_KEYS = 'for pg, grp in groupby(REG, key=lambda e: e["page"]):\n    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)\n    parts = []\n    for e in grp:\n        s = f"{e[\'n\']}. {e[\'key\']}"\n        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):\n            s += f"（{e[\'note\']}）"\n        parts.append(s)'
NEW_KEYS = '# Notes printed on this page = exactly the set printed in the core\n# edition (tools/p8.py extract on the shipped core P8: noted 97/150).\n# Reproduced as an explicit set so the Russian edition shows the same\n# notes for the same exercises, even though Russian notes are longer\n# than the core rule (page 8 always, or note <= 10 chars, or type in\n# the two special types). Bracket form: half-width " (note)", per the\n# shipped W43 FR x RU build code.\nPRINT_NOTES = {1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150}\nfor pg, grp in groupby(REG, key=lambda e: e["page"]):\n    kf.para(f"— СТРАНИЦА {pg} —", 17, "sans", True, OLIVE, 1.28, 3)\n    parts = []\n    for e in grp:\n        s = f"{e[\'n\']}. {e[\'key\']}"\n        if e["note"] and e["n"] in PRINT_NOTES:\n            s += f" ({e[\'note\']})"\n        parts.append(s)'
apply_file("content8.py", [(OLD_KEYS, NEW_KEYS)])
print("transform round 1 done")

section(2)
# Round 2 (measured from round-1 render):
# - P1 gloss 7->5 lines (else the LES DATES box is pushed out of col 0 and
#   the headline flow overflows by 127px); gloss items stay 7 (split on .).
# - P2 date block dy 1570->1690: the Russian ET VOUS box ends 1654.6 and the
#   old gold rule at 1558 cut through it; +120 keeps the core 13px clearance
#   pattern (examples ink to hline) and P2-ex ends 2485 < 2562.
# - P4-micro head too wide (476 > 434) -> short form.
# - P7 clinic bridge 3->2 lines (clinic ended 2270 > bottom 2268).
# - P8 battery stems #135-139 back to the core line counts (battery 1526 ->
#   1410). #138 is bare "Этим вечером будем собирать портфели." (no
#   prefix): every prefixed form wraps to 2 lines, and the bare form keeps
#   both "this evening" (= ce soir) and "budem + infinitive" (futur proche).
# - P8 keys notes shortened (notes print only on P8; hints stay accurate);
#   target: keys flow back inside 2545 (round 1: 2746).
apply_file("content12.py", [
    ('f.gloss("se jouer решаться, разыгрываться · une finale финал · une demi-finale полуфинал · un quart de finale четвертьфинал · une nocturne ночное мероприятие · un frisson дрожь, азарт · la coquille Saint-Jacques гребешок.")',
     'f.gloss("se jouer решаться · une finale финал · une demi-finale ½ финала · un quart de finale ¼ финала · une nocturne шоу · un frisson азарт · coquille Saint-Jacques гребешок.")'),
    ('dy = 1570', 'dy = 1690'),
    ('"вся Франция возвращается в школу в понедельник 2-го"', '"вся Франция возвращается 2-го"'),
    ('"последняя ночная программа в субботу 7-го"', '"последняя программа в субботу 7-го"', 2),
    ('"все три зоны возвращаются в одно и то же утро понедельника"', '"все три зоны — в одно утро понедельника"'),
    ('"последняя ночная программа в субботу"', '"последняя программа в субботу"'),
    ('"в Пор-ан-Бессене продают гребешков"', '"в Пор-ан-Бессене — гребешки"'),
    ('"фестиваль гребешка в Пор-ан-Бессене"', '"фестиваль в Пор-ан-Бессене"'),
    ('"в ноябре вечером рано темнеет"', '"в ноябре рано темнеет"'),
])
apply_file("content34.py", [
    ('mf.head("MICRO-DRILLS · БЫСТРАЯ ПРАКТИКА", 24)', 'mf.head("MICRO-DRILLS · ПРАКТИКА", 24)'),
    ('"в День всех святых кладбища полны хризантем"', '"кладбища полны хризантем"'),
    ('"на Хэллоуин дети надевают костюмы"', '"дети надевают костюмы"'),
    ('"хризантемы никогда не дарят в подарок"', '"хризантемы не дарят в подарок"'),
    ('"шкала страха различается по цветам"', '"шкала страха — по цветам"'),
    ('"турнир на колясках — с пятницы по воскресенье"', '"турнир на колясках: пт–вс"'),
    ('"основная сетка начинается в понедельник"', '"основная сетка с понедельника"'),
    ('"финал одиночного разряда в воскресенье"', '"финал одиночек в воскресенье"'),
])
apply_file("content56.py", [
    ('"тексты песен тоже помогают учить французский"', '"тексты песен помогают учить французский"'),
    ('"открывать для себя незнакомые группы"', '"открывать незнакомые группы"'),
    ('"группа, выступающая сегодня вечером"', '"группа сегодня вечером"'),
    ('"на афише — состав участников"', '"афиша: состав участников"'),
    ('"вторник 3-го: культура и СМИ"', '"вторник: культура и СМИ"'),
    ('"среда 4-го: сельское хозяйство"', '"среда: сельское хозяйство"'),
    ('"четверг 5-го: территориальное развитие и наука"', '"четверг 5-го: территории и наука"'),
    ('"пятница 6-го: государственные финансы и экономика"', '"пятница 6-го: финансы и экономика"'),
    ('"23 октября доходы бюджета соцобеспечения отклонены 115–1"', '"23 октября доходы отклонены 115–1"'),
    ('"Сенат рассматривает текст с 9 ноября"', '"Сенат: текст с 9 ноября"'),
    ('"Национальное собрание рассматривает бюджет"', '"Собрание рассматривает бюджет"'),
])
apply_file("content7.py", [
    ('cf.bridge("Клиника ошибок · В каждом предложении одна ошибка: найдите её и исправьте.")',
     'cf.bridge("Клиника ошибок · Найдите и исправьте ошибку в каждом предложении.")'),
    ('"Согласование: créateurs во множественном числе → rencontrent, а не rencontre"',
     '"créateurs (мн. число) → rencontrent, не rencontre"'),
    ('"Сослагательное наклонение: il examine, без -s"', '"сослагательное: il examine, без -s"'),
])
apply_file("content8.py", [
    ('"Переведите на русский: « Lire un programme, c\'est déjà comprendre la France. »"',
     '"На русский: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"Переведите: Он бежит быстрее своего брата."', '"Перевод: Он бежит быстрее своего брата."'),
    ('"Переведите: Ученики на каникулах с 17 октября."', '"Перевод: Ученики на каникулах с 17 окт."'),
    ('"Переведите: Сегодня вечером мы будем собирать портфели."', '"Этим вечером будем собирать портфели."'),
    ('"Переведите: Пока неизвестно, кто финалисты."', '"Перевод: Финалисты пока неизвестны."'),
    ('"понедельник — учебный день (обычный понедельник после возвращения)"', '"понедельник — учебный день"'),
    ('"в воскресенье вечером рано спать, потому что в понедельник в школу"', '"рано спать: в понедельник в школу"'),
    ('"avoir + причастие прошедшего времени goûté (без согласования)"', '"avoir + причастие goûté (без согласования)"'),
    ('"si + imparfait → conditionnel présent; j\' — je перед гласной"', '"si + imparfait → conditionnel; j\' = je"'),
    ('"подлежащее ce programme в 3-м лице ед. числа → semble"', '"ce programme — 3-е лицо ед. числа → semble"'),
    ('"финалисты станут известны только в субботу вечером"', '"финалисты — только в субботу вечером"'),
    ('"маленький значок для маленького Лео, от монстров"', '"значок для маленького Лео, от монстров"'),
    ('"passé composé: a + причастие прошедшего времени"', '"passé composé: a + причастие"'),
    ('"будущее время aura lieu (финал в воскресенье)"', '"будущее aura lieu (финал в воскресенье)"'),
    ('"les finales во множественном числе → ont lieu"', '"les finales — мн. число → ont lieu"'),
    ('"il est prévu que + сослагательное наклонение"', '"il est prévu que + сослагательное"'),
    ('"в воскресенье сначала финалы, потом гребешки"', '"сначала финалы, потом гребешки"'),
    ('"7 nov. = samedi (последняя ночная программа)"', '"7 nov. = samedi (последняя программа)"'),
    ('"ночная программа с 19 часов до 1 часа ночи"', '"ночная программа 19:00–1:00"'),
    ('"все три зоны возвращаются в один день"', '"все три зоны — в один день"'),
    ('"контекст дегустации (un régal) → goûté"', '"дегустация (un régal) → goûté"'),
    ('"сравнительная степень plus vite + court"', '"сравнение plus vite + court"'),
    ('"aller + инфинитив (futur proche)"', '"aller + инфинитив"'),
    ('"8 ноября 2026 года — воскресенье"', '"8 ноября 2026 — воскресенье"'),
    ('"поехать в Нантер на финалы"', '"в Нантер на финалы"'),
    ('"фестиваль гребешка 7–8 ноября"', '"фестиваль 7–8 ноября"'),
    ('"покупать гребешков на рынке"', '"гребешки на рынке"'),
    ('"goûter = пробовать (инфинитив)"', '"goûter = пробовать"'),
    ('"à la portaise — способ приготовления"', '"à la portaise — приготовление"'),
])
print("transform round 2 done")

section(3)
# Round 3: round 2's dy +120 broke P2-ex (a top shift of D eats 4*D of
# four-column capacity; the flow only had 197px slack, so D must be <= 49).
# Combined fix instead: ET VOUS Russian note 6 -> 3 lines (eh -87) plus
# dy 1690 -> 1610 (+40 vs core). Box then ends 1567.6, new rule at 1598
# (30px clear); P2-ex capacity slack after +40 is 37px (verify by render).
apply_file("content12.py", [
    ('dy = 1690', 'dy = 1610'),
    ('"Расскажите о своём возвращении в школу: где вы были в понедельник утром и какую книгу прочитали на каникулах? Напишите два предложения по-французски и пришлите в редакцию."',
     '"Расскажите о возвращении: где вы были в понедельник утром, что читали? Пришлите два предложения!"', 2),
])
print("transform round 3 done")

section(4)
# Round 4: occlusion-audit NEW flags (all box-title/line overflows; measured
# with text_w before fixing; ink right must be <= 1885, LES DATES <= 961).
# P1 agenda footer RU line overflowed the page edge (ink 2276) -- p.text
# does not wrap, so the sentence itself is shortened.
apply_file("content12.py", [
    ('"LES DATES · ДАТЫ ФИНАЛЬНОГО УИК-ЭНДА"', '"LES DATES · ДАТЫ УИК-ЭНДА"'),
    ('"Результаты финального уик-энда станут известны в субботу вечером и в воскресенье."', '"Итоги: суббота вечером и воскресенье."'),
    ('"DANS CE NUMÉRO · СОДЕРЖАНИЕ"', '"DANS CE NUMÉRO · В НОМЕРЕ"'),
])
apply_file("content34.py", [
    ('"LES MOTS DES FÊTES · СЛОВА ПРАЗДНИКОВ"', '"LES MOTS DES FÊTES · СЛОВА"'),
    ('"un jour férié — государственный праздник"', '"un jour férié — праздничный день"'),
    ('"DATES À RETENIR · ДАТЫ НА ПАМЯТЬ"', '"DATES À RETENIR · КАЛЕНДАРЬ"'),
    ('"LES MOTS DU TENNIS · ТЕННИСНЫЕ СЛОВА"', '"LES MOTS DU TENNIS · ТЕННИС"'),
    ('"À SUIVRE · ПРОДОЛЖЕНИЕ СЛЕДУЕТ"', '"À SUIVRE · ПРОДОЛЖЕНИЕ"'),
])
apply_file("content56.py", [
    ('"MOTS DE LA MUSIQUE · МУЗЫКАЛЬНЫЕ СЛОВА"', '"MOTS DE LA MUSIQUE · МУЗЫКА"'),
    ('"PARIS CREATOR WEEK · НЕДЕЛЯ КРЕАТОРОВ"', '"PARIS CREATOR WEEK · КРЕАТОРЫ"'),
])
apply_file("content7.py", [
    ('"Примечание редакции: настоящих писем и лучших сочинений VOL.2 со стр. 8 не поступило (номер W44 не вышел); здесь — помеченный пример редакции, а настоящие работы будут разобраны в VOL.4."',
     '"Примечание редакции: настоящих писем и лучших сочинений VOL.2 со стр. 8 не поступило (W44 не вышел); здесь — помеченный пример, настоящие работы — в VOL.4."'),
])
print("transform round 4 done")
