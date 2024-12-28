import random


dictionary = {
    "Творожные шарики с зеленью": (20, 200),
    "Яблоко с арахисовым маслом": (6, 250),
    "Овсяные хлопья с йогуртом и ягодами": (10, 300),
    "Морковные палочки с хумусом": (5, 150),
    "Куриные рулетики с сыром": (30, 250),
    "Тосты с авокадо и помидорами": (8, 300),
    "Протеиновый коктейль с бананом": (25, 250),
    "Миндаль и сухофрукты": (6, 200),
    "Сырники из творога без сахара": (18, 220),
    "Кефир с семенами чиа": (8, 150),
    "Овощные чипсы из свеклы и моркови": (3, 180),
    "Запеченные яйца в авокадо": (12, 300),
    "Смузи из шпината и банана": (5, 200),
    "Творожный десерт с медом и орехами": (18, 250),
    "Греческий йогурт с медом и орехами": (20, 300),
    "Овсяные печенья с бананом и орехами": (5, 220),
    "Куриные фрикадельки с соусом терияки": (25, 280),
    "Салат из тунца с фасолью и овощами": (30, 350),
    "Яйцо всмятку с цельнозерновым хлебом": (12, 200),
    "Фрукты с йогуртом и мюсли": (8, 250),
    "Кукурузные палочки с сыром": (5, 150),
    "Протеиновые батончики домашнего приготовления": (20, 300),
    "Овощные роллы с лавашем и курицей": (20, 250),
    "Сырные палочки из моцареллы": (15, 200),
    "Фрукты с творогом и медом": (15, 220),
    "Чиа-пудинг с кокосовым молоком": (6, 180),
    "Бутерброд с куриным паштетом": (20, 250),
    "Яблочные дольки с миндальным маслом": (4, 230),
    "Коктейль из кефира и ягод": (8, 150),
    "Овсянка с ягодами и медом": (6, 200),
    "Морковный салат с орехами и изюмом": (3, 180),
    "Фаршированные яйца с авокадо": (12, 220),
    "Батончик мюсли с медом и орехами": (8, 300),
    "Протеиновый коктейль с ягодами": (25, 250),
    "Суп-пюре из гороха с крекерами": (10, 200),
    "Овощные кексы с сыром и зеленью": (8, 220),
    "Каша из пшена с ягодами и медом": (6, 240),
    "Запеченные яблоки с корицей и орехами": (2, 180),
    "Творожный крем с ягодами": (18, 220),
    "Чипсы из нори": (5, 100),
    "Сэндвич с индейкой и шпинатом": (25, 300),
    "Коктейль из миндаля и банана": (8, 250),
    "Овощной салат с тунцом": (30, 350),
    "Яйцо пашот на тосте": (12, 200),
    "Гречневые блины с творогом": (15, 240),
    "Творожный десерт с кокосом": (18, 220),
    "Смузи из манго и шпината": (4, 180),
    "Хлебцы с хумусом и огурцом": (6, 150),
    "Каша из киноа с овощами": (8, 200),
    "Протеиновый батончик без сахара": (20, 300),
    "Творожные кексы с ягодами": (18, 240),
    "Закуска из баклажанов под соусом тахини": (5, 200),
    "Яблочные чипсы в духовке": (1, 150),
    "Бутерброд с лососем и авокадо": (20, 300),
    "Фрукты в шоколаде": (3, 250),
    "Суп-пюре из шпината и картофеля": (6, 220),
    "Овсянка на воде с корицей": (5, 150),
    "Чиа-пудинг с ягодами": (6, 180),
    "Сырные лепешки на гриле": (15, 250),
    "Яйцо в мешочке на тосте": (12, 200),
    "Протеиновый коктейль со шпинатом": (25, 220),
    "Запеченные баклажаны с томатами": (4, 180),
    "Овощной салат с курицей и кунжутом": (28, 350),
    "Творожный десерт с шоколадом": (18, 250),
    "Яблоко, запеченное с корицей и медом": (1, 200),
    "Каша из гречки с молоком": (8, 220),
    "Хумус с морковными палочками": (5, 150),
    "Закуска из тунца на хлебцах": (20, 250),
    "Овсяные хлопья с кефиром и фруктами": (8, 200),
    "Фрукты в йогурте": (6, 180),
    "Каша из пшена на молоке": (7, 240),
    "Протеиновый коктейль с кокосовым молоком": (20, 250),
    "Овощной салат с оливковым маслом": (4, 200),
    "Яйцо, запеченное в перце": (12, 220),
    "Творожный десерт с орехами": (18, 240),
    "Закуска из сыра и винограда": (10, 200),
    "Овсянка на воде с фруктами": (5, 180),
    "Греческий йогурт с семенами чиа": (18, 220),
    "Бутерброд с куриным филе и огурцом": (25, 300),
    "Каша из киноа с овощами и яйцом": (10, 250),
    "Чипсы из сладкого картофеля": (2, 180),
    "Запеченные груши с медом и орехами": (2, 220),
    "Овощной смузи с авокадо и шпинатом": (5, 200),
    "Творожные кексы без сахара": (18, 240),
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
    "Овощной салат с курицей и кунжутом": (28, 350)

}


def get_random_entry(dictionary):
    
    random_key = random.choice(list(dictionary.keys()))
    
    values = dictionary[random_key]
    
    return random_key, values[0], values[1]


dst, dsp, dsc = get_random_entry(dictionary)
