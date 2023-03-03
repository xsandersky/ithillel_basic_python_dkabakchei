import string
import secrets

def my_func():
    alphabet = string.ascii_letters + string.digits + '_'
    #password = ' '.join(secrets.choice(alphabet) for _ in range(8)) # [1,2,a, 2,b,_,2]

    stroka = ' '
    while True:
        password = ' '.join(secrets.choice(alphabet) for i in range(8)).split()
        for i in range(len(password)):
            if stroka == password[i]:
                my_func()
            stroka = password[i]
                
        if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 1):
            break
    password = ''.join(password)

    return password
        
    

print(my_func())