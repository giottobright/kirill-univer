# -*- coding: utf-8 -*-
"""Визуал коммерческого предложения (Задание 2)."""
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

plt.rcParams['font.family'] = 'DejaVu Sans'
A = '/home/user/kirill-univer/work/assets/'
NAVY, BLUE, GREEN, ORANGE, GREY = '#1F4E78', '#2E75B6', '#548235', '#ED7D31', '#7F7F7F'


def w(t, n):
    return '\n'.join(textwrap.fill(p, n) for p in t.split('\n'))


fig, ax = plt.subplots(figsize=(9.6, 13.6))
ax.set_xlim(0, 9.6)
ax.set_ylim(0, 13.6)
ax.axis('off')
ax.add_patch(Rectangle((0, 0), 9.6, 13.6, fc='white', ec=NAVY, lw=2))

# шапка
ax.add_patch(Rectangle((0, 12.4), 9.6, 1.2, fc=NAVY))
ax.add_patch(Rectangle((0.4, 12.65), 0.7, 0.7, fc='white'))
ax.text(0.75, 13.0, 'Н', ha='center', va='center', fontsize=20, weight='bold', color=NAVY)
ax.text(1.35, 13.15, 'ООО «НОРБИТ» (ГК ЛАНИТ)', fontsize=12, weight='bold', color='white')
ax.text(1.35, 12.78, 'г. Москва  ·  +7 (495) 787-52-77  ·  srm@norbit.ru  ·  norbit.ru',
        fontsize=8, color='#CCD8E6')
ax.text(9.2, 13.0, 'КОММЕРЧЕСКОЕ\nПРЕДЛОЖЕНИЕ', ha='right', va='center',
        fontsize=10, weight='bold', color='white')

# заголовок
ax.text(4.8, 11.85, 'Перестаньте терять деньги', ha='center', fontsize=18,
        weight='bold', color=NAVY)
ax.text(4.8, 11.4, 'на ненадёжных поставщиках', ha='center', fontsize=18,
        weight='bold', color=ORANGE)
# лид
ax.text(4.8, 10.85, w('Каждый сорванный контракт — это убытки и простои. Модуль '
        '«SRM.Аттестация» автоматически проверяет поставщиков и подсказывает, '
        'с кем безопасно работать.', 78), ha='center', va='center', fontsize=9.5,
        color='#333')

# оффер
ax.add_patch(FancyBboxPatch((0.5, 9.0), 8.6, 1.35, boxstyle='round,pad=0.02,rounding_size=0.06',
             fc='#DEEBF7', ec=BLUE, lw=1.5))
ax.text(4.8, 9.95, 'НАШЕ ПРЕДЛОЖЕНИЕ', ha='center', fontsize=10, weight='bold', color=NAVY)
ax.text(4.8, 9.4, w('Снизьте долю срывов поставок на 25 % за счёт автоматической '
        'аттестации поставщиков и объективного рейтинга их надёжности. Система '
        'сама составит графики проверок и выберет оптимального партнёра под '
        'вашу закупку.', 82), ha='center', va='center', fontsize=9, color='#222')

# тарифы
ax.text(0.5, 8.55, 'ТАРИФЫ', fontsize=10, weight='bold', color=NAVY)
tariffs = [('БАЗОВЫЙ', 'от 2,5 млн ₽', ['До 100 поставщиков', 'Графики аттестации',
            'Рейтинг надёжности'], BLUE),
           ('ПРОФЕССИОНАЛЬНЫЙ', 'от 5 млн ₽', ['Расширенная аналитика',
            'Интеграции с 1С и ФНС', 'Автоподбор партнёров'], GREEN),
           ('КОРПОРАТИВНЫЙ', 'от 12 млн ₽', ['Без ограничений',
            'Выделенная поддержка', 'Настройка «под ключ»'], ORANGE)]
for i, (name, price, feats, col) in enumerate(tariffs):
    x = 0.5 + i * 2.95
    ax.add_patch(FancyBboxPatch((x, 6.2), 2.75, 2.15,
                 boxstyle='round,pad=0.02,rounding_size=0.06', fc='white', ec=col, lw=1.8))
    ax.add_patch(FancyBboxPatch((x, 7.75), 2.75, 0.6,
                 boxstyle='round,pad=0.02,rounding_size=0.06', fc=col, ec=col))
    ax.text(x + 1.375, 8.05, name, ha='center', va='center', fontsize=8.2,
            weight='bold', color='white')
    ax.text(x + 1.375, 7.4, price, ha='center', fontsize=11, weight='bold', color=col)
    for j, f in enumerate(feats):
        ax.text(x + 0.18, 7.0 - j * 0.32, '• ' + f, fontsize=7.4, color='#333')

# убеждение
ax.text(0.5, 5.85, 'ПОЧЕМУ НОРБИТ', fontsize=10, weight='bold', color=NAVY)
adv = ['Решение в реестре российского ПО', 'Экспертиза ГК ЛАНИТ, десятки внедрений',
       'Бесплатный пилот на 30 дней', 'Гарантия поддержки по SLA']
for i, a in enumerate(adv):
    x = 0.5 + (i % 2) * 4.5
    y = 5.4 - (i // 2) * 0.5
    ax.add_patch(FancyBboxPatch((x, y - 0.16), 4.2, 0.42,
                 boxstyle='round,pad=0.01,rounding_size=0.05', fc='#E2EFDA', ec=GREEN))
    ax.text(x + 0.15, y + 0.05, '✓  ' + a, fontsize=8.2, va='center', color='#222')

# схема взаимодействия
ax.text(0.5, 4.0, 'СХЕМА РАБОТЫ', fontsize=10, weight='bold', color=NAVY)
steps = ['Заявка', 'Демонстрация\nи аудит', 'Договор', 'Внедрение\nи настройка',
         'Обучение', 'Поддержка\nпо SLA']
for i, s in enumerate(steps):
    x = 0.55 + i * 1.5
    ax.add_patch(FancyBboxPatch((x, 3.05), 1.25, 0.7,
                 boxstyle='round,pad=0.01,rounding_size=0.05', fc=NAVY, ec=NAVY))
    ax.text(x + 0.625, 3.4, s, ha='center', va='center', fontsize=6.7, color='white')
    if i < 5:
        ax.add_patch(FancyArrowPatch((x + 1.27, 3.4), (x + 1.5, 3.4),
                     arrowstyle='-|>', mutation_scale=9, color=GREY))

# призыв к действию
ax.add_patch(FancyBboxPatch((0.5, 1.55), 8.6, 1.15,
             boxstyle='round,pad=0.02,rounding_size=0.06', fc=ORANGE, ec=ORANGE))
ax.text(4.8, 2.32, 'Закажите бесплатную демонстрацию модуля «SRM.Аттестация»',
        ha='center', fontsize=10.5, weight='bold', color='white')
ax.text(4.8, 1.9, 'Оставьте заявку на norbit.ru или позвоните: +7 (495) 787-52-77.  '
        'Предложение действует до конца квартала.', ha='center', fontsize=8.2, color='white')

ax.text(4.8, 0.7, 'ООО «НОРБИТ» — российский разработчик систем управления '
        'закупками и поставщиками  ·  Вариант № 7  ·  [ФИО студентов]',
        ha='center', fontsize=7.3, color=GREY, style='italic')

fig.savefig(A + 'kp.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig)
print('kp.png готов')
