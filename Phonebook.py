def write_name():
    name = input('Введите имя: ')
    return name
def write_surname():
    surname = input('Введите фамилию: ')
    return surname
def write_phone():
    phone = input('Введите телефон: ')
    return phone
def write_adress():
    adress = input('Введите адрес: ')
    return adress

def input_data(a=None):
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {surname}: {phone}\n{adress}\n\n')

def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        data_first = data.readlines()
        print(data_first)
        for line in data_first:
            print(line, end='')

def search_line():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print(data)
        temp = data.readlines()
        print(temp)
        data_first = ''.join(temp).split('\n\n')
        print(data_first)
        for line in data_first:
            if search in line:
                print(line)

# input_data()
# print_data()
# search_line()

def update_data():
    name = input("Введите имя или фамилию человека, которого хотите изменить: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    updated_contact = []
    found = False
    for line in lines:
        if name.lower() in line.lower():
            new_name = input("Введите новое имя: ")
            new_last_name = input("Введите новую фамилию: ")
            new_phone = input("Введите новый номер телефона: ")
            updated_contact.append(f"{new_name} {new_last_name}: {new_phone}\n")
            found = True
        else:
            updated_contact.append(line)
    if found:
        with open('phonebook.txt', 'w', encoding='utf-8') as data:
            data.writelines(updated_contact)
        print("Контакт успешно изменен.")
    else:
        print("Контакт не найден.")

def delete_data():
    name = input("Введите имя или фамилию человека, которого хотите удалить: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    updated_contact = []
    found = False
    for line in lines:
        if name.lower() not in line.lower():
            updated_contact.append(line)
        else:
            found = True
    if found:
        with open('phonebook.txt', 'w', encoding='utf-8') as data:
            data.writelines(updated_contact)
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")


# update_data()  
# delete_data() 

  
 
