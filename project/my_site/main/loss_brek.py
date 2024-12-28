import random

# Шаг 1: Создание словаря
dictionary = {
    "Омлет из яиц с шпинатом": (20, 250),
    "Гречневая каша на воде с яблоком": (10, 300),
    "Творожный салат с зеленью и помидорами": (25, 200),
    "Яблоко с корицей и грецкими орехами": (4, 250),
    "Салат из капусты с морковью и оливковым маслом": (3, 150),
    "Овсянка на воде с семенами льна": (8, 220),
    "Протеиновый коктейль с ягодами и шпинатом": (30, 300),
    "Блинчики из овсяной муки с медом": (10, 350),
    "Суп из чечевицы с овощами": (15, 250),
    "Каша из ячменя с тыквой и медом": (12, 320),
    "Яйцо всмятку с тостом из цельнозернового хлеба": (14, 280),
    "Творог с клубникой и медом": (25, 300),
    "Кукурузная каша с ягодами и орехами": (8, 350),
    "Запеченные яйца в авокадо": (18, 400),
    "Смузи из банана и шпината с миндальным молоком": (6, 250),
    "Хлебцы с хумусом и огурцом": (8, 200),
    "Пудинг из семян чиа с кокосовым молоком": (10, 300),
    "Суп-пюре из сладкого картофеля и имбиря": (4, 250),
    "Овсяные хлопья с йогуртом и фруктами": (12, 350),
    "Яйцо-пашот на салате из рукколы и помидоров": (18, 300),
    "Каша из киноа с грибами и шпинатом": (12, 320),
    "Бутерброд с куриным филе и авокадо": (30, 400),
    "Греческий йогурт с медом и грецкими орехами": (20, 350),
    "Фрукты с творогом и семенами чиа": (15, 250),
    "Суп из брокколи с куриным филе": (25, 300),
    "Овсянка на воде с ягодами и медом": (8, 280),
    "Запеченные овощи с курицей": (30, 400),
    "Творожные сырники без сахара": (25, 300),
    "Смузи из киви и шпината с йогуртом": (6, 200),
    "Яблочный салат с орехами и йогуртом": (5, 250),
    "Овсяные панкейки без муки с бананом": (10, 300),
    "Чечевичный салат с овощами": (20, 350),
    "Овощное рагу с курицей и сладким картофелем": (30, 450),
    "Овсянка с кокосовым молоком и манго": (8, 350),
    "Сырники из творога с ягодным соусом": (25, 400),
    "Протеиновый батончик с орехами и медом": (20, 300),
    "Запеченные перцы, фаршированные овощами": (8, 350),
    "Суп-пюре из цветной капусты": (6, 200),
    "Гречневая каша с куриным филе": (30, 400),
    "Бутерброд с лососем и авокадо": (35, 450),
    "Омлет с брокколи и помидорами": (20, 300),
    "Каша из риса с яблоками и корицей": (6, 320),
    "Творожный десерт с ягодами": (20, 250),
    "Фаршированные кабачки с мясом и овощами": (25, 400),
    "Смузи из манго и шпината": (4, 200),
    "Яйцо-скрамбл с помидорами и шпинатом": (14, 280),
    "Овощной салат с тунцом и оливковым маслом": (25, 350),
    "Каша из пшена на воде с фруктами": (10, 300),
    "Протеиновый коктейль с бананом и шпинатом": (20, 250),
    "Блинчики из гречневой муки с ягодами": (12, 300),
    "Овсянка на воде с тыквой и корицей": (8, 280),
    "Запеченная цветная капуста со специями": (5, 200),
    "Тосты из цельнозернового хлеба с хумусом": (8, 250),
    "Суп-пюре из тыквы с имбирем": (4, 220),
    "Овсяные хлопья с бананом и корицей": (8, 300),
    "Сырники из творога без сахара": (25, 350),
    "Протеиновый смузи с ягодами и шпинатом": (20, 250),
    "Яйцо-пашот на тосте из ржаного хлеба": (14, 280),
    "Овощной салат с киноа и лимонным соком": (10, 300),
    "Чиа-пудинг на кокосовом молоке": (10, 350),
    "Гречка со сливками и зеленью": (14, 400),
    "Запеченные яйца в перце": (20, 300),
    "Суп-пюре из моркови и картофеля": (4, 200),
    "Омлет со сладким картофелем и шпинатом": (20, 350),
    "Яблочный салат с орехами и йогуртом": (5, 250),
    "Овсянка на воде с грушей и корицей": (8, 280),
    "Творожный десерт со свежими ягодами": (25, 300),
    "Фаршированные яйца тунцом": (20, 300),
    "Запеченные овощи в духовке": (5, 200),
    "Смузи из киви, шпината и йогурта": (6, 200),
    "Блинчики из овсяной муки с яблоком": (12, 300),
    "Суп-пюре из брокколи и картофеля": (6, 250),
    "Чиа-пудинг на миндальном молоке": (10, 350),
    "Овсянка на молоке со свежими фруктами": (10, 350),
    "Суп из чечевицы со специями": (15, 250),
    "Гречка со сливочным маслом": (14, 400),
    "Яйцо-скрамбл на тосте": (14, 280),
    "Овощные палочки с гуакамоле": (4, 250),
    "Протеиновый шейк со спирулиной": (18, 200),
    "Овощное рагу со сладким картофелем": (8, 400),
    "Яблочный пирог на овсяной основе": (6, 350),
    "Творожный десерт со сметаной": (25, 300),
    "Шоколадный протеиновый шейк": (28, 350),
    "Бутерброд с авокадо, яйцом и зеленью": (18, 450),
    "Гречневая каша со сливочным маслом": (14, 400),
    "Кукурузные чипсы с гуакамоле": (6, 300),
    "Овсяные лепешки с семенами чиа": (8, 250),
    "Суп-пюре из моркови и имбиря": (4, 200),
    "Протеиновый батончик без сахара": (20, 250),
    "Запеченные перцы, фаршированные рисом": (8, 350),
    "Каша из киноа с орехами": (12, 320),
    "Фрукты в йогурте": (6, 200),
    "Яйцо-скрамбл на тосте": (14, 280),
    "Овощные палочки с гуакамоле": (4, 250),
    "Протеиновый шейк со спирулиной": (18, 200),
    "Творожный десерт со свежими ягодами": (25, 300),
    "Чиа-пудинг на миндальном молоке": (10, 350),
    "Запеченные картофельные дольки со специями": (6, 400),
    "Смузи из ананаса, шпината и кефира": (6, 200),
    "Овсяные панкейки с бананом": (12, 400)

}

# Шаг 2: Получение случайного ключа и его значений
def get_random_entry(dictionary):
    # Выбор случайного ключа
    random_key = random.choice(list(dictionary.keys()))
    # Получение значений по ключу
    values = dictionary[random_key]
    
    return random_key, values[0], values[1]

# Пример использования
lbt, lbp, lbc = get_random_entry(dictionary)