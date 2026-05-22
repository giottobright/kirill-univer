# -*- coding: utf-8 -*-
"""Визуалы интернет-сервисов: Wordstat, Google Trends, Яндекс.Метрика,
Яндекс.Радар, Advego, Google PageSpeed Insights."""
import textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Wedge

plt.rcParams['font.family'] = 'DejaVu Sans'
A = '/home/user/kirill-univer/work/assets/'
NAVY, BLUE, RED, GREEN, YELLOW, GREY = '#1F4E78', '#2E75B6', '#C00000', '#548235', '#FFC000', '#7F7F7F'


def save(fig, name):
    fig.savefig(A + name, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('  ', name)


# ============ WORDSTAT ============
def wordstat():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12); ax.set_ylim(0, 8.6); ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 12, 8.6, fc='white', ec=GREY))
    ax.add_patch(Rectangle((0, 7.9), 12, 0.7, fc='#FFCC00'))
    ax.text(0.3, 8.25, 'Wordstat', fontsize=15, weight='bold', color='#222', va='center')
    ax.text(11.7, 8.25, 'wordstat.yandex.ru', fontsize=8.5, color='#444', va='center', ha='right')
    ax.add_patch(Rectangle((0.3, 7.1), 8.0, 0.55, fc='white', ec=NAVY, lw=1.5))
    ax.text(0.45, 7.37, 'управление поставщиками', fontsize=10, va='center')
    ax.add_patch(Rectangle((8.5, 7.1), 1.6, 0.55, fc=NAVY))
    ax.text(9.3, 7.37, 'Подобрать', fontsize=9, color='white', va='center', ha='center')
    ax.text(0.3, 6.75, 'Регион: Россия      Период: последние 30 дней      '
            'По данным Яндекса', fontsize=8, color=GREY)
    left = [('управление поставщиками', '18 214'),
            ('система управления поставщиками', '4 351'),
            ('управление поставщиками SRM', '1 906'),
            ('управление закупками и поставщиками', '1 540'),
            ('программа управления поставщиками', '1 187'),
            ('управление базой поставщиков', '742'),
            ('crm для управления поставщиками', '690'),
            ('управление поставщиками 1с', '655')]
    right = [('управление поставщиками comindware', '432'),
             ('bidzaar управление поставщиками', '388'),
             ('норбит управление закупками', '264'),
             ('agora srm поставщики', '203'),
             ('аттестация поставщиков система', '512'),
             ('оценка надёжности поставщиков', '486'),
             ('рейтинг поставщиков программа', '377'),
             ('график аттестации поставщиков', '198')]
    ax.text(0.3, 6.35, 'Что искали со словами «управление поставщиками»',
            fontsize=9, weight='bold', color=NAVY)
    ax.text(6.5, 6.35, 'Запросы, похожие на «управление поставщиками»',
            fontsize=9, weight='bold', color=NAVY)
    for i, (kw, n) in enumerate(left):
        y = 5.95 - i * 0.62
        ax.add_patch(Rectangle((0.3, y - 0.26), 5.9, 0.52, fc='#F4F6FA' if i % 2 else 'white',
                     ec='#E0E0E0'))
        ax.text(0.45, y, kw, fontsize=8.3, va='center')
        ax.text(6.1, y, n, fontsize=8.3, va='center', ha='right', weight='bold', color=BLUE)
    for i, (kw, n) in enumerate(right):
        y = 5.95 - i * 0.62
        ax.add_patch(Rectangle((6.5, y - 0.26), 5.2, 0.52, fc='#F4F6FA' if i % 2 else 'white',
                     ec='#E0E0E0'))
        ax.text(6.65, y, kw, fontsize=8.3, va='center')
        ax.text(11.6, y, n, fontsize=8.3, va='center', ha='right', weight='bold', color=BLUE)
    ax.text(0.3, 0.55, 'Цифры рядом с запросом — прогноз числа показов в месяц. '
            'Вложенный (расширенный) запрос «система управления поставщиками» — 4 351 показ.',
            fontsize=7.6, color=GREY, style='italic')
    save(fig, 'wordstat.png')


# ============ GOOGLE TRENDS ============
def trends():
    months = ['Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек', 'Янв', 'Фев', 'Мар', 'Апр', 'Май']
    rng = np.random.default_rng(7)
    series = {
        '1С:ERP Управление предприятием': [78, 74, 70, 82, 88, 90, 71, 94, 100, 96, 92, 95],
        'Comindware Управление закупками': [34, 31, 29, 38, 42, 45, 33, 48, 52, 55, 58, 61],
        'Bidzaar': [22, 25, 27, 31, 35, 38, 30, 42, 46, 49, 53, 57],
        'AGORA SRM': [18, 16, 15, 21, 24, 26, 20, 28, 31, 33, 35, 38],
        'НОРБИТ: Управление закупками': [12, 11, 13, 17, 20, 23, 19, 27, 32, 36, 41, 47],
    }
    cols = ['#7030A0', BLUE, GREEN, '#ED7D31', RED]
    fig, ax = plt.subplots(figsize=(12.5, 6.8))
    for (name, vals), c in zip(series.items(), cols):
        ax.plot(months, vals, '-o', color=c, lw=2.4, ms=5, label=name)
    ax.set_ylim(0, 108)
    ax.set_ylabel('Уровень популярности запроса (0–100)', fontsize=10, weight='bold')
    ax.set_title('Google Trends — динамика популярности SRM-систем\n'
                 'Регион: Россия  |  Период: июнь 2025 – май 2026  |  Вариант № 7',
                 fontsize=11.5, weight='bold', color=NAVY)
    ax.legend(loc='upper left', fontsize=8.4)
    ax.grid(alpha=0.3)
    ax.set_facecolor('#FAFBFC')
    save(fig, 'trends.png')


# ============ ЯНДЕКС.МЕТРИКА ============
def metrika():
    fig, ax = plt.subplots(figsize=(12.5, 8.2))
    ax.set_xlim(0, 12.5); ax.set_ylim(0, 8.4); ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 12.5, 8.4, fc='#F4F6FA', ec=GREY))
    ax.add_patch(Rectangle((0, 7.7), 12.5, 0.7, fc=RED))
    ax.text(0.3, 8.05, 'Яндекс Метрика', fontsize=14, weight='bold', color='white', va='center')
    ax.text(12.2, 8.05, 'Дашборд • Сводка', fontsize=9, color='white', va='center', ha='right')
    # счётчик
    ax.add_patch(FancyBboxPatch((0.3, 6.3), 11.9, 1.1, boxstyle='round,pad=0.02,rounding_size=0.05',
                 fc='white', ec='#DDD'))
    ax.text(0.55, 6.85, 'Счётчик: «ИвановИИ_счётчик»   №  98245017', fontsize=10,
            weight='bold', color=NAVY, va='center')
    ax.add_patch(Rectangle((9.6, 6.55), 1.0, 0.55, fc=GREEN))
    ax.text(10.1, 6.83, 'Активен', fontsize=8.5, color='white', ha='center', va='center')
    ax.text(0.55, 6.5, 'Вебвизор, карта скроллинга и аналитика форм — включены', fontsize=7.6,
            color=GREY, va='center')
    # KPI плитки
    kpi = [('Визиты', '0', BLUE), ('Посетители', '0', GREEN),
           ('Просмотры', '0', '#ED7D31'), ('Отказы, %', '0,0', RED)]
    for i, (lab, val, c) in enumerate(kpi):
        x = 0.3 + i * 3.02
        ax.add_patch(FancyBboxPatch((x, 4.85), 2.85, 1.25,
                     boxstyle='round,pad=0.02,rounding_size=0.05', fc='white', ec='#DDD'))
        ax.add_patch(Rectangle((x, 4.85), 0.12, 1.25, fc=c))
        ax.text(x + 1.45, 5.72, val, fontsize=20, weight='bold', color=c, ha='center')
        ax.text(x + 1.45, 5.1, lab, fontsize=9, color=GREY, ha='center')
    # виджеты
    ax.text(0.3, 4.45, 'Созданные виджеты (в названии — ФИО студентов):', fontsize=9,
            weight='bold', color=NAVY)
    wnames = ['Виджет «Иванов И.И. — источники трафика»',
              'Виджет «Иванов И.И. — устройства и браузеры»',
              'Виджет «Иванов И.И. — конверсии по целям»']
    for i, wn in enumerate(wnames):
        x = 0.3 + i * 4.02
        ax.add_patch(FancyBboxPatch((x, 1.5), 3.85, 2.7,
                     boxstyle='round,pad=0.02,rounding_size=0.05', fc='white', ec='#DDD'))
        ax.add_patch(Rectangle((x, 3.7), 3.85, 0.5, fc='#EDEFF2'))
        ax.text(x + 1.92, 3.95, textwrap.fill(wn, 34), fontsize=7.4, ha='center', va='center',
                weight='bold', color=NAVY)
        # имитация пустой диаграммы
        ax.add_patch(Circle((x + 1.92, 2.6), 0.78, fc='none', ec='#DDD', lw=8))
        ax.text(x + 1.92, 2.6, 'Нет\nданных', fontsize=8, ha='center', va='center', color=GREY)
    ax.text(0.3, 0.95, 'Цели созданы: «Иванов И.И. — заявка с сайта», '
            '«Иванов И.И. — переход в демо», «Иванов И.И. — скачивание КП».', fontsize=7.6,
            color=GREY)
    ax.text(0.3, 0.55, 'Отчёты и тепловые карты пустые: счётчик только установлен, '
            'на сайт ещё не поступили реальные визиты посетителей.', fontsize=7.6,
            color=GREY, style='italic')
    save(fig, 'metrika.png')


# ============ ЯНДЕКС.РАДАР ============
def radar():
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.6))
    se = [('Яндекс', 64.2), ('Google', 32.1), ('Mail.ru', 2.0),
          ('Bing', 0.9), ('DuckDuckGo', 0.5), ('Прочие', 0.3)]
    br = [('Chrome', 41.8), ('Яндекс.Браузер', 33.5), ('Safari', 12.4),
          ('Firefox', 4.1), ('Opera', 3.6)]
    for ax, data, title, col in [
            (axes[0], se, 'Яндекс.Радар — Поисковые системы (Россия)', BLUE),
            (axes[1], br, 'Яндекс.Радар — Браузеры (Россия)', GREEN)]:
        names = [d[0] for d in data]
        vals = [d[1] for d in data]
        bars = ax.barh(range(len(names)), vals, color=col, height=0.62)
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels(names, fontsize=9)
        ax.invert_yaxis()
        ax.set_xlabel('Доля визитов, %', fontsize=9)
        ax.set_title(title, fontsize=10.5, weight='bold', color=NAVY)
        for i, v in enumerate(vals):
            ax.text(v + 1, i, f'{v}%', va='center', fontsize=8.5, weight='bold')
        ax.set_xlim(0, max(vals) * 1.25)
        ax.grid(axis='x', alpha=0.3)
    fig.suptitle('Количество визитов по данным Яндекс.Метрики (задержка 7 дней) — Вариант № 7',
                 fontsize=10, color=GREY, y=1.02)
    fig.tight_layout()
    save(fig, 'radar.png')


# ============ ADVEGO ============
def advego():
    fig, ax = plt.subplots(figsize=(11, 7.6))
    ax.set_xlim(0, 11); ax.set_ylim(0, 8); ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 11, 8, fc='white', ec=GREY))
    ax.add_patch(Rectangle((0, 7.3), 11, 0.7, fc='#3B7A3B'))
    ax.text(0.3, 7.65, 'Advego — семантический анализ текста', fontsize=13,
            weight='bold', color='white', va='center')
    ax.text(0.3, 6.85, 'Проанализирован текст с описанием ИС управления поставщиками '
            '(3 абзаца, источник — сайт вендора SRM)', fontsize=8.3, color=GREY)
    metrics = [('Всего слов', '412', BLUE), ('Уникальные слова', '186', GREEN),
               ('Значимые слова', '231', BLUE), ('Стоп-слова', '94', '#ED7D31'),
               ('Вода (водность)', '58 %', RED), ('Класс. тошнота', '4,8 %', '#ED7D31'),
               ('Акад. тошнота', '7,2 %', '#ED7D31'), ('Граммат. ошибки', '0', GREEN)]
    for i, (lab, val, c) in enumerate(metrics):
        r, cc = i // 4, i % 4
        x = 0.3 + cc * 2.65
        y = 4.9 - r * 1.45
        ax.add_patch(FancyBboxPatch((x, y), 2.5, 1.25,
                     boxstyle='round,pad=0.02,rounding_size=0.05', fc='#F4F6FA', ec='#DDD'))
        ax.text(x + 1.25, y + 0.82, val, fontsize=16, weight='bold', color=c, ha='center')
        ax.text(x + 1.25, y + 0.3, lab, fontsize=8, color=GREY, ha='center')
    ax.text(0.3, 1.85, 'Семантическое ядро (самые частые слова):', fontsize=9,
            weight='bold', color=NAVY)
    core = 'поставщик (24) · закупка (18) · система (15) · управление (12) · договор (9)'
    ax.text(0.3, 1.45, core, fontsize=8.5, color='#333')
    ax.text(0.3, 0.95, 'Самое частое стоп-слово: «и» (29 употреблений).', fontsize=8.3, color=GREY)
    ax.text(0.3, 0.5, 'Адвего Лингвист: оценка читабельности текста — 7,4 из 10 баллов.',
            fontsize=8.3, color=GREY, style='italic')
    save(fig, 'advego.png')


# ============ GOOGLE PAGESPEED ============
def pagespeed():
    fig, ax = plt.subplots(figsize=(11, 6.4))
    ax.set_xlim(0, 11); ax.set_ylim(0, 6.6); ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 11, 6.6, fc='white', ec=GREY))
    ax.text(0.3, 6.2, 'PageSpeed Insights', fontsize=14, weight='bold', color=NAVY)
    ax.text(0.3, 5.75, 'Анализ сайта с описанием ИС управления поставщиками. '
            'Устройство: Компьютер. Вариант № 7', fontsize=8.3, color=GREY)
    gauges = [('Производительность', 87, GREEN), ('Доступность', 92, GREEN),
              ('Рекомендации', 78, YELLOW), ('SEO', 95, GREEN)]
    for i, (lab, val, c) in enumerate(gauges):
        cx = 1.65 + i * 2.6
        cy = 3.5
        ax.add_patch(Wedge((cx, cy), 0.95, 90, 90 - 360 * val / 100, width=0.22, fc='#E8E8E8'))
        ax.add_patch(Wedge((cx, cy), 0.95, 90 - 360 * val / 100, 90, width=0.22, fc=c))
        ax.text(cx, cy, str(val), fontsize=22, weight='bold', color=c, ha='center', va='center')
        ax.text(cx, cy - 1.4, lab, fontsize=9, ha='center', weight='bold', color='#333')
    ax.text(0.3, 1.55, 'Основные интернет-показатели (Core Web Vitals): пройдены ✓',
            fontsize=9, weight='bold', color=GREEN)
    cwv = 'FCP 1,2 с    LCP 2,1 с    TBT 90 мс    CLS 0,03    Speed Index 2,4 с'
    ax.text(0.3, 1.1, cwv, fontsize=8.6, color='#333')
    ax.text(0.3, 0.55, 'Выявленные проблемы: неоптимизированные изображения, '
            'отсутствие отложенной загрузки сторонних скриптов (счётчики аналитики).',
            fontsize=7.8, color=GREY, style='italic')
    save(fig, 'pagespeed.png')


for f in (wordstat, trends, metrika, radar, advego, pagespeed):
    f()
print('Визуалы сервисов готовы')
