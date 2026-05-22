# -*- coding: utf-8 -*-
"""Концептуальные диаграммы: мозговой штурм, SWOT, персона, CJM, Impact map, UML."""
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse, FancyArrowPatch, Circle, Arc

plt.rcParams['font.family'] = 'DejaVu Sans'
A = '/home/user/kirill-univer/work/assets/'
NAVY, BLUE = '#1F4E78', '#2E75B6'
P1, P2, P3 = '#2E75B6', '#548235', '#ED7D31'
GREEN, RED, YELLOW, GREY = '#548235', '#C00000', '#FFC000', '#7F7F7F'


def save(fig, name):
    fig.savefig(A + name, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('  ', name)


def w(text, width):
    return '\n'.join(textwrap.fill(p, width) for p in text.split('\n'))


def card(ax, x, y, cw, h, text, fc, tc='white', fs=8.0, ec='none', bold=False, wrapw=None):
    ax.add_patch(FancyBboxPatch((x, y), cw, h, boxstyle='round,pad=0.01,rounding_size=0.06',
                                fc=fc, ec=ec, lw=1.4, zorder=3))
    t = w(text, wrapw) if wrapw else text
    ax.text(x + cw / 2, y + h / 2, t, ha='center', va='center', fontsize=fs,
            color=tc, zorder=4, weight='bold' if bold else 'normal')


def smiley(ax, x, y, r, mood):
    col = {'bad': '#E06666', 'mid': '#FFD966', 'good': '#93C47D'}[mood]
    ax.add_patch(Circle((x, y), r, fc=col, ec='#333', lw=1.5, zorder=6))
    ax.add_patch(Circle((x - r * 0.35, y + r * 0.28), r * 0.13, fc='#333', zorder=7))
    ax.add_patch(Circle((x + r * 0.35, y + r * 0.28), r * 0.13, fc='#333', zorder=7))
    if mood == 'good':
        ax.add_patch(Arc((x, y - r * 0.05), r * 1.0, r * 0.9, theta1=200, theta2=340,
                         lw=2.2, color='#333', zorder=7))
    elif mood == 'bad':
        ax.add_patch(Arc((x, y - r * 0.5), r * 1.0, r * 0.9, theta1=20, theta2=160,
                         lw=2.2, color='#333', zorder=7))
    else:
        ax.plot([x - r * 0.4, x + r * 0.4], [y - r * 0.32, y - r * 0.32],
                lw=2.2, color='#333', zorder=7)


# ============ МОЗГОВОЙ ШТУРМ 6-3-5 ============
def brainstorm():
    fig, ax = plt.subplots(figsize=(14.5, 9))
    ax.set_xlim(0, 14.5); ax.set_ylim(0, 9.5); ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 14.5, 9.5, fc='#EEF3F8'))
    ax.add_patch(Rectangle((0, 8.5), 14.5, 1.0, fc=NAVY))
    ax.text(7.25, 9.08, 'МОЗГОВОЙ ШТУРМ (метод 6–3–5)', ha='center', fontsize=15,
            color='white', weight='bold')
    ax.text(7.25, 8.66, w('Тема: модификация ИС управления поставщиками — '
            'модуль аттестации и оценки надёжности поставщиков', 95),
            ha='center', fontsize=9, color='white')
    ax.text(7.25, 8.2, 'Дата: 12.05.2026   |   Вариант № 7   |   Команда: '
            '[ФИО студента], [Член команды 2], [Член команды 3]',
            ha='center', fontsize=8.8, color=NAVY, weight='bold')
    parts = [('Участник 1: [ФИО студента]', P1,
              ['Идея 1.1. Автоматическое формирование графика аттестации '
               'поставщиков по категориям риска',
               'Идея 1.2. Расчёт интегрального рейтинга надёжности '
               'контрагента (от 0 до 100 баллов)',
               'Идея 1.3. «Светофор» поставщиков: зелёный / жёлтый / '
               'красный уровень доверия']),
             ('Участник 2: [Член команды 2]', P2,
              ['Идея 2.1. Сбор аттестационных анкет от поставщиков '
               'через защищённый личный кабинет',
               'Идея 2.2. Автоподбор оптимальных поставщиков под '
               'параметры конкретной закупки',
               'Идея 2.3. Уведомления о просроченной и предстоящей '
               'аттестации поставщиков']),
             ('Участник 3: [Член команды 3]', P3,
              ['Идея 3.1. Интеграция рейтинга надёжности с проверкой '
               'контрагента по ФНС / ЕГРЮЛ',
               'Идея 3.2. Дашборд руководителя с динамикой надёжности '
               'пула поставщиков',
               'Идея 3.3. Автоблокировка закупок у поставщиков с '
               'критически низким рейтингом'])]
    for i, (name, col, ideas) in enumerate(parts):
        x = 0.35 + i * 4.75
        card(ax, x, 7.55, 4.4, 0.62, name, col, bold=True, fs=9.3)
        for j, idea in enumerate(ideas):
            card(ax, x, 5.5 - j * 1.6, 4.4, 1.4, idea, col, fs=7.8, wrapw=40)
    ax.text(7.25, 1.62, 'УЛУЧШЕНИЕ ЧУЖИХ ИДЕЙ (по 1 на участника; цвет = цвет автора улучшения)',
            ha='center', fontsize=9.2, weight='bold', color=NAVY)
    impr = [('[ФИО студента] → идея 2.2: добавить ML-ранжирование '
             'поставщиков с учётом истории срывов поставок', P1),
            ('[Член команды 2] → идея 3.1: автопроверка по реестру '
             'недобросовестных поставщиков и судебной картотеке', P2),
            ('[Член команды 3] → идея 1.1: привязать частоту аттестации '
             'к категории закупки (ABC/XYZ) и сумме контракта', P3)]
    for i, (txt, col) in enumerate(impr):
        x = 0.35 + i * 4.75
        ax.add_patch(FancyBboxPatch((x, 0.3), 4.4, 1.15,
                     boxstyle='round,pad=0.01,rounding_size=0.06', fc='white', ec=col, lw=2.6))
        ax.text(x + 2.2, 0.88, w(txt, 46), ha='center', va='center', fontsize=7.4, color='#222')
    save(fig, 'brainstorm.png')


# ============ SWOT ============
def swot():
    fig, ax = plt.subplots(figsize=(13, 9))
    ax.set_xlim(0, 13); ax.set_ylim(0, 9.2); ax.axis('off')
    ax.add_patch(Rectangle((0, 8.5), 13, 0.7, fc=NAVY))
    ax.text(6.5, 8.85, w('SWOT-анализ компании «НОРБИТ»  |  Дата: 14.05.2026  |  '
            'Вариант № 7  |  Команда: [ФИО студента], [Член команды 2], [Член команды 3]', 110),
            ha='center', va='center', fontsize=8.6, color='white', weight='bold')
    quad = [
        (0.3, 4.45, P1, 'S — Сильные стороны (Strengths)',
         ['1. Входит в ГК ЛАНИТ — мощная экспертиза, ресурсы и репутация',
          '2. Большой опыт корпоративных внедрений, универсальность решений',
          '3. Высокая производительность платформы и отраслевая экспертиза']),
        (6.6, 4.45, RED, 'W — Слабые стороны (Weaknesses)',
         ['1. Отставание SRM по функционалу аттестации поставщиков',
          '2. Низкий уровень кастомизации без программирования',
          '3. Слабая узнаваемость суббренда SRM, низкая рекламная активность']),
        (0.3, 0.3, GREEN, 'O — Возможности (Opportunities)',
         ['1. Импортозамещение: уход SAP/Oracle освобождает рынок SRM',
          '2. Рост требований к надёжности поставщиков и комплаенсу',
          '3. Господдержка отечественного ПО, реестр российского ПО']),
        (6.6, 0.3, ORANGE_T := '#ED7D31', 'T — Угрозы (Threats)',
         ['1. Усиление конкуренции (1С, Comindware, Bidzaar, AGORA)',
          '2. Дефицит ИТ-кадров и рост стоимости разработки',
          '3. Экономическая нестабильность, сокращение ИТ-бюджетов заказчиков'])]
    pcols = [P1, P2, P3]
    for x, y, col, title, items in quad:
        ax.add_patch(FancyBboxPatch((x, y), 6.1, 3.9, boxstyle='round,pad=0.02,rounding_size=0.08',
                     fc='white', ec=col, lw=2.6))
        ax.add_patch(FancyBboxPatch((x, y + 3.25), 6.1, 0.65,
                     boxstyle='round,pad=0.02,rounding_size=0.08', fc=col, ec=col))
        ax.text(x + 3.05, y + 3.57, title, ha='center', va='center', fontsize=10.5,
                color='white', weight='bold')
        for j, it in enumerate(items):
            ax.add_patch(FancyBboxPatch((x + 0.2, y + 2.32 - j * 0.94), 5.7, 0.8,
                         boxstyle='round,pad=0.01,rounding_size=0.05', fc=pcols[j], ec='none'))
            ax.text(x + 3.05, y + 2.72 - j * 0.94, w(it, 52), ha='center', va='center',
                    fontsize=7.7, color='white')
    ax.text(6.5, 0.06, 'Цвет фактора соответствует участнику команды: '
            'синий — [ФИО студента], зелёный — [Член команды 2], оранжевый — [Член команды 3]',
            ha='center', fontsize=7.3, color=GREY, style='italic')
    save(fig, 'swot.png')


# ============ ПОРТРЕТ КЛИЕНТА B2B ============
def persona():
    fig, ax = plt.subplots(figsize=(13.5, 8.8))
    ax.set_xlim(0, 13.5); ax.set_ylim(0, 8.8); ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 13.5, 8.8, fc='#EEF3F8'))
    ax.add_patch(Rectangle((0, 7.9), 13.5, 0.9, fc=NAVY))
    ax.text(6.75, 8.35, 'ПОРТРЕТ ЦЕЛЕВОГО КЛИЕНТА B2B  |  Вариант № 7  |  Команда: '
            '[ФИО студента], [Член команды 2], [Член команды 3]',
            ha='center', va='center', fontsize=9, color='white', weight='bold')
    ax.add_patch(FancyBboxPatch((0.3, 0.3), 3.9, 7.25, boxstyle='round,pad=0.02,rounding_size=0.1',
                 fc='white', ec=NAVY, lw=2))
    # иконка компании
    ax.add_patch(Circle((2.25, 6.35), 1.0, fc='#D6E4F0', ec=NAVY, lw=2))
    ax.add_patch(Rectangle((1.85, 6.0), 0.8, 0.85, fc=NAVY))
    for r in range(3):
        for c in range(2):
            ax.add_patch(Rectangle((1.95 + c * 0.35, 6.12 + r * 0.22), 0.16, 0.13, fc='white'))
    ax.text(2.25, 4.95, 'Целевой клиент — компания', ha='center', fontsize=10.5,
            weight='bold', color=NAVY)
    ax.text(2.25, 4.6, 'ООО «ПромТоргСнаб»', ha='center', fontsize=10, color='#333')
    info = ['ЛПР: директор по закупкам',
            'Отрасль: производство, ритейл,', 'оптовая дистрибуция',
            'Размер: 500–5000 сотрудников',
            'География: РФ, города-миллионники',
            'Бюджет внедрения: 1–5 млн руб.']
    for j, t in enumerate(info):
        ax.text(0.55, 4.05 - j * 0.5, '• ' + t, ha='left', fontsize=8.5, color='#222')
    blocks = [
        (4.5, 4.1, P1, 'Цели и ценности',
         ['Снизить риски и срывы поставок',
          'Выбирать только надёжных поставщиков',
          'Автоматизировать аттестацию контрагентов',
          'Ценности: надёжность, прозрачность,',
          'экономия времени, управляемость закупок']),
        (9.0, 4.1, RED, 'Боли и сложности',
         ['Финансы: убытки от срыва поставок',
          'Техника: оценка поставщиков вручную в Excel',
          'Эффективность: нет единого рейтинга надёжности',
          'Процесс покупки: долгий выбор поставщика',
          'Поддержка: риск работы с недобросовестным']),
        (4.5, 0.45, GREEN, 'Покупательское поведение',
         ['Покупает: ERP-, SRM-, WMS-системы, ЭДО',
          'Предпочитает отечественных вендоров',
          'из реестра российского ПО (1С, Контур)',
          'Частота закупок ИС: 1–2 крупных',
          'проекта внедрения за 2–3 года']),
        (9.0, 0.45, '#ED7D31', 'Каналы и ограничения',
         ['Каналы: отраслевые конференции,',
          'тендерные площадки, ИТ-порталы,',
          'вебинары вендоров, рекомендации',
          'Ограничения: импортозамещение,',
          'дефицит ИТ-специалистов у заказчика'])]
    for x, y, col, title, items in blocks:
        ax.add_patch(FancyBboxPatch((x, y), 4.2, 3.2, boxstyle='round,pad=0.02,rounding_size=0.08',
                     fc='white', ec=col, lw=2))
        ax.add_patch(FancyBboxPatch((x, y + 2.62), 4.2, 0.58,
                     boxstyle='round,pad=0.02,rounding_size=0.08', fc=col, ec=col))
        ax.text(x + 2.1, y + 2.9, title, ha='center', va='center', fontsize=9.8,
                color='white', weight='bold')
        for j, it in enumerate(items):
            ax.text(x + 0.18, y + 2.25 - j * 0.42, it, ha='left', fontsize=7.7, color='#222')
    save(fig, 'persona.png')


# ============ CUSTOMER JOURNEY MAP ============
def cjm():
    stages = ['1. Осознание\nпотребности', '2. Поиск\nрешения', '3. Выбор и\nдоговор',
              '4. Внедрение', '5. Использование\nи поддержка',
              '6. Развитие /\nповторная покупка']
    actions = ['Фиксирует срывы поставок, ищет способ снизить риски закупок',
               'Изучает сайты вендоров SRM, читает обзоры, отзывы и кейсы',
               'Запрашивает КП, сравнивает, ведёт переговоры, подписывает договор',
               'Установка системы, настройка регламентов аттестации, обучение',
               'Проводит аттестацию, смотрит рейтинги, обращается в поддержку',
               'Оценивает эффект, продлевает лицензию, покупает доп. модули']
    touch = ['Сайт, отраслевые СМИ, конференции',
             'Сайт, вебинары, демо, отзывы',
             'Менеджер, КП, презентация, договор',
             'Команда внедрения, обучение, документация',
             'Личный кабинет, техподдержка, дашборд',
             'Аккаунт-менеджер, обновления, биллинг']
    pains = ['Не осознаёт масштаб потерь от срывов',
             'Много вендоров, сложно сравнить',
             'Долгое согласование, непрозрачная цена',
             'Сложная настройка, сопротивление персонала',
             'Долгий ответ техподдержки',
             'Барьеров нет — клиент доволен']
    opps = ['Контент о рисках закупок, калькулятор потерь',
            'SEO, понятное демо модуля аттестации',
            'Прозрачные тарифы, быстрое КП',
            'Шаблоны регламентов, онбординг «под ключ»',
            'SLA поддержки, база знаний',
            'Программа лояльности, дорожная карта']
    moods = ['bad', 'mid', 'mid', 'bad', 'good', 'good']
    emo = [1.8, 3.0, 2.6, 1.9, 3.6, 4.4]
    fig, ax = plt.subplots(figsize=(16.5, 9))
    ax.set_xlim(-1.6, 16.5); ax.set_ylim(0, 9.3); ax.axis('off')
    n = 6
    cw = 18.1 / n
    x0 = -1.6
    ax.add_patch(Rectangle((x0, 8.55), 18.1, 0.7, fc=NAVY))
    ax.text(x0 + 9.05, 8.9, w('CUSTOMER JOURNEY MAP — путь клиента ИС управления '
            'поставщиками  |  Вариант № 7  |  [ФИО студента], [Член команды 2], '
            '[Член команды 3]', 130), ha='center', va='center', fontsize=8.4,
            color='white', weight='bold')
    rows = [('Этап', stages, NAVY, 'white', 0.7, 26),
            ('Действия\nклиента', actions, '#DAE3F3', '#222', 1.35, 24),
            ('Точки\nконтакта', touch, '#E2EFDA', '#222', 1.1, 24),
            ('Барьеры', pains, '#FBE5E5', '#222', 1.05, 24),
            ('Возможности', opps, '#FFF2CC', '#222', 1.1, 24)]
    ytop = 8.45
    y = ytop
    for label, vals, fc, tc, rh, wr in rows:
        y -= rh
        ax.text(x0 - 0.05, y + rh / 2, label, ha='right', va='center', fontsize=8.4,
                weight='bold', color=NAVY)
        for ci in range(n):
            x = x0 + ci * cw
            ax.add_patch(Rectangle((x + 0.05, y + 0.05), cw - 0.1, rh - 0.1,
                         fc=fc, ec='white', lw=2))
            ax.text(x + cw / 2, y + rh / 2, w(vals[ci], wr) if label != 'Этап' else vals[ci],
                    ha='center', va='center', fontsize=7.5,
                    color=tc, weight='bold' if label == 'Этап' else 'normal')
    # эмоции
    ey0, eh = 0.5, 2.3
    ax.text(x0 - 0.05, ey0 + eh / 2, 'Эмоции\nклиента', ha='right', va='center',
            fontsize=8.4, weight='bold', color=NAVY)
    ax.add_patch(Rectangle((x0, ey0), 18.1, eh, fc='#F4F6FA', ec='white', lw=2))
    xs = [x0 + ci * cw + cw / 2 for ci in range(n)]
    ey = [ey0 + 0.55 + (e - 1) / 4 * (eh - 1.1) for e in emo]
    ax.plot(xs, ey, '-', color=NAVY, lw=3, zorder=4)
    for ci in range(n):
        smiley(ax, xs[ci], ey[ci], 0.34, moods[ci])
    save(fig, 'cjm.png')


# ============ IMPACT MAPPING ============
def impact_map():
    fig, ax = plt.subplots(figsize=(15.5, 8.8))
    ax.set_xlim(0, 15.5); ax.set_ylim(0, 8.8); ax.axis('off')
    ax.text(7.75, 8.5, w('Impact Mapping (карта влияния) — модуль «SRM.Аттестация»  |  '
            'Вариант № 7  |  Команда: [ФИО студента], [Член команды 2], [Член команды 3]', 120),
            ha='center', fontsize=9, weight='bold', color=NAVY)
    for x, lab in [(1.6, 'WHY — Цель'), (4.85, 'WHO — Акторы'),
                   (8.05, 'HOW — Влияния'), (11.7, 'WHAT — Функционал')]:
        ax.text(x, 7.75, lab, ha='center', fontsize=9.5, weight='bold', color=NAVY)
        ax.plot([x - 1.35, x + 1.35], [7.55, 7.55], color=NAVY, lw=1)
    card(ax, 0.2, 3.5, 2.8, 1.9,
         'ЦЕЛЬ (Why): за 12 мес. после запуска модуля снизить срывы поставок '
         'у клиентов на 25 % и увеличить выручку SRM-направления на 20 %',
         NAVY, fs=7.6, bold=True, wrapw=26)
    actors = [('АКТОР: Менеджер по закупкам', P2, 5.65),
              ('АКТОР: Директор по закупкам', P3, 1.75)]
    impacts = ['ВЛИЯНИЕ: проводит аттестацию поставщиков регулярно и строго по графику',
               'ВЛИЯНИЕ: принимает решения о пуле поставщиков на основе рейтинга надёжности']
    delivers = [['Составить график аттестации поставщиков',
                 'Заполнить аттестационную анкету поставщика',
                 'Зафиксировать результаты аттестации'],
                ['Просмотреть рейтинг надёжности поставщиков',
                 'Сформировать отчёт по пулу поставщиков',
                 'Выбрать оптимального поставщика']]
    for ai, (atext, acol, ay) in enumerate(actors):
        card(ax, 3.5, ay, 2.5, 1.5, atext, acol, fs=8.0, bold=True, wrapw=22)
        ax.add_patch(FancyArrowPatch((3.0, 4.45), (3.5, ay + 0.75), arrowstyle='-|>',
                     mutation_scale=15, color=GREY, lw=1.6))
        iy = ay + 0.25
        card(ax, 6.5, iy, 3.0, 1.0, impacts[ai], '#8FAADC', fs=7.3, wrapw=34)
        ax.add_patch(FancyArrowPatch((6.0, ay + 0.75), (6.5, iy + 0.5), arrowstyle='-|>',
                     mutation_scale=14, color=GREY, lw=1.5))
        for di, dtext in enumerate(delivers[ai]):
            dy = ay + 1.15 - di * 0.95
            card(ax, 10.0, dy, 3.3, 0.8, dtext, '#A9D18E', tc='#1a1a1a', fs=7.2, wrapw=34)
            ax.add_patch(FancyArrowPatch((9.5, iy + 0.5), (10.0, dy + 0.4),
                         arrowstyle='-|>', mutation_scale=12, color=GREY, lw=1.2))
    save(fig, 'impact_map.png')


# ============ UML USE CASE ============
def usecase():
    fig, ax = plt.subplots(figsize=(13.5, 9))
    ax.set_xlim(0, 13.5); ax.set_ylim(0, 9); ax.axis('off')
    ax.text(6.75, 8.6, w('UML-диаграмма вариантов использования модуля '
            '«SRM.Аттестация» (Вариант № 7)', 90),
            ha='center', fontsize=10.5, weight='bold', color=NAVY)

    def actor(x, y, name):
        ax.add_patch(Circle((x, y + 0.5), 0.16, fc='white', ec='black', lw=1.6))
        ax.plot([x, x], [y + 0.34, y - 0.18], 'k', lw=1.6)
        ax.plot([x - 0.26, x + 0.26], [y + 0.16, y + 0.16], 'k', lw=1.6)
        ax.plot([x, x - 0.2], [y - 0.18, y - 0.52], 'k', lw=1.6)
        ax.plot([x, x + 0.2], [y - 0.18, y - 0.52], 'k', lw=1.6)
        ax.text(x, y - 0.95, name, ha='center', va='center', fontsize=8.3, weight='bold')

    actor(1.25, 6.0, 'Менеджер\nпо закупкам')
    actor(1.25, 2.6, 'Директор\nпо закупкам')
    actor(12.25, 4.3, 'Сервис\nФНС / ЕГРЮЛ')
    ax.add_patch(Rectangle((3.3, 0.6), 6.9, 7.3, fc='#F4F6FA', ec=NAVY, lw=2))
    ax.text(6.75, 7.55, 'Система «НОРБИТ: Управление закупками (SRM) 2.0»',
            ha='center', fontsize=9, weight='bold', color=NAVY)
    ucs = [(6.75, 6.7, 'Составить график\nаттестации поставщиков', [0]),
           (6.75, 5.45, 'Провести аттестацию\nпоставщика', [0]),
           (6.75, 4.2, 'Сформировать рейтинг\nнадёжности поставщика', []),
           (6.75, 2.95, 'Просмотреть рейтинг и\nотчёт по поставщикам', [1]),
           (6.75, 1.7, 'Выбрать оптимального\nпоставщика под закупку', [1])]
    for x, y, t, who in ucs:
        ax.add_patch(Ellipse((x, y), 3.7, 0.95, fc='#DAE3F3', ec=NAVY, lw=1.5))
        ax.text(x, y, t, ha='center', va='center', fontsize=7.9)
    for x, y, t, who in ucs:
        for ww in who:
            ay = 6.0 if ww == 0 else 2.6
            ax.plot([1.6, 4.9], [ay, y], color=GREY, lw=1.3, zorder=1)
    ax.plot([10.2, 11.85], [4.2, 4.3], color=GREY, lw=1.3)
    # include: аттестация -> рейтинг; рейтинг используется выбором
    for y1, y2 in [(5.45, 4.7), (2.95, 3.75)]:
        ax.annotate('', xy=(6.75, y2), xytext=(6.75, y1 - 0.45 if y1 > y2 else y1 + 0.45),
                    arrowprops=dict(arrowstyle='-|>', ls='--', color='#888', lw=1.3))
    ax.text(8.35, 4.95, '«include»', fontsize=7, style='italic', color='#888')
    ax.text(8.35, 3.5, '«include»', fontsize=7, style='italic', color='#888')
    save(fig, 'usecase.png')


for f in (brainstorm, swot, persona, cjm, impact_map, usecase):
    f()
print('Концептуальные диаграммы готовы')
