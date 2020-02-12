with open('recipes.txt', encoding='utf8') as f: # открываем файл в качестве объекта f
    raw_recipes = f.read()                  # сохранили содержимое объекта f в переменную raw_recipes
    list_raw_recipes = raw_recipes.split('\n\n') # разделили содержимое raw_recipes по блюдам в список, используем разделителем двойной переход на новую строку
cook_book = dict()                              # создали пустой словарь (для будущей записи туда содержимого нашего файла)
for element in list_raw_recipes:            # пробегаемся по списку наших данных
    data = element.split('\n')              # в переменную data записываем список строк, относящихся к блюду
    cook_book[data[0]] = list()             # создаем внутри словаря по блюду (ключ) пустой список (значение)
    for i in data[2:]:                      # пробегаемся по строкам, начиная с 3 (там ингридиенты)
        ingridient_name, quantity, measure = i.split(' | ') # в переменные записываем наши значения
        cook_book[data[0]].append({'ingridient_name':ingridient_name, # добавляем в качестве !значения! первого ключа (название блюда) список из словарей
                                   'quantity':int(quantity),
                                   'measure':measure})
# for k in cook_book:
#     print(k, cook_book[k])

def get_shop_list_by_dishes(dishes, person_count):
    ing = dict()            # создаем пустой целевой словарь
    for d in dishes:        # пробегаемся по введенным блюдам
        for i in cook_book[d]: # для каждого элемента нашего уже созданного словаря с рецептами по ключу d (блюдо)
            if i['ingridient_name'] in ing: # проверяем, встречался ли уже ингридиент в созданном целевом словаре
                ing[i['ingridient_name']]['quantity'] += i['quantity'] * person_count # к уже указанному количеству ингридиента добавляем новое
            else:
                ing[i['ingridient_name']] = {'measure': i['measure'], # если ингридиент встречается впервые, записываем его и его значение
                                             'quantity': i['quantity'] * person_count}
    return ing

result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for i in result.items():
    print(i)

