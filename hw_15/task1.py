from copy import deepcopy
from json import load, dump

class InputHandler:
    def get_input_str(self, promt, value=None):
        while True:
            self.user_input = input(promt)

            if value:
                while self.user_input not in value:
                    self.user_input = input(promt)
                break

            if any(char.isdigit() for char in self.user_input):
                continue
            else:
                break

        return self.user_input
    

    def get_input_int(self, promt):
        while True:
            self.user_input = input(promt)

            if self.user_input.isdigit():
                self.user_input = int(self.user_input)
                break
        
        return self.user_input



class PhoneBook:
    """
    class PhoneBook - Includes the following methods:
    
    output_phonebook:               Displays our contacts on the screen
    print_promt:                    Displays the menu for managing our phonebook

    print_phonebook:                Outputs the existing list of contacts in the phonebook 
    sort_phone_book_by_age:         Sorts the list of contacts in our phonebook
    add_new_contact:                Adding a new contact to the phonebook
    find_contact_by_name:           Display all the information about the contact by his name
    find_contact_by_age:            Outputs all the information about the contact by his age
    remove_contact_by_name:         Remove a contact from the phonebook by his name
    count_all_conacts:              Count the number of contacts in the phonebook and display them on the screen
    avg_age_all_contacts:           Calculate the average age of all contacts in our phonebook
    increase_age_for_all_contacts:  Increase the age of all contacts in our phone book
    find_contact_by_operator:       Search for contacts in the phonebook by phone operator

    exit:                           Close the program with the option to save changes
    save_to_file:                   Save the changes to the existing phonebook or we can save the changes to a new file
    load_from_file:                 Load the phonebook from another file and work with it
    """



    running = True
    phone_book = [
            {"name":"Nazar", "surname":"Nazarenko", "age": 50, "phone_number":"+380676150054", "phone_operator":"Kyivstar"}, {"name":"Mariia", "surname":"Mariychuk", "age": 15, "phone_number":"+380631894577", "phone_operator":"Lifecell"}
            ]
    copy_phone_book = deepcopy(phone_book)


    def output_phonebook(self, number, contact):
        output_str = f"--[ {number} ]--------------------------\n"
        for key, value in contact.items():
            output_str += f"| {key.capitalize()}: {value:>20} |\n"
        print(output_str)


    def print_phonebook(self):                                                 
        print ("\n\n#########  Phone book  ##########")
        for number, contact in enumerate(self.phone_book, start=1):
            self.output_phonebook(self, number, contact)


    def print_promt(self):
        print("\n~ Welcome to phonebook ~")
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
        print("     0 - Exit\n")
        

    def add_new_contact(self):
        self.new_contact = {}
        self.new_contact['surname'] = InputHandler.get_input_str(self, 'Введи фалимию: ').capitalize()
        self.new_contact['name'] = InputHandler.get_input_str(self, 'Введи имя: ').capitalize()
        self.new_contact['age'] = InputHandler.get_input_int(self, 'Введи возраст: ')
        self.new_contact['phone_number'] = InputHandler.get_input_int(self, 'Введи номер телефона: ')
        self.new_contact['phone_operator'] = InputHandler.get_input_str(self, 'Введи название оператора: ').capitalize()
        self.phone_book.append(self.new_contact)


    def find_contact_by_name(self):
        self.input_find_name = InputHandler.get_input_str(self, 'Введи имя контакта, данные которого тебе нужны: ').capitalize()
        self.find_name = True
        
        for number, elem in enumerate(self.phone_book, start=1):
            if self.input_find_name == elem['name']:
                self.output_phonebook(self, number, elem)
                self.find_name = False
        if self.find_name:
            print('Такого имени нет')


    def find_contact_by_age(self):
        self.input_find_age = InputHandler.get_input_int(self, 'Введи возраст, для вывода контакта/ов: ')
        self.find_age = True
        
        for number, elem in enumerate(self.phone_book, start=1):
            if self.input_find_age == elem['age']:
                self.output_phonebook(self, number, elem)
                self.find_age = False
        if self.find_age:
            print('Контакта с таким возрастом нет')


    def find_contact_by_operator(self):
        self.input_find_operator = InputHandler.get_input_str(self, 'Введи название оператора для вывода контактов: ').capitalize()
        self.find_operator = True
        
        for number, elem in enumerate(self.phone_book, start=1):
            if self.input_find_operator == elem['phone_operator']:
                self.output_phonebook(self, number, elem)
                self.find_operator = False
        if self.find_operator:
            print('Контакта с таким возрастом нет')


    def remove_contact_by_name(self):
        self.user_input = InputHandler.get_input_str(self, 'Введи имя контакта которого хочешь удалить: ').capitalize()
        self.copy_phone_book = deepcopy(self.phone_book)
        self.flag_remove = True

        for i in range(len(self.phone_book)):
            if self.phone_book[i]['name'] == self.user_input:
                self.flag_remove = False
                del self.copy_phone_book[i]
        
        if self.flag_remove:
            print('Нечего удалять')
        else:
            self.phone_book = self.copy_phone_book


    def count_all_conacts(self):
        print(f'Всего {len(self.phone_book)} контактов в телефоннов книге')


    def sort_phone_book_by_age(self):
        self.phone_book.sort(key=lambda sort_age: sort_age['age'])


    def increase_age_for_all_contacts(self):
        self.user_input = InputHandler.get_input_int(self, 'Введи на сколько увеличить возраст контактов: ')
        if len(self.phone_book) > 0:
            for contact in self.phone_book:
                if contact['age']:
                    contact["age"] += self.user_input
        else:
            print('Телефонна книга пустая. Так, что возраст не у кого повышать')

    
    def avg_age_all_contacts(self):
        self.summary = 0

        for contact in self.phone_book:
            self.summary += contact['age']
        avg = self.summary / len(self.phone_book)

        print(f'Средний возраст всех людей в телефонной книге = {round(avg,2)}')


    def save_to_file(self):
        self.save_input = InputHandler.get_input_str(self, 'Перезаписать этот файл? (y/n)', ('y', 'n')).lower()

        if self.save_input == 'y':
            with open('__main__.py', 'w') as f:
                dump(self.phone_book, f)

        else:
            self.user_input = input('Введи название файла куда сохранишь книгу контактов: ')
            with open(self.user_input, 'w') as f:
                dump(self.phone_book, f)
                


    def load_from_file(self):
        if len(self.phone_book) > 0:
            self.answer = InputHandler.get_input_str(self, 'У вас есть существующие данные. Сохранить их перед загрузкой из файла? (y/n): ', ('y', 'n')).lower()
            if self.answer == 'y':
                self.save_to_file()
            self.phone_book.clear()

        self.user_input = input('Введи название файла, откуда загрузить телефонные данные: ')
        with open(self.user_input, 'r') as f:
            self.new_data_book = load(f)

        self.phone_book = self.new_data_book

        return self.phone_book
    

    def exit(self):
        self.answer = InputHandler.get_input_str(self, "У вас есть существующие данные. Сохранить их перед выходом из программы? (y/n): ", ('y', 'n')).lower()
        if self.answer == 'y':
                self.save_to_file()

        self.running = False


class User(PhoneBook):
    while PhoneBook.running:
        try:
            menu = {
                        '1':  PhoneBook.print_phonebook,
                        '2':  PhoneBook.sort_phone_book_by_age,
                        '3':  PhoneBook.add_new_contact,
                        '4':  PhoneBook.find_contact_by_name,
                        '5':  PhoneBook.find_contact_by_age,
                        '6':  PhoneBook.remove_contact_by_name,
                        '7':  PhoneBook.count_all_conacts,
                        '8':  PhoneBook.avg_age_all_contacts,
                        '9':  PhoneBook.increase_age_for_all_contacts,
                        'a':  PhoneBook.find_contact_by_operator,

                        '0':  PhoneBook.exit,
                        's':  PhoneBook.save_to_file,
                        'l':  PhoneBook.load_from_file,
                    }
            
            PhoneBook.print_promt(PhoneBook)
            user_input = InputHandler.get_input_str(InputHandler, 'phonebook> ', '0123456789sla')
            menu[user_input](PhoneBook)

        except Exception as ex:
            print("Something went wrong. Try again...")
             










       