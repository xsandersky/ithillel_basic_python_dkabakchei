from copy import deepcopy

class PhoneBook:
    phone_book = [
            {"name":"Nazar", "surname":"Nazarenko", "age": 50, "phone_number":"+380676150054", "phone_operator":"Kyivstar"}, {"name":"Mariia", "surname":"Mariychuk", "age": 15, "phone_number":"+380631894577", "phone_operator":"Lifecell"}
            ]
        

    def output(self, number, contact):
            print ("--[ %s ]--------------------------" % number)
            print ("| Surname: %20s |" % contact["surname"])
            print ("| Name:    %20s |" % contact["name"])
            print ("| Age:     %20s |" % contact["age"])
            print ("| Phone:   %20s |" % contact["phone_number"])
            print ("| Operator:%20s |" % contact["phone_operator"])
            print ()


    def avg_age(self):
        self.avg_age = 0
        for i in self.phone_book:
            self.avg_age += i['age']
        print(self.avg_age)


    def add_new_contact(self):
        self.new_contact = {}
        self.new_contact['surname'] = input('Введи фалимию: ')
        self.new_contact['name'] = input('Введи имя: ')
        self.new_contact['age'] = input('Введи возраст: ')
        self.new_contact['phone_number'] = input('Введи номер телефона: ')
        self.new_contact['phone_operator'] = input('Введи название оператора: ')
        self.phone_book.append(self.new_contact)


    def find_contact_by_name(self):
        self.input_find_name = input('Введи имя контакта, данные которого тебе нужны: ')
        flag = True
        
        for number, elem in enumerate(self.phone_book):
            if self.input_find_name == elem['name']:
                self.output(number, elem)
                flag = False
        if flag:
            print('Такого имени нет')


    def find_contact_by_age(self):
        self.input_find_name = int(input('Введи возраст, для вывода контакта/ов: '))
        flag = True
        
        for number, elem in enumerate(self.phone_book):
            if self.input_find_name == elem['age']:
                self.output(number, elem)
                flag = False
        if flag:
            print('Контакта с таким возрастом нет')


    def find_contact_by_operator(self):
        self.input_find_name = input('Введи название оператора для вывода контактов: ')
        flag = True
        
        for number, elem in enumerate(self.phone_book):
            if self.input_find_name == elem['phone_operator']:
                self.output(number, elem)
                flag = False
        if flag:
            print('Контакта с таким возрастом нет')


    def remove_contact_by_name(self):
        self.user_input = input('Введи имя контакта которого хочешь удалить: ')
        self.copy_phone_book = deepcopy(self.phone_book)
        flag = True

        for i in range(len(self.phone_book)):
            if self.phone_book[i]['name'] == self.user_input:
                flag = False
                del self.copy_phone_book['name']
        
        if  flag:
            print('Нечего удалять')
        else:
            self.phone_book = self.copy_phone_book

    def count_all_conacts(self):
        print(f'Всего {len(self.phone_book)} контакта\ов в телефоннов книге')

    





p = PhoneBook()
# p.avg_age()
# p.add_new_contact()
# p.find_contact_by_name()
# p.find_contact_by_age()
p.count_all_conacts()