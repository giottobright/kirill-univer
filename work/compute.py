# -*- coding: utf-8 -*-
"""Расчёт всех числовых результатов практикума (Вариант 7). Сохраняет data.json."""
import json, statistics

# ============ МНОГОУГОЛЬНИК КОНКУРЕНТОСПОСОБНОСТИ (Табл.27) ============
crit = ['Размер бизнеса заказчика', 'Функционал', 'Гибкость и масштабируемость',
        'Производительность платформы', 'Кастомизация', 'Универсальность решения',
        'Разнообразие ценообразования', 'Рекламная активность', 'Известность бренда',
        'Дистрибуция']
companies = ['НОРБИТ: Управление закупками (SRM)', 'Comindware Управление закупками',
             'Bidzaar', 'AGORA SRM', '1С:ERP Управление предприятием 2']
scores = {
    'НОРБИТ: Управление закупками (SRM)': [10, 4, 5, 7, 2, 9, 4, 5, 7, 4],
    'Comindware Управление закупками':    [7, 8, 9, 8, 9, 7, 6, 7, 7, 6],
    'Bidzaar':                            [6, 7, 7, 6, 6, 6, 8, 8, 6, 9],
    'AGORA SRM':                          [8, 6, 6, 7, 5, 7, 7, 6, 5, 7],
    '1С:ERP Управление предприятием 2':   [9, 9, 8, 6, 8, 8, 5, 6, 10, 8],
}
importance = [0.08, 0.15, 0.12, 0.10, 0.13, 0.11, 0.07, 0.06, 0.09, 0.09]

diff = [statistics.stdev([scores[c][i] for c in companies]) for i in range(10)]
C = [importance[i] * diff[i] for i in range(10)]
sumC = sum(C)
determ = [C[i] / sumC for i in range(10)]
U = {c: sum(scores[c][i] * importance[i] for i in range(10)) for c in companies}
Udet = {c: sum(scores[c][i] * determ[i] for i in range(10)) for c in companies}
competitors = companies[1:]
best_comp = max(competitors, key=lambda c: U[c])
rel_eff = [scores[companies[0]][i] / scores[best_comp][i] for i in range(10)]

poly = dict(crit=crit, companies=companies, scores=scores, importance=importance,
            diff=diff, C=C, determ=determ, U=U, Udet=Udet,
            best_comp=best_comp, rel_eff=rel_eff)

# ============ GE / McKinsey ============
ge_comp_crit = [
    'ИТ-продукт имеет зарегистрированную торговую марку',
    'Компания имеет надёжный канал привлечения заказчиков',
    'Известный бренд, под которым реализуются ИТ-товары, сильнее, чем у конкурентов',
    'Компания имеет отличный имидж, и он выше, чем у конкурентов',
    'Высокий уровень разнообразия ИТ-товаров и дифференциации на рынке',
    'Компания может быстро адаптироваться к рыночным изменениям']
ge_attr_crit = [
    'Высокий потенциал роста рынка и сегмента',
    'Ограниченное количество игроков с высокой динамикой их продаж',
    'Лёгкий выход на рынок для новых игроков',
    'Высокий уровень лояльности у нашей компании в сегменте',
    'Сегмент является самым быстрорастущим из оцениваемых альтернатив',
    'Минимальны риски влияния внешних экономических факторов на ёмкость рынка']
segments = ['Крупный бизнес и корпорации (промышленность, ритейл, ТЭК)',
            'Госзаказчики и компании с госучастием (223-ФЗ)',
            'Средний бизнес (производство, опт, логистика)']
wc = [0.20, 0.18, 0.17, 0.15, 0.16, 0.14]
wa = [0.18, 0.15, 0.14, 0.20, 0.18, 0.15]
comp_sc = {'Крупный бизнес и корпорации (промышленность, ритейл, ТЭК)': [8, 8, 9, 8, 7, 6],
           'Госзаказчики и компании с госучастием (223-ФЗ)':           [7, 6, 6, 6, 5, 5],
           'Средний бизнес (производство, опт, логистика)':            [5, 4, 4, 4, 5, 6]}
attr_sc = {'Крупный бизнес и корпорации (промышленность, ритейл, ТЭК)': [7, 5, 3, 8, 5, 6],
           'Госзаказчики и компании с госучастием (223-ФЗ)':           [8, 6, 4, 6, 7, 4],
           'Средний бизнес (производство, опт, логистика)':            [9, 8, 8, 5, 9, 7]}
comp_total = {s: sum(comp_sc[s][i] * wc[i] for i in range(6)) for s in segments}
attr_total = {s: sum(attr_sc[s][i] * wa[i] for i in range(6)) for s in segments}

def level(v):
    return 'низкая' if v <= 3.33 else ('средняя' if v <= 6.67 else 'высокая')

ge = dict(comp_crit=ge_comp_crit, attr_crit=ge_attr_crit, segments=segments,
          wc=wc, wa=wa, comp_sc=comp_sc, attr_sc=attr_sc,
          comp_total=comp_total, attr_total=attr_total,
          comp_level={s: level(comp_total[s]) for s in segments},
          attr_level={s: level(attr_total[s]) for s in segments})

# ============ BCG ============
bcg_raw = [  # name, sales2024, sales2025, capacity, share_brand%, share_comp%
    ('«НОРБИТ: Управление закупками (SRM)»', 5063, 5040, 11000, 31, 11),
    ('«НОРБИТ: Управление автотранспортом»', 1313, 6013, 75755, 8, 29),
    ('«НОРБИТ: ТОИР» (управление активами)', 2220, 9332, 67121, 36, 12),
    ('«НОРБИТ: Управление складом (WMS)»', 2764, 2643, 67766, 9, 36),
    ('«НОРБИТ: Управление маркетингом»', 8879, 7817, 48629, 28, 14),
    ('«НОРБИТ: Сервис Деск»', 8864, 3615, 96684, 16, 34),
]
sumE = sum(r[3] for r in bcg_raw)
bcg = []
for name, s24, s25, cap, sb, sc in bcg_raw:
    tr = s25 / s24 * 100
    trw = cap * tr / sumE
    growth = 'высокий' if trw > 10 else 'низкий'
    odr = sb / sc
    odr_txt = 'высокая' if odr > 1 else 'низкая'
    if growth == 'высокий' and odr > 1:
        quad = 'ЗВЕЗДЫ'
    elif growth == 'высокий' and odr <= 1:
        quad = 'ТРУДНЫЕ ДЕТИ'
    elif growth == 'низкий' and odr > 1:
        quad = 'ДОЙНЫЕ КОРОВЫ'
    else:
        quad = 'СОБАКИ'
    bcg.append(dict(name=name, s24=s24, s25=s25, cap=cap, share_brand=sb,
                     share_comp=sc, tr=tr, trw=trw, growth=growth, odr=odr,
                     odr_txt=odr_txt, quad=quad))

data = dict(poly=poly, ge=ge, bcg=dict(rows=bcg, sumE=sumE))
with open('/home/user/kirill-univer/work/data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print('=== МНОГОУГОЛЬНИК ===')
for c in companies:
    print(f'  {c[:35]:35} U={U[c]:.3f}  Uдет={Udet[c]:.3f}')
print(f'  Лучший конкурент: {best_comp}')
print('  Дифференциация:', [round(x, 2) for x in diff])
print('  Детерминация: ', [round(x, 3) for x in determ])
print('  Отн.эффективность:', [round(x, 2) for x in rel_eff])
print('=== GE/McKinsey ===')
for s in segments:
    print(f'  {s[:40]:40} конкур={comp_total[s]:.2f}({level(comp_total[s])}) '
          f'привлек={attr_total[s]:.2f}({level(attr_total[s])})')
print('=== BCG ===  sumE=', sumE)
for r in bcg:
    print(f'  {r["name"][:42]:42} ТР={r["tr"]:.1f}% ТРвзв={r["trw"]:.2f}% '
          f'ОДР={r["odr"]:.2f} -> {r["quad"]}')
