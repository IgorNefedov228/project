import random

# Шаг 1: Создание словаря
dictionary = {
   "Куриное филе с лимоном и зеленью": (34, 280),
    "Тушеная капуста с курицей": (28, 300),
    "Фаршированные цукини с овощами": (15, 250),
    "Рыба, запеченная с лимоном и укропом": (28, 320),
    "Салат из свежих овощей с оливковым маслом": (4, 200),
    "Гречневая каша с грибами": (10, 320),
    "Овощной рагу с курицей и нутом": (30, 400),
    "Запеченные баклажаны с томатами и сыром фета": (12, 350),
    "Тушеная индейка с цветной капустой": (28, 300),
    "Суп из шпината с куриным филе": (20, 250),
    "Куриные бедра, запеченные с картофелем и морковью": (35, 450),
    "Салат с тунцом и фасолью": (30, 400),
    "Овощное рагу с чечевицей и томатами": (15, 350),
    "Лосось на гриле с лимонным соусом": (30, 400),
    "Запеченные перцы с фаршем и рисом": (25, 380),
    "Куриный салат с яблоком и орехами": (28, 350),
    "Овощной суп с чечевицей и зеленью": (15, 250),
    "Индейка, тушеная с брокколи и морковью": (28, 300),
    "Киноа с запеченными овощами и фетой": (12, 350),
    "Суп-пюре из тыквы с имбирем и кокосовым молоком": (4, 250),
    "Куриные котлеты на пару с картофельным пюре из цветной капусты": (25, 300),
    "Рыбные тефтели в томатном соусе с гарниром из гречки": (30, 350),
    "Запеченные овощи с бобами и специями": (12, 300),
    "Салат из капусты с морковью и курицей": (20, 250),
    "Гречневая каша с тушеными овощами и курицей": (30, 400),
    "Курица, запеченная в духовке со специями и лимоном": (32, 370),
    "Овощной рагу с индейкой и сладким картофелем": (28, 400),
    "Чечевичный суп со шпинатом и морковью": (15, 250),
    "Фаршированные помидоры с рисом и куриным фаршем": (25, 400),
    "Суп-пюре из моркови и картофеля": (4, 200),
    "Лосось, запеченный со специями": (30, 350),
    "Овощное рагу со сладким картофелем и нутом": (15, 400),
    "Запеченные кабачки с фаршем и помидорами": (20, 350),
    "Суп из брокколи с куриным филе": (25, 300),
    "Куриные шашлычки с овощами на гриле": (30, 400),
    "Паста из цельнозерновой муки с томатным соусом и овощами": (12, 350),
    "Овощной салат с киноа и лимонной заправкой": (10, 300),
    "Куриный бульон с лапшой из цельнозерновой муки": (20, 250),
    "Гречка с жареными грибами и луком": (10, 320),
    "Суп из чечевицы со специями и зеленью": (15, 250),
    "Фаршированные цукини с куриным фаршем": (20, 300),
    "Овощной салат с тунцом и оливковым маслом": (25, 350),
    "Запеченная рыба со сладким картофелем": (30, 400),
    "Тушеная капуста с говядиной": (28, 350),
    "Овсянка на молоке с ягодами": (10, 350),
    "Куриные крылышки в медовой глазури": (28, 400),
    "Запеченные перцы, фаршированные рисом": (8, 350),
    "Чечевичный суп со специями": (15, 250),
    "Куриный бульон с лапшой": (20, 150),
    "Киноа с тушеными овощами": (12, 300),
    "Рыбные котлеты на пару": (25, 300),
    "Овощной салат с курицей": (30, 350),
    "Паста из цельнозерновой муки с томатным соусом": (12, 350),
    "Чечевичный суп с помидорами": (15, 250),
    "Гречневая каша с грибами": (10, 320),
    "Запеченные баклажаны со специями": (6, 300),
    "Индейка, запеченная со специями": (32, 370),
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
    "Стейк из индейки на гриле с салатом": (32, 350),
    "Чили кон карне на основе индейки": (30, 400),
    "Ризотто с грибами и шпинатом": (12, 350),
    "Запеканка из цветной капусты и куриного фарша": (25, 300),
    "Суп из кабачков и картофеля": (6, 220),
    "Куриные наггетсы в панировке из овсянки": (28, 350),
    "Теплый салат из киноа, шпината и орехов": (10, 300),
    "Запеченные овощи под сыром фета": (12, 320)

}

# Шаг 2: Получение случайного ключа и его значений
def get_random_entry(dictionary):
    # Выбор случайного ключа
    random_key = random.choice(list(dictionary.keys()))
    # Получение значений по ключу
    values = dictionary[random_key]
    
    return random_key, values[0], values[1]

# Пример использования
ldt, ldp, ldc = get_random_entry(dictionary)