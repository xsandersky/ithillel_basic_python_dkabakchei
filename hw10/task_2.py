import string
import secrets


def get_int():
    user_input = input()
    
    while True:
        if user_input.isdigit():
            if int(user_input) > 7:
                break
        user_input = input('Программа принимает только числа. Введи число больше 7: ')
            
    user_input = int(user_input)
    
    return user_input
    

def my_pass(lenght_password):
    alphabet = string.ascii_letters + string.digits + '_'
    password = list((secrets.choice(alphabet) for i in range(lenght_password)))

    while True:
        flag = True
        
        for i in range(1, len(password)):
            if password[i] == password[i-1]:
                flag = False
                break

        if flag is True and (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)) == True:
            break
        
        password = list((secrets.choice(alphabet) for i in range(lenght_password)))

    password = ''.join(password)

    return password


def main():
    pass_lenght = get_int()
    print(my_pass(pass_lenght))


if __name__=='__main__':
    main()
