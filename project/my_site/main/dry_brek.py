import random

# Шаг 1: Создание словаря
dictionary = {
    "Овсянка с бананом": (10, 350),
    "Яичница с помидорами": (18, 250),
    "Тост с авокадо": (6, 300),
    "Гречневая каша с грибами": (12, 400),
    "Кефир с ягодами": (8, 150),
    "Блины с творогом": (20, 400),
    "Омлет с шпинатом": (15, 220),
    "Пшенная каша с тыквой": (10, 350),
    "Смузи из банана и шпината": (5, 200),
    "Творожная запеканка с изюмом": (18, 300),
    "Хлебцы с арахисовым маслом": (10, 250),
    "Каша из киноа с орехами": (15, 450),
    "Яблочный пирог с овсянкой": (8, 400),
    "Чиа-пудинг с кокосом": (8, 300),
    "Каша из риса с молоком": (7, 350),
    "Сырники с медом": (20, 400),
    "Греческий йогурт с медом и орехами": (15, 250),
    "Бутерброд с лососем и сливочным сыром": (20, 350),
    "Овсяные печенья с изюмом": (5, 200),
    "Фриттата с картошкой и луком": (12, 350),
    "Каша из кукурузной крупы с молоком": (8, 300),
    "Яйцо пашот на тосте": (14, 250),
    "Творог с медом и фруктами": (15, 200),
    "Овсянка с орехами и медом": (12, 400),
    "Бутерброд с авокадо и яйцом": (12, 300),
    "Запеченные яблоки с корицей": (1, 150),
    "Каша из перловой крупы": (10, 320),
    "Сырники из овсянки": (10, 250),
    "Яйца, запеченные в авокадо": (12, 300),
    "Гречневая каша с молоком": (12, 350),
    "Панкейки из овсяной муки": (10, 300),
    "Овощной салат с яйцом": (12, 200),
    "Каша из ячневой крупы": (9, 320),
    "Тосты с рикоттой и ягодами": (10, 250),
    "Каша из гречки с овощами": (12, 400),
    "Овсяные хлопья с молоком и фруктами": (10, 350),
    "Яйца в сметане": (14, 280),
    "Блинчики с яблоками": (8, 300),
    "Творожный мусс с ягодами": (15, 250),
    "Каша из овсянки с семенами чиа": (12, 350),
    "Суп-пюре из брокколи": (5, 180),
    "Яблочные оладьи": (6, 280),
    "Гречка с куриным филе": (30, 400),
    "Чашка мюсли с йогуртом": (15, 350),
    "Запеченные бананы с медом": (2, 200),
    "Овсяные хлопья с шоколадом": (10, 400),
    "Яйца, запеченные в томатах": (14, 250),
    "Смузи из манго и йогурта": (7, 220),
    "Творожные оладьи без муки": (20, 280),
    "Бутерброд с тунцом и огурцом": (22, 320),
    "Пшенная каша с медом и орехами": (10, 370),
    "Овощной омлет": (14, 220),
    "Тосты с хумусом и овощами": (9, 280),
    "Каша из кукурузной крупы с тыквой": (9, 350),
    "Яблочный смузи": (1, 150),
    "Яйца-бенедикт на английском маффине": (20, 400),
    "Овсянка с семенами льна": (12, 350),
    "Творожный десерт с ягодами": (18, 250),
    "Гречка с тушеными овощами": (10, 320),
    "Каша из риса с курицей и овощами": (25, 450),
    "Блины из гречневой муки": (10, 300),
    "Суп из чечевицы и овощей": (15, 250),
    "Яйцо всмятку на тосте": (12, 220),
    "Овощной салат с курицей и авокадо": (25, 350),
    "Панкейки из банана и овсянки": (8, 300),
    "Чиа-пудинг с ягодами и медом": (8, 300),
    "Запеканка из картофеля и сыра": (15, 400),
    "Овсянка со свежими фруктами и орехами": (12, 350),
    "Тосты с рикоттой и томатами": (10, 250),
    "Яйца, жаренные на оливковом масле": (14, 240),
    "Суп-пюре из цветной капусты": (5, 180),
    "Гречневая каша со сливочным маслом": (12, 350),
    "Каша из ячменя с медом": (9, 320),
    "Бутерброд с куриным паштетом": (20, 300),
    "Овощное рагу с яйцом": (12, 250),
    "Яблочные чипсы с корицей": (1, 150),
    "Овсянка со сгущенкой": (9, 400),
    "Блинчики из картофельного пюре": (6, 300),
    "Омлет с беконом и сыром": (25, 450),
    "Греческий йогурт с гранолой": (15, 350),
    "Сырники со сметаной": (20, 400),
    "Каша из пшена с яблоками": (8, 320),
    "Тосты с лососем и авокадо": (22, 400),
    "Овсянка на воде со специями": (8, 250),
    "Запеканка из творога и ягод": (18, 300),
    "Суп-пюре из тыквы и моркови": (4, 180),
    "Яйцо в хлебе (яйцо, запеченное в хлебе)": (13, 270),
    "Гречка со шпинатом": (12, 320),
    "Пшенная каша с молоком": (9, 340),
    "Чиа-пудинг с миндальным молоком": (8, 290),
    "Овсяные блинчики на воде": (7, 250),
    "Бутерброд со сливочным сыром и зеленью": (9, 280),
    "Фриттата с овощами": (14, 320),
    "Суп-пюре из чечевицы": (12, 220),
    "Яблочное пюре на завтрак": (1, 150),
    "Омлет со шпинатом и помидорами": (14, 240),
    "Овсянка со сгущенкой и орехами": (9, 400),
    "Блины из гречневой муки со сметаной": (12, 350),
    "Творожная запеканка без сахара": (20, 300),
    "Каша из ячменя на молоке": (10, 340)

}

# Шаг 2: Получение случайного ключа и его значений
def get_random_entry(dictionary):
    # Выбор случайного ключа
    random_key = random.choice(list(dictionary.keys()))
    # Получение значений по ключу
    values = dictionary[random_key]
    
    return random_key, values[0], values[1]

# Пример использования
dbt, dbp, dbc = get_random_entry(dictionary)