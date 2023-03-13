import string
import secrets


def get_int(promt):
    user_input = input(promt)
    
    while True:
        if user_input.isdigit():
            if int(user_input) > 7:
                break
        user_input = input('Программа принимает только числа. Введи число больше 7: ')
            
    user_input = int(user_input)
    
    return user_input
    

def my_pass(lenght_password):
    alphabet = string.ascii_letters + string.digits + '_'
    
    while True:
        flag = True
        password = list(secrets.choice(alphabet) for i in range(lenght_password))
        
        for i in range(1, len(password)):
            if password[i] == password[i-1]:
                flag = False
                break

        if flag and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
            break

    password = ''.join(password)

    return password


def main():
    pass_lenght = get_int('Введи число из скольких символов ты хочешь создать пароль: ')
    print(my_pass(pass_lenght))


if __name__=='__main__':
    main()
