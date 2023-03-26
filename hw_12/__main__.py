#------------------------------------------------------------------------------
# Never use real phone/fax numbers for tests. Use 555 numbers: 
# https://en.wikipedia.org/wiki/555_(telephone_number)
from copy import copy
from json import load, dump, dumps
from utilities.wrapper import wrapper_off_on
from utilities.user_input import get_input_str, get_input_int
from utilities.output_prints import print_entry, print_prompt, printError, printInfo
import argparse

parser = argparse.ArgumentParser(description='Phone Book App')

parser.add_argument('filename', type=str, help='Путь к файлу с книгой')
parser.add_argument('-v', '--verbose', action='store_true', help='Включение/выключение декоратора')
args = parser.parse_args()

phone_book = [
{"name":"Nazar", "surname":"Nazarenko", "age": 50, "phone_number":"+380676150054", "phone_operator":"Kyivstar"},
{"name":"Mariia", "surname":"Mariychuk", "age": 15, "phone_number":"+380631894577", "phone_operator":"Lifecell"},
]

check_equal_phone_book = copy(phone_book)

running = True
decor_off = not args.verbose

#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def print_phonebook():                                                 
    print ("\n\n#########  Phone book  ##########\n")

    for number, entry in enumerate(phone_book, start=1):
        print_entry(number, entry)


@wrapper_off_on(decor_off)
def add_entry_phonebook():                                                    
    global phone_book

    entry = {}
    entry["surname"] = get_input_str("Enter surname: ").capitalize()
    entry["name"] = get_input_str("Enter name: ").capitalize()
    entry["age"] = get_input_int("Enter age: ")
    entry["phone_number"] = get_input_int("Enter phone num.: ")
    entry["phone_operator"] = get_input_str("Enter phone operator: ").capitalize()
    phone_book.append(entry)


@wrapper_off_on(decor_off)
def find_entry_name_phonebook():                                                      
    global phone_book

    name = get_input_str("    Enter name: ")
    found = False

    for number, entry in enumerate(phone_book, start=1):
        if entry["name"] == name:
            print_entry(number, entry)
            found = True
    if not found:
        printError("Not found!!")


@wrapper_off_on(decor_off)
def find_entry_age_phonebook():                                                                
    global phone_book
    user_input = get_input_int('Введи возраст для поиска контакта: ')
    flag = True

    for number, entry in enumerate(phone_book, start=1):
        if entry['age'] == user_input:
            print_entry(number, entry)
            flag = False
    if flag:
        printError('Not found!')

 
@wrapper_off_on(decor_off)
def find_entry_by_operator():                                                                 
    global phone_book

    user_input = get_input_str('Введи название мобильного оператора: ').capitalize()
    flag = True

    for number, entry in enumerate(phone_book, start=1):
        if entry['phone_operator'] == user_input:
            print_entry(number, entry)
            flag = False
    if flag:
        printError('Not found!')
    

@wrapper_off_on(decor_off)
def delete_entry_name_phonebook():                                                                
    global phone_book
    copy_phone_book = copy(phone_book)

    user_input = get_input_str('Введи кого хочешь удалить из телефонной книги: ').capitalize()
    
    for contact in phone_book:
        if contact['name'] == user_input:
            copy_phone_book.remove(contact)

    if phone_book == copy_phone_book:
        print('Нечего удалять')
    else:
        phone_book = copy_phone_book
        print(f'Контакт с именем {user_input} был удален')

    for number, entry in enumerate(phone_book, start=1):
        print_entry(number, entry)


@wrapper_off_on(decor_off)
def count_all_entries_in_phonebook():                                                            
    print ("Total number of entries: ", len(phone_book))


@wrapper_off_on(decor_off)
def print_phonebook_by_age():                                                                    
    global phone_book
    phone_book.sort(key=lambda sort_age: sort_age['age'])

    for number, entry in enumerate(phone_book, start=1):
        print_entry(number, entry)


@wrapper_off_on(decor_off)
def increase_age():                                                                              
    global phone_book

    user_input = get_input_int('Введи на сколько увеличить возраст всех людей в телефонной книге: ')

    for entry in phone_book:
        if entry['age']:
            entry['age'] += user_input


@wrapper_off_on(decor_off)
def avr_age_of_all_persons():                                                                     
    global phone_book
    sum_age = 0

    for contact in phone_book:
        sum_age += contact['age']

    avg = sum_age / len(phone_book)

    print(f'Средний возраст всех людей в телефонной книге = {round(avg,2)}')


@wrapper_off_on(decor_off)
def save_to_file():
    global phone_book
    user_input = get_input_str('Введи название файла (с расширением) куда сохранять: ')
    
    with open(user_input, 'w') as f:
        dump(phone_book, f)
    

@wrapper_off_on(decor_off)
def load_from_file():
    global phone_book

    if len(phone_book) > 0:
        answer = get_input_str("У вас есть существующие данные. Сохранить их перед загрузкой из файла? (y/n): ", ('y', 'n'))
        if answer.lower() == 'y':
            save_to_file()

    phone_book.clear()
    user_input = get_input_str('Введи название файла, откуда загрузить телефонные данные: ')

    with open(user_input, 'r') as f:
        new_data_book = load(f)
        
    phone_book = new_data_book

    return phone_book
    

@wrapper_off_on(decor_off)
def exit():
      global running
      answer = get_input_str("У вас есть существующие данные. Сохранить их перед выходом из программы? (y/n): ", ('y', 'n'))
      if answer.lower() == 'y':
            save_to_file()

      running = False


def main():
    while running:
        try:
            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  'a':  find_entry_by_operator,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = get_input_str("phonebook> ", '0123456789sla')
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")



if __name__ == '__main__':
    main()