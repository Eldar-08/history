import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import HistoricalPeriod, HistoricalFact

# Create periods
stone, _ = HistoricalPeriod.objects.get_or_create(
    name='stone',
    defaults={
        'start_year': -3000000,
        'end_year': -3000,
        'description': 'Период доисторических охотников-собирателей. Люди жили в пещерах и создавали первые орудия труда из камня.'
    }
)

bronze, _ = HistoricalPeriod.objects.get_or_create(
    name='bronze',
    defaults={
        'start_year': -3000,
        'end_year': -1200,
        'description': 'Эпоха развития земледелия и скотоводства. Появление первых городов и письменности на территории Центральной Азии.'
    }
)

iron, _ = HistoricalPeriod.objects.get_or_create(
    name='iron',
    defaults={
        'start_year': -1200,
        'end_year': 500,
        'description': 'Век железа и развития кочевых цивилизаций. Расцвет скифской культуры.'
    }
)

medieval, _ = HistoricalPeriod.objects.get_or_create(
    name='medieval',
    defaults={
        'start_year': 500,
        'end_year': 1500,
        'description': 'Эпоха тюркских каганатов и монгольского завоевания. Развитие Великого Шёлкового пути.'
    }
)

modern, _ = HistoricalPeriod.objects.get_or_create(
    name='modern',
    defaults={
        'start_year': 1500,
        'end_year': None,
        'description': 'Новое время. Кыргызстан в составе Российской империи и Советского Союза.'
    }
)

# Create facts for stone age
facts_data = [
    {
        'title': 'Появление человека в регионе',
        'description': 'Археологические находки указывают на обитание человека в современных границах Кыргызстана уже в каменном веке. Около озера Иссык-Куль найдены стоянки древних охотников.',
        'period': stone,
        'year': -1500000
    },
    {
        'title': 'Развитие охотничьего мастерства',
        'description': 'В каменном веке люди на территории современного Кыргызстана охотились на мамонтов, оленей и диких лошадей. Они создавали орудия из кремня и костей животных.',
        'period': stone,
        'year': -50000
    },
    {
        'title': 'Переход к земледелию',
        'description': 'Примерно 10 000 лет назад начался переход от охоты к земледелию и скотоводству. Этот период назвают неолитической революцией.',
        'period': bronze,
        'year': -8000
    },
    {
        'title': 'Развитие цивилизации в долинах',
        'description': 'В бронзовом веке в долинах рек развивались первые поселения. Люди строили дома, создавали керамику и развивали торговлю.',
        'period': bronze,
        'year': -2000
    },
    {
        'title': 'Скифские кочевники',
        'description': 'В железном веке территорию населяли скифские и сакские племена - кочевники, известные своим боевым мастерством и красивой культурой.',
        'period': iron,
        'year': -700
    },
    {
        'title': 'Великий Шёлковый путь',
        'description': 'В средние века Кыргызстан находился на перекрёстке великих торговых маршрутов. Через его территорию проходили караваны с товарами из Китая, Индии и Персии.',
        'period': medieval,
        'year': 100
    },
    {
        'title': 'Тюркские каганаты',
        'description': 'Тюркские народы создали мощные каганаты, которые контролировали Центральную Азию и торговлю по Шёлковому пути.',
        'period': medieval,
        'year': 552
    },
    {
        'title': 'Монгольское завоевание',
        'description': 'В начале XIII века земли современного Кыргызстана были завоёваны войсками Чингисхана. Это оказало значительное влияние на культуру и политику региона.',
        'period': medieval,
        'year': 1219
    },
    {
        'title': 'Исламизация',
        'description': 'В период средневековья ислам постепенно стал основной религией на территории Кыргызстана, принесённый торговцами и завоевателями.',
        'period': medieval,
        'year': 1000
    },
    {
        'title': 'Присоединение к Российской империи',
        'description': 'В XIX веке Кыргызстан был присоединён к Российской империи. Это привело к значительным политическим и социальным изменениям.',
        'period': modern,
        'year': 1876
    },
]

for fact_data in facts_data:
    HistoricalFact.objects.get_or_create(
        title=fact_data['title'],
        defaults={
            'description': fact_data['description'],
            'period': fact_data['period'],
            'year': fact_data['year']
        }
    )

print("✅ Все данные успешно добавлены!")
print(f"Периодов: {HistoricalPeriod.objects.count()}")
print(f"Фактов: {HistoricalFact.objects.count()}")
