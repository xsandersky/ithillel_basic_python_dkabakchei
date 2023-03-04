import string
import secrets


def get_int():
    user_input = input()
    
    while True:
        if user_input.isdigit():
            if int(user_input) > 7:
                break
            else:
                user_input = input('Введи число больше 7: ')
        user_input = input('Программа принимает только числа. Введи число больше 7: ')
            
    user_input = int(user_input)
    
    return user_input
    

def my_pass(lenght_password):
    alphabet = string.ascii_letters + string.digits + '_'
    
    password = ' '.join(secrets.choice(alphabet) for i in range(lenght_password)).split()
    
    while True:

        while True:
            flag = True
            proverka_na_equal = ' '

            for i in range(len(password)):
                if proverka_na_equal != password[i]:
                    print(f'proverka_na_equal: {proverka_na_equal} не равна password[i]: {password[i]}')
                    proverka_na_equal = password[i]
                else:
                    flag = False
                    break

            if flag == True:
                break
            else:
                password = ' '.join(secrets.choice(alphabet) for i in range(lenght_password)).split()

        if (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)) == True:
            break

        password = ' '.join(secrets.choice(alphabet) for i in range(lenght_password)).split()

    password = ''.join(password)

    return password


def main():
    x = get_int()
    print(my_pass(x))


if __name__=='__main__':
    main()
