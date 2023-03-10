from random import randint
import string


def get_integer(prompt, lower_bound, upper_bound):
    while True:
        try:
            user_input = int(input(prompt))
            if lower_bound <= user_input <= upper_bound:
                break
            else:
                print(f'Принимаем числа от {lower_bound} до {upper_bound}.')

        except ValueError:
            print('- Попробуй ввести нужную цифру.')
    
    return user_input


def get_str(prompt, valid_char):    
    user_input = input(prompt)
    
    while True:        
        if user_input in valid_char:
                break
        else:
            user_input = input('Введи букву согласно инструкциям: ')
    
    return user_input.lower()


def hint_help():
    txt = 'Если число от ПК больше рандомного, то нажми "w" | Если число меньше, нажми "s" | Если угадал, то нажми "="'
    lenght_txt = len(txt)
    print('|' + '-' * lenght_txt + '|')
    print('|' + txt + '|')
    print('|' + '-' * lenght_txt + '|')


def user_find_num():
    lower_bound = 1
    upper_bound = 100

    random_num = randint(1, 100)
    my_num = get_integer(f'Угадай число от {lower_bound} до {upper_bound}: ', lower_bound, upper_bound)

    while my_num != random_num:
        if my_num > random_num:
            upper_bound = my_num
            print('- Твое число больше рандомного.')

        else:
            lower_bound = my_num
            print('- Твое число меньше рандомного')

        my_num = get_integer(f'Введи число от {lower_bound} до {upper_bound}: ', lower_bound, upper_bound)

    print(f'Да! Ты угадал. Рандомное число = {my_num}')


def pc_find_num():
    lower_bound = 1
    upper_bound = 100
    my_num = get_integer('Загадай число от 1 до 100: ', lower_bound, upper_bound)

    print('Рандомное число которое должен угадать ПК:', my_num)
    hint_help()

    pc_num = randint(lower_bound, upper_bound)
    print('- Пк называет число:', pc_num)

    char = get_str('Нажми букву согласно инструкции: ', ('w', 's'))

    while True:
        if char in 'w':
            upper_bound = pc_num
            print(f'Это число больше, следующее рандомное число от ПК в пределах от {lower_bound} до {upper_bound}')

        elif char in 's':
            lower_bound = pc_num
            print(f'Это число меньше, следующее рандомное число от ПК в пределах от {lower_bound} до {upper_bound}')
       
        elif char in '=':
            print(f'ПК Угадал. Наше число {pc_num}')
            break

        pc_num = randint(lower_bound, upper_bound)
        print('- Пк называет число: ', pc_num)
        char = get_str('Жми букву "w" если число больше, "s" если число меньше, "=" если угадал: ', ('w', 's', '='))


def main():
    while True:      
        char = get_str('Если хочешь сам угадывать числа, то нажми кнопку "u" | Если хочешь, чтобы ПК угадывал числа, нажми кнопку "p": ', ('u', 'p')) 
        if char == 'u':
            user_find_num()
        elif char == 'p':
            pc_find_num()
        
        restart = get_str('Хочешь повторить игру? Если - да, нажми "y", если - нет, нажми "n": ', ('y', 'n'))
        if restart == 'n':
            break
    print('Отлично поиграли.')


if __name__=='__main__':
    main()