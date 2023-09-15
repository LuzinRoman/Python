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
        print(data)
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
search_line()

def update_contact(full_name):
    new_name = write_name()
    new_surname = write_surname()
    new_phone = write_phone()
    new_address = write_adress()
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        for line in lines:
            if full_name in line:
                data.write(f'{new_name} {new_surname}: {new_phone}\n{new_address}\n\n')
            else:
                data.write(line)

def delete_contact(full_name):
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        for line in lines:
            if full_name not in line:
                data.write(line)


# update_contact()
delete_contact('Роман Лузин')
