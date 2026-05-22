# -*- coding: utf-8 -*-
"""Генерация всех диаграмм и визуалов практикума (Вариант 7, НОРБИТ SRM)."""
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse, FancyArrowPatch, Circle
from matplotlib.lines import Line2D

plt.rcParams['font.family'] = 'DejaVu Sans'
A = '/home/user/kirill-univer/work/assets/'
D = json.load(open('/home/user/kirill-univer/work/data.json', encoding='utf-8'))
poly, ge, bcg = D['poly'], D['ge'], D['bcg']

NAVY, BLUE, LBLUE = '#1F4E78', '#2E75B6', '#9DC3E6'
GREEN, LGREEN = '#548235', '#C6E0B4'
YELLOW, ORANGE, RED = '#FFC000', '#ED7D31', '#C00000'
GREY, LGREY = '#7F7F7F', '#F2F2F2'
P1, P2, P3 = '#2E75B6', '#548235', '#ED7D31'  # цвета участников команды


def save(fig, name):
    fig.savefig(A + name, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('  ', name)


def rbox(ax, x, y, w, h, text, fc, ec='none', tc='white', fs=9, bold=False, round=0.025):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0.004,rounding_size={round}',
                                fc=fc, ec=ec, lw=1.2))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs,
            color=tc, weight='bold' if bold else 'normal', wrap=True)


# ============ 1. МНОГОУГОЛЬНИК КОНКУРЕНТОСПОСОБНОСТИ ============
def diagram_polygon():
    crit = poly['crit']
    N = len(crit)
    ang = [n / N * 2 * math.pi for n in range(N)] + [0]
    fig, ax = plt.subplots(figsize=(9.5, 8.5), subplot_kw=dict(polar=True))
    cols = {'НОРБИТ: Управление закупками (SRM)': RED,
            'Comindware Управление закупками': BLUE,
            'Bidzaar': GREEN, 'AGORA SRM': ORANGE,
            '1С:ERP Управление предприятием 2': '#7030A0'}
    for c in poly['companies']:
        vals = poly['scores'][c] + [poly['scores'][c][0]]
        thick = c in ('НОРБИТ: Управление закупками (SRM)', '1С:ERP Управление предприятием 2')
        ax.plot(ang, vals, color=cols[c], lw=4.5 if thick else 1.8,
                label=c, marker='o', ms=6 if thick else 3,
                zorder=5 if thick else 3)
        if thick:
            ax.fill(ang, vals, color=cols[c], alpha=0.12)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels([c.replace(' ', '\n', 1) for c in crit], fontsize=9)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=8, color=GREY)
    ax.set_title('Многоугольник конкурентоспособности\n([ФИО студентов], Вариант 7)',
                 fontsize=13, weight='bold', color=NAVY, pad=28)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), fontsize=8.5, ncol=2)
    ax.grid(color='#CCCCCC')
    save(fig, 'polygon.png')


# ============ 2. МАТРИЦА ВАЖНОСТЬ / ЭФФЕКТИВНОСТЬ ============
def diagram_importance_eff():
    crit = poly['crit']
    imp = poly['importance']
    sc = poly['scores']['НОРБИТ: Управление закупками (SRM)']
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.axhspan(7, 11, facecolor=LGREEN, alpha=0.35)
    ax.axhspan(0, 7, facecolor='#FCE4D6', alpha=0.35)
    ax.axhline(7, ls='--', lw=2.2, color=GREEN, label='Порог полезности (7 баллов)')
    ax.axvline(0.10, ls='--', lw=2.2, color=RED, label='Порог важности (0,10)')
    # i: (dx, dy) подписи в пунктах; отрицательный dy — подпись снизу
    off = {0: (0, 12), 1: (0, 12), 2: (0, 12), 3: (0, -16), 4: (0, 12),
           5: (0, 12), 6: (0, -16), 7: (0, 12), 8: (0, 12), 9: (0, 12)}
    for i, c in enumerate(crit):
        ax.scatter(imp[i], sc[i], s=220, color=BLUE, edgecolor=NAVY, zorder=5)
        dx, dy = off[i]
        ax.annotate(c, (imp[i], sc[i]), fontsize=8.5, ha='center',
                    va='bottom' if dy > 0 else 'top', xytext=(dx, dy),
                    textcoords='offset points')
    ax.set_xlim(0.04, 0.17)
    ax.set_ylim(0, 11)
    ax.set_xlabel('Важность критерия', fontsize=11, weight='bold')
    ax.set_ylabel('Полезность атрибута (балл ИС «НОРБИТ»)', fontsize=11, weight='bold')
    ax.set_title('Матрица «Важность / Эффективность» ([ФИО студентов], Вариант 7)',
                 fontsize=12.5, weight='bold', color=NAVY)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(alpha=0.3)
    save(fig, 'importance_effectiveness.png')


# ============ 3. МАТРИЦА GE / McKINSEY ============
def diagram_ge():
    fig, ax = plt.subplots(figsize=(9.5, 9))
    zones = [['#FFD966', '#A9D18E', '#A9D18E'],
             ['#FF8A80', '#FFD966', '#A9D18E'],
             ['#FF8A80', '#FF8A80', '#FFD966']]
    nums = [['№1', '№2', '№3'], ['№4', '№5', '№6'], ['№7', '№8', '№9']]
    # ряды снизу вверх: низкая/средняя/высокая привлекательность
    for r in range(3):
        for c in range(3):
            ax.add_patch(Rectangle((c, r), 1, 1, fc=zones[2 - r][c], ec='white', lw=3))
            ax.text(c + 0.06, r + 0.93, nums[2 - r][c], fontsize=10, weight='bold',
                    va='top', color='#444444')
    lvl = {'низкая': 0, 'средняя': 1, 'высокая': 2}
    seg = ge['segments']
    for i, s in enumerate(seg):
        x = lvl[ge['comp_level'][s]] + 0.5
        y = lvl[ge['attr_level'][s]] + 0.5
        ax.add_patch(Circle((x, y), 0.30, fc=NAVY, ec='white', lw=2.5, zorder=5))
        ax.text(x, y, f'С{i+1}', ha='center', va='center', color='white',
                fontsize=13, weight='bold', zorder=6)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(['Низкая', 'Средняя', 'Высокая'], fontsize=10)
    ax.set_yticks([0.5, 1.5, 2.5])
    ax.set_yticklabels(['Низкая', 'Средняя', 'Высокая'], fontsize=10, rotation=90, va='center')
    ax.set_xlabel('Конкурентоспособность бизнеса в сегменте', fontsize=11, weight='bold')
    ax.set_ylabel('Привлекательность рынка (сегмента)', fontsize=11, weight='bold')
    ax.set_title('Матрица GE / McKinsey ([ФИО студентов], Вариант 7)',
                 fontsize=12.5, weight='bold', color=NAVY, pad=12)
    leg = '\n'.join(f'С{i+1} — {s}  (привл.={ge["attr_total"][s]:.2f}; '
                    f'конкур.={ge["comp_total"][s]:.2f})' for i, s in enumerate(seg))
    ax.text(1.5, -0.55, leg, ha='center', va='top', fontsize=8.6,
            transform=ax.transData)
    ax.set_aspect('equal')
    save(fig, 'ge_mckinsey.png')


# ============ 4. МАТРИЦА BCG (пузырьковая) ============
def diagram_bcg():
    rows = bcg['rows']
    fig, ax = plt.subplots(figsize=(11, 8.5))
    xmax = max(r['odr'] for r in rows) * 1.25
    ymax = max(r['trw'] for r in rows) * 1.2
    ax.axvspan(0, 1, 0, 1, facecolor='#FFF2CC', alpha=0.0)
    ax.axhline(10, ls='--', color=GREY, lw=1.6)
    ax.axvline(1, ls='--', color=GREY, lw=1.6)
    ax.add_patch(Rectangle((0, 10), 1, ymax - 10, fc='#DEEBF7', alpha=0.55))
    ax.add_patch(Rectangle((1, 10), xmax - 1, ymax - 10, fc='#E2EFDA', alpha=0.6))
    ax.add_patch(Rectangle((0, 0), 1, 10, fc='#FCE4D6', alpha=0.6))
    ax.add_patch(Rectangle((1, 0), xmax - 1, 10, fc='#FFF2CC', alpha=0.7))
    ax.text(0.5, ymax * 0.97, 'ТРУДНЫЕ ДЕТИ', ha='center', fontsize=11,
            weight='bold', color=BLUE)
    ax.text((1 + xmax) / 2, ymax * 0.97, 'ЗВЁЗДЫ', ha='center', fontsize=11,
            weight='bold', color=GREEN)
    ax.text(0.5, 1.0, 'СОБАКИ', ha='center', fontsize=11, weight='bold', color=RED)
    ax.text((1 + xmax) / 2, 1.0, 'ДОЙНЫЕ КОРОВЫ', ha='center', fontsize=11,
            weight='bold', color=ORANGE)
    cols = {'ЗВЕЗДЫ': GREEN, 'ТРУДНЫЕ ДЕТИ': BLUE, 'ДОЙНЫЕ КОРОВЫ': ORANGE, 'СОБАКИ': RED}
    for i, r in enumerate(rows):
        size = r['s25'] / max(x['s25'] for x in rows) * 4500 + 500
        ax.scatter(r['odr'], r['trw'], s=size, color=cols[r['quad']],
                   alpha=0.55, edgecolor='black', lw=1.2, zorder=4)
        ax.text(r['odr'], r['trw'], f'Т{i+1}', ha='center', va='center',
                fontsize=10, weight='bold', zorder=6)
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.set_xlabel('Относительная доля рынка (ОДР)', fontsize=11, weight='bold')
    ax.set_ylabel('Взвешенный темп роста рынка, %', fontsize=11, weight='bold')
    ax.set_title('Матрица BCG «Темп роста – Доля рынка» ([ФИО студентов], Вариант 7)',
                 fontsize=12, weight='bold', color=NAVY)
    leg = '   '.join(f'Т{i+1} — {r["name"]}' for i, r in enumerate(rows))
    ax.text(0.5, -0.12, leg, transform=ax.transAxes, ha='center', fontsize=7.6)
    ax.grid(alpha=0.25)
    save(fig, 'bcg.png')


# ============ 5. МАТРИЦА АНСОФФА ============
def diagram_ansoff():
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.axis('off')
    cells = [
        (0, 1, LGREEN, 'СТРАТЕГИЯ ПРОНИКНОВЕНИЯ', 'Текущий товар — текущий рынок',
         'Возможна. Рост доли SRM на рынке РФ:\nактивизация продаж, расширение\nклиентской базы, кросс-продажи.\nРиск ≈50%, базовые расходы.'),
        (1, 1, '#A9D18E', 'СТРАТЕГИЯ РАЗВИТИЯ ТОВАРА', 'Новый товар — текущий рынок',
         'ВОЗМОЖНА — ПРИОРИТЕТ. Вывод SRM 2.0\nс модулем «SRM.Аттестация»: графики\nаттестации, рейтинг надёжности,\nвыбор партнёров. Риск ≈33%.'),
        (0, 0, '#FFE699', 'СТРАТЕГИЯ РАЗВИТИЯ РЫНКА', 'Текущий товар — новый рынок',
         'Вероятна. Выход текущей SRM на\nрынки ЕАЭС/СНГ и в сегмент\nгосзаказчиков (223-ФЗ).\nРиск ≈20%, 4-кратные расходы.'),
        (1, 0, '#FF8A80', 'СТРАТЕГИЯ ДИВЕРСИФИКАЦИИ', 'Новый товар — новый рынок',
         'Не возможна. Высокий риск (≈5%),\n12-16-кратные расходы, нет\nкомпетенций. Стратегия\nотклоняется.'),
    ]
    for cx, cy, fc, title, sub, body in cells:
        x, y = cx * 5 + 0.3, cy * 4 + 0.3
        ax.add_patch(FancyBboxPatch((x, y), 4.6, 3.6, boxstyle='round,pad=0.02,rounding_size=0.1',
                                    fc=fc, ec=NAVY, lw=2))
        ax.text(x + 2.3, y + 3.25, title, ha='center', fontsize=11.5, weight='bold', color=NAVY)
        ax.text(x + 2.3, y + 2.85, sub, ha='center', fontsize=8.5, style='italic', color='#444')
        ax.text(x + 2.3, y + 1.5, body, ha='center', fontsize=8.8, color='#222')
    ax.text(5.3, 8.4, 'Продукт', ha='center', fontsize=11, weight='bold', color=NAVY)
    ax.text(2.6, 8.0, 'Существующий', ha='center', fontsize=9.5, color='#444')
    ax.text(7.9, 8.0, 'Новый', ha='center', fontsize=9.5, color='#444')
    ax.text(-0.15, 4.3, 'Рынок', va='center', rotation=90, fontsize=11, weight='bold', color=NAVY)
    ax.text(0.12, 6.1, 'Существующий', va='center', rotation=90, fontsize=9.5, color='#444')
    ax.text(0.12, 2.1, 'Новый', va='center', rotation=90, fontsize=9.5, color='#444')
    ax.set_xlim(-0.4, 10)
    ax.set_ylim(-0.3, 8.7)
    ax.set_title('Матрица Ансоффа ([ФИО студентов], Вариант 7)',
                 fontsize=13, weight='bold', color=NAVY, pad=16)
    save(fig, 'ansoff.png')


for f in (diagram_polygon, diagram_importance_eff, diagram_ge, diagram_bcg, diagram_ansoff):
    f()
print('Аналитические диаграммы готовы')
