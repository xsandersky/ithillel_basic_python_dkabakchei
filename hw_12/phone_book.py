#------------------------------------------------------------------------------
# Never use real phone/fax numbers for tests. Use 555 numbers: 
# https://en.wikipedia.org/wiki/555_(telephone_number)
from copy import copy
from json import load, dump
import string
import argparse

parser = argparse.ArgumentParser(description='Phone Book App')

parser.add_argument('filename', type=str, help='Путь к файлу с книгой')
parser.add_argument('-v', '--verbose', action='store_true', help='Путь к файлу с книгой')

args = parser.parse_args()


phone_book = [
{"name":"Nazar", "surname":"Nazarenko", "age": 50, "phone_number":"+380676150054", "phone_operator":"Kyivstar"},
{"name":"Mariia", "surname":"Mariychuk", "age": 15, "phone_number":"+380631894577", "phone_operator":"Lifecell"},
]
check_equal_phone_book = copy(phone_book)

running = True
decor_off = not args.verbose

#------------------------------------------------------------------------------
def get_input_str(promt, value = None):

    while True:
        user_input = input(promt)
        
        if value is not None:
            while user_input not in value:
                user_input = input(promt)
            break

        if any(char.isdigit() for char in user_input):
            continue
        else:
            break

    return user_input


#------------------------------------------------------------------------------
def get_input_int(promt):

    while True:
        user_input = input(promt)

        if user_input.isdigit():
            user_input = int(user_input)
            break

    return user_input


#------------------------------------------------------------------------------
def wrapper_off_on(decor_off):
    def wrapper(func):
        def prints(*args, **qwargs):
            if decor_off:
                print(f'Начинаю обарбатывать фурнцию {func.__name__}\n')
            result = func(*args, **qwargs)
            if decor_off:
                print(f'\nЗаканчиваю обрабатывать вашу функцию {func.__name__}')
            return result
        return prints   
    return wrapper

#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| Operator:%20s |" % entry["phone_operator"])
    print ()


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def print_phonebook():                                                              #############DONE     print_phonebook
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def add_entry_phonebook():                                                            #############DONE     add_entry_phonebook     
    global phone_book
    surname = get_input_str("    Enter surname: ").capitalize()
    name    = get_input_str("    Enter name: ").capitalize()
    age     = get_input_int("    Enter age: ")
    phone_number   = get_input_int("    Enter phone num.: ")
    phone_operator = get_input_str("    Enter phone operator: ").capitalize()

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["phone_operator"] = phone_operator
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def find_entry_name_phonebook():                                                            #############DONE      find_entry_name_phonebook
    global phone_book
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def find_entry_age_phonebook():                                                                #############DONE     find_entry_age_phonebook():
    global phone_book
    user_input = get_input_int('Введи цифру: ')
    idx = 1
    flag = True

    for entry in phone_book:
        if entry['age'] == user_input:
            print_entry(idx, entry)
            flag = False
    if flag:
        print('Not found!')


#------------------------------------------------------------------------------   
@wrapper_off_on(decor_off)
def find_entry_by_operator():                                                                   #############DONE     find_entry_by_operator()
    global phone_book

    user_input = get_input_str('Введи название мобильного оператора: ')
    number = 1

    for entry in phone_book:
        if entry['phone_operator'] == user_input:
            print_entry(number, entry)
            number += 1


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def delete_entry_name_phonebook():                                                              #############DONE       delete_entry_name_phonebook():  
    global phone_book
    copy_phone_book = copy(phone_book)

    user_input = get_input_str('Введи кого хочешь удалить из телефонной книги: ')
    
    for i in range(len(phone_book)):
        if phone_book[i]['name'] == user_input:
            del copy_phone_book[i]

    if phone_book == copy_phone_book:
        print('Нечего удалять')
    else:
        phone_book = copy_phone_book
    
    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def count_all_entries_in_phonebook():                                                            #############DONE        count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def print_phonebook_by_age():                                                                    #############DONE  print_phonebook_by_age(
    global phone_book
    phone_book.sort(key=lambda sort_age: sort_age['age'])

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def increase_age():                                                                              #############DONE  increase_age
    global phone_book

    user_input = get_input_int('Введи на сколько увеличить возраст всех людей в телефонной книге: ')

    for entry in phone_book:
        if entry['age']:
            entry['age'] += user_input


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def avr_age_of_all_persons():                                                                     #############DONE     avr_age_of_all_persons
    global phone_book
    sum = 0

    for dic in phone_book:
        sum += dic.pop('age')
        avg = sum / len(phone_book)

    print(f'Средний возраст всех людей в телефонной книге = {avg}')





#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def save_to_file():
    global phone_book
    user_input = get_input_str('Введи название файла (с расширением) куда сохранять: ')

    f = open(user_input, 'w')
    dump(phone_book, f)
    f.close
    


#------------------------------------------------------------------------------
@wrapper_off_on(decor_off)
def load_from_file():
    global phone_book
    if len(phone_book) > 0:
        answer = get_input_str("У вас есть существующие данные. Сохранить их перед загрузкой из файла? (y/n): ", ('y', 'n'))
        if answer.lower() == 'y':
            save_to_file()

    phone_book.clear()
    user_input = get_input_str('Введи название файла, откуда загрузить телефонные данные: ')

    f = open(user_input, 'r')
    new_data_book = load(f)
    f.close()
    phone_book = new_data_book

    return phone_book
    
    #------------------------------------------------------------------------------

@wrapper_off_on(decor_off)
def exit():
      global running
      answer = get_input_str("У вас есть существующие данные. Сохранить их перед выходом из программы? (y/n): ", ('y', 'n'))
      if answer.lower() == 'y':
            save_to_file()

      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     a - Find entry by phone operator")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
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


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()