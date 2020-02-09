documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "98765"},
    {"type": "driving license", "number": "00000"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def get_person_by_doc(documents):  # 1 "p"
    doc = input('Введите номер документа: ')
    for document in documents:
        if document['number'] == doc:
            return document['name']
    return ('Нет такого документа')

def get_all_docs(documents):  # 2 "l"
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')

def get_shelf(directories):  # 3 "s"
    doc = input('Введите номер документа: ')
    for shelf in directories:
        if doc in directories[shelf]:
            return (f'Номер полки: {shelf}')
    return ('Нет такого документа')

def add_new_doc(documents, directories):  # 4 "a"
    new_number = input('Введите номер нового документа:')
    new_type = input('Введите тип нового документа: ')
    new_name = input('Введите имя: ')
    shelf_number = input('Введите номер полки: ')
    documents.append({"type": new_type, "number": new_number, "name": new_name})
    if shelf_number in directories:
        directories[shelf_number].append(new_number)
    else:
        directories[shelf_number] = [new_number]
    return documents, directories

def get_all_owners(documents):  # ЗАДАНИЕ К ЛЕКЦИИ 2.3 EXCEPTIONS  команда "all"
    for doc in documents:
        try:
            if doc['name']:
                print(doc['name'])
            else:
                print(f"У документа {doc['number']} введено пустое имя")
        except KeyError as e:
            print(f"У документа {doc['number']} нет поля 'имя'")

def delete_doc(documents, directories):  # 5 "d"
    number = input('Введите номер удаляемого документа:')
    not_deleted = True
    for item in documents:
        if number == item["number"]:
            documents.remove(item)
            print(f'Документ с номером {number} удален из каталога')
            not_deleted = False
            break
    if not_deleted:
        print("Документ в каталоге не найден")
    not_deleted = True

    for shelf in directories:
        if number in directories[shelf]:
            directories[shelf].remove(number)
            print(f'Документ с номером {number} удален с полки')
            not_deleted = False
            break
    if not_deleted:
        print("Документ на полке не найден")
    return documents, directories

def move_doc(documents, directories):  # 6 "m"
    target_doc = input('Введите номер перемещаемого документа:')
    target_shelf = input('Введите номер полки, на которую его следует переместить: ')
    not_moved = True
    for shelf in directories:
        if target_doc in directories[shelf]:
            directories[shelf].remove(target_doc)
            not_moved = False
            break
    if not_moved:
        print(f'Документ с номером {target_doc} не найден')
    else:
        if target_shelf in directories:
            directories[target_shelf].append(target_doc)
        else:
            directories[target_shelf] = [target_doc]
        print(f'Документ перемещен с полки {shelf} на полку {target_shelf}')
    return documents, directories

def add_shelf(directories):  # 7 "as"
    new_shelf = input('Введите номер новой полки:')
    if new_shelf in directories:
        print(f'Полка {new_shelf} уже существует')
    else:
        directories[new_shelf] = []
        print(f'Полка {new_shelf} добавлена')
    return directories

def main(documents, directories):  # Основная функция, объединяющая все функции для вводимых команд
    while True:
        user_input = input('\nВведите команду: ')
        if user_input == 'p':
            print(get_person_by_doc(documents))
            # 1 - #команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
        elif user_input == 'l':
            get_all_docs(documents)
            # 2 - команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
        elif user_input == 's':
            print(get_shelf(directories))
            # 3 - команда, которая спросит номер документа и выведет номер полки, на которой он находится
        elif user_input == 'a':
            documents, directories = add_new_doc(documents, directories)
            # 4 - команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
        elif user_input == 'd':
            # 5 - команда, которая спросит номер документа и удалит его из каталога и из перечня полок
            documents, directories = delete_doc(documents, directories)
        elif user_input == 'm':
            # 6 - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
            documents, directories = move_doc(documents, directories)
        elif user_input == 'as':
            # 7 - команда, которая спросит номер новой полки и добавит ее в перечень
            directories = add_shelf(directories)
        elif user_input == 'q':
            # 8 для выхода из программы
            break
        elif user_input == 'all':
            # ДЛЯ ВЫВОДА ВСЕХ ВЛАДЕЛЬЦЕВ ДОКУМЕНТОВ
            get_all_owners(documents)
        else:
            print('Вы ввели неправильную команду')

main(documents, directories)
