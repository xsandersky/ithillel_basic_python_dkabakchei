from random import shuffle
from copy import copy


def pemrtuate(text):
    list_text = text.split(' ')

    all_txt = []

    for elem in list_text:
        new_lst = []
        
        if len(elem) < 4:
            all_txt.append(elem)

        else:
            mid_txt = list(elem[1:-1])
            new_lst.append(elem[0])

            while len(mid_txt) > 2:
                chunk = mid_txt[:3]

                shuffle(chunk)
                while chunk == mid_txt[:3]:
                    shuffle(chunk)

                new_lst.extend(chunk)
                mid_txt = mid_txt[3:]

            if len(mid_txt) == 2:
                if mid_txt[0] == mid_txt[1]:

                    mid_txt[0], mid_txt[1] = mid_txt[1], mid_txt[0]
                    new_lst.extend(mid_txt)

                else:
                    copy_mid_txt = mid_txt.copy()
                    
                    shuffle(mid_txt)
                    while mid_txt == copy_mid_txt:
                        shuffle(mid_txt) 
                    new_lst.extend(mid_txt)
            else:
                new_lst.extend(mid_txt)

            new_lst.append(elem[-1])
            all_txt.append(''.join(new_lst))

    final = ' '.join(all_txt)

    return final
                

def main():
    default_txt = 'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).'
    print(pemrtuate(default_txt))
    

if __name__=='__main__':
    main()
    