from random import randint

num_lst = [i for i in range(1, 101)]

def get_integer():
    int_input = int(input('Input some number from 1 to 100: '))
    return int_input


def hint_help():
    txt = 'Если число от ПК больше рандомного, то нажми "w" | Если число меньше, нажми "s" | Если угадал, то нажми "="'
    lenght_txt = len(txt)
    print('|' + '-' * lenght_txt + '|')
    print('|' + txt + '|')
    print('|' + '-' * lenght_txt + '|')
    

def get_str():
    str_input = input()
    return str_input


def idx_num_in_list(pc_num):
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
        my_num = int(input('Введи число: '))
    print('Угадал')
    
    print(f'Запустить игру повторно?\nНажми "y" если хочешь продолжить | Нажми "n" если хочешь закончить игру')
    if get_str() == 'y':
        return user_find_num()


def pc_find_num():
    
    global num_lst    

    hint_help()
    num = randint(num_lst[0], num_lst[-1])
    print('Рандомное число которое должен угадать ПК:', num)
    pc_num = randint(num_lst[0], num_lst[-1])
    print('Пк называет число:', pc_num)
    
    
    char = get_str()
    
    while True:
        if char == 'w':
            print('Это число больше, попробуй еще раз угадать')
            
            idx_num = idx_num_in_list(pc_num)
            num_lst = num_lst[:idx_num]
            pc_num = randint(num_lst[0], num_lst[-1])

            print('Новое рандомное число:', pc_num)

        elif char == 's':
            print('Это число меньше, попробуй еще раз угадать')

            idx_num = idx_num_in_list(pc_num)
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
    print('Если хочешь сам угадывать числа, то нажми кнопку "m" | Если хочешь, чтобы ПК угадывал числа, нажми кнопку "p"')
 
    a = get_str()

    if a == 'p':
        pc_find_num()
    elif a == 'm':
        user_find_num()
    print('Смотри куда ты жмешь!')
        
    
if __name__=='__main__':
    main()
