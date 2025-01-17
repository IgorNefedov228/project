import random


dictionary = {
    
    "Каша из овсяных хлопьев с бананом": (8, 300),
    "Творожная запеканка с яблоками": (20, 320),
    "Сэндвич с куриным филе и авокадо": (30, 400),
    "Яйцо пашот с лососем на цельнозерновом хлебе": (25, 350),
    "Гречневая каша с молоком и медом": (9, 270),
    "Овсяные хлопья с йогуртом и фруктами": (12, 320),
    "Блины с творогом и ягодами": (15, 330),
    "Омлет с шпинатом и сыром": (20, 300),
    "Каша из киноа с кокосовым молоком": (10, 280),
    "Творожные оладьи с изюмом": (18, 290),
    "Яблочный смузи с овсянкой и медом": (5, 250),
    "Запеченные яйца в авокадо с помидорами": (20, 360),
    "Овсянка с орехами и медом": (9, 310),
    "Бутерброд с индейкой и шпинатом": (26, 320),
    "Суп-пюре из тыквы с грецкими орехами": (6, 230),
    "Протеиновый коктейль с бананом и арахисовым маслом": (30, 400),
    "Овощной омлет с брокколи и сыром фета": (22, 320),
    "Творожный десерт с медом и орехами": (18, 280),
    "Каша из пшена с ягодами и медом": (7, 260),
    "Фриттата с картофелем и шпинатом": (18, 350),
    "Овсянка на воде с шоколадом и бананом": (7, 290),
    "Яйца, запеченные в перце с сыром": (20, 300),
    "Блинчики из овсяной муки с творогом": (18, 310),
    "Суп из чечевицы с овощами и яйцом": (15, 250),
    "Овощной салат с тунцом и яйцом": (30, 350),
    "Яйцо всмятку на тосте с авокадо": (12, 280),
    "Гречка с куриным филе и шпинатом": (30, 400),
    "Овсяные печенья с медом и орехами": (6, 250),
    "Творожные кексы с изюмом и орехами": (18, 290),
    "Каша из ячменя с медом и фруктами": (8, 260),
    "Запеченные овощи с яйцом и сыром": (15, 270),
    "Смузи из манго и йогурта": (8, 220),
    "Бутерброд с авокадо и семенами чиа": (10, 300),
    "Творожная запеканка с ягодами": (20, 280),
    "Овсянка на молоке с какао": (9, 310),
    "Яблоко, запеченное со специями и медом": (1, 240),
    "Чиа-пудинг с кокосовым молоком и ягодами": (6, 180),
    "Овсянка с кленовым сиропом и грецкими орехами": (8, 290),
    "Суп-пюре из цветной капусты с сыром": (6, 220),
    "Яйцо в мешочек на тосте с помидорами": (14, 240),
    "Гречка с грибами и луком": (10, 270),
    "Сырники из рикотты с медом": (18, 300),
    "Протеиновый батончик домашнего приготовления": (20, 300),
    "Овощной салат с курицей и кунжутом": (28, 350),
    "Каша из кукурузы с молоком и ягодами": (7, 250),
    "Блинчики с бананом и медом": (8, 300),
    "Овсянка на воде с корицей и яблоками": (5, 200),
    "Фруктовый салат с йогуртом и медом": (8, 220),
    "Яйцо, запеченное в томате": (12, 180),
    "Гречка с овощами и куриным филе": (30, 400),
    "Овсяные хлопья на воде с медом и орехами": (6, 220),
    "Запеченные груши с творогом и медом": (12, 240),
    "Суп-пюре из шпината и картофеля": (6, 220),
    "Чиа-пудинг со свежими фруктами": (6, 180),
    "Овощной салат с куриным филе": (28, 350),
    "Яйцо всмятку на тосте": (12, 200),
    "Блины из цельнозерновой муки с творогом": (18, 310),
    "Овсянка на молоке с ягодами": (9, 290),
    "Гречневая каша с овощами и яйцом": (15, 270),
    "Запеченные баклажаны с фаршем": (25, 350),
    "Творожный десерт с медом": (18, 240),
    "Овсянка на воде со свежими ягодами": (6, 200),
    "Яблочный пирог на овсяной основе": (5, 320),
    "Протеиновый коктейль со шпинатом": (25, 220),
    "Суп-пюре из брокколи с яйцом": (10, 220),
    "Овощные кексы со шпинатом и сыром": (10, 280),
    "Каша из ячменя на молоке": (8, 260),
    "Запеченные груши со специями": (1, 200),
    "Бутерброд с сыром и помидорами": (15, 300),
    "Яйцо в мешочке на тосте": (12, 200),
    "Овсянка на воде со свежими фруктами": (6, 200),
    "Каша из киноа с овощами": (10, 250),
    "Протеиновый батончик домашнего приготовления": (20, 300),
    "Суп-пюре из цветной капусты": (6, 220),
    "Овсянка на воде с ягодами": (6, 200),
    "Закуска из куриного филе на хлебцах": (20, 250),
    "Яблоко, запеченное со специями": (1, 200),
    "Суп-пюре из тыквы": (6, 220),
    "Овощной салат с тунцом": (30, 350),
    "Яйцо всмятку на тосте": (12, 200),
    "Фрукты в шоколаде": (3, 250),
    "Суп-пюре из шпината и картофеля": (6, 220),
    "Овсянка на воде с корицей": (5, 150),
    "Чиа-пудинг с ягодами": (6, 180),
    "Сырные лепешки на гриле": (15, 250),
    "Яйцо в мешочке на тосте": (12, 200),
    "Протеиновый коктейль со шпинатом": (25, 220),
    "Запеченные баклажаны с томатами": (4, 180),
    "Овощной салат с курицей и кунжутом": (28, 350),
    "Гречневая каша с овощами и яйцом": (15, 270),
    "Запеченные баклажаны с фаршем": (25, 350),
    "Творожный десерт с медом": (18, 240),
    "Овсянка на молоке с ягодами": (9, 290),
    "Гречка с грибами и луком": (10, 270),
    "Сырники из рикотты с медом": (18, 300),
    "Протеиновый батончик домашнего приготовления": (20, 300),
    "Овощной салат с курицей и кунжутом": (28, 350),
    "Яйцо всмятку на тосте": (12, 200),
    "Блины из цельнозерновой муки с творогом": (18, 310),
    "Овсянка на воде со свежими фруктами": (6, 200),

}

def get_random_entry(dictionary):

    random_key = random.choice(list(dictionary.keys()))

    values = dictionary[random_key]
    
    return random_key, values[0], values[1]

wbt, wbp, wbc = get_random_entry(dictionary)

print(wbt, wbp, wbc)