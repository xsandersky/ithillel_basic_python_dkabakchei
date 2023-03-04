from random import randint
import string


def get_integer():
    user_input = input('Жмакай цифру: ')
    
    while True:
        if user_input.isdigit():
                break
        else:
            user_input = input('Введи число: ')
            
    user_input = int(user_input)
    
    return user_input


def get_str():    
    user_input = input('Нажимай на букву: ')

    while True:
        if user_input in string.ascii_letters or user_input in '=':
                break
        else:
            user_input = input('Жми на букву, а не цифру:)')
    
    return user_input


def hint_help():
    txt = 'Если число от ПК больше рандомного, то нажми "w" | Если число меньше, нажми "s" | Если угадал, то нажми "="'
    lenght_txt = len(txt)
    print('|' + '-' * lenght_txt + '|')
    print('|' + txt + '|')
    print('|' + '-' * lenght_txt + '|')
    

def idx_num_in_list(pc_num, num_lst):
    x = 0
    
    for i in num_lst:
        if i == pc_num:
            break
        x += 1
    return x


def user_find_num():
    num = randint(1, 100)
    my_num = get_integer()

    while my_num != num:
        if my_num > num:
            print('Твое число больше рандомного')
        else:
            print('Твое число меньше рандомного')
        my_num = get_integer()
    print('Угадал')
    
    print(f'Запустить игру повторно?\nНажми "y" если хочешь продолжить | Нажми "n" если хочешь закончить игру')
    if get_str() == 'y':
        return user_find_num()


def pc_find_num():
    num_lst = [i for i in range(1, 101)] 
    hint_help()

    num = randint(num_lst[0], num_lst[-1])
    print('Рандомное число которое должен угадать ПК:', num)
    pc_num = randint(num_lst[0], num_lst[-1])
    print('Пк называет число:', pc_num)
    
    char = get_str()
    
    while True:
        if char in 'Ww':
            print('Это число больше, попробуй еще раз угадать')
            
            idx_num = idx_num_in_list(pc_num, num_lst)
            num_lst = num_lst[:idx_num]
            pc_num = randint(num_lst[0], num_lst[-1])

            print('Новое рандомное число:', pc_num)

        elif char in 'sS':
            print('Это число меньше, попробуй еще раз угадать')

            idx_num = idx_num_in_list(pc_num, num_lst)
            num_lst = num_lst[idx_num + 1:]
            pc_num = randint(num_lst[0], num_lst[-1])

            print('Новое рандомное число:', pc_num)

        elif char == '=':
            print('Угадал')
            break
        char = get_str()
      
    print(f'Запустить игру повторно?\nНажми "y" если хочешь продолжить | Нажми "n" если хочешь закончить игру')

    if get_str() == 'y':
        return pc_find_num()


def main():
    print('Если хочешь сам угадывать числа, то нажми кнопку "m" | Если хочешь, чтобы ПК угадывал числа, нажми кнопку "p": ')
    
    char = get_str()

    if char in 'p':
        pc_find_num()
    elif char in 'm':
        user_find_num()


if __name__=='__main__':
    main()