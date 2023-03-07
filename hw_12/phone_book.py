from copy import copy
#------------------------------------------------------------------------------
# Never use real phone/fax numbers for tests. Use 555 numbers: 
# https://en.wikipedia.org/wiki/555_(telephone_number)
phone_book = [
{"name": "Nazar", "surname": "Nazarenko", "age": 50, "phone_number":"+18005550102"},
{"name": "Mariia", "surname": "Mariychuk", "age": 15, "phone_number":"+18505550112"},
]

running = True


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
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
def find_entry_age_phonebook(years):
    global phone_book

    for d in phone_book:
        if d['age'] == years:
            print(d)
        else:
            continue


#------------------------------------------------------------------------------
def delete_entry_name_phonebook(name):
    global phone_book
    copy_phone_book = copy(phone_book)
    
    for i in range(len(phone_book)):
        if phone_book[i]['name'] == name:
            del copy_phone_book[i]

    return copy_phone_book


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    global phone_book
    copy_phone_book = copy(phone_book)
    copy_phone_book.sort(key=lambda sort_age: sort_age['age'])

    return copy_phone_book


#------------------------------------------------------------------------------
def increase_age(num):
    global phone_book
    copy_phone_book = copy(phone_book)
    
    for i in range(len(phone_book)):
        if phone_book[i]['age']:
            copy_phone_book[i]['age'] += num

    return copy_phone_book


#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    global phone_book
    sum = 0
    iterable = 0

    for dic in phone_book:
        iterable += 1
        sum += dic.pop('age')
        avg = sum / iterable

    return avg


#------------------------------------------------------------------------------
def save_to_file():
  pass


#------------------------------------------------------------------------------
def load_from_file():
    pass


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
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

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()