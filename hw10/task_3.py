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
                copy_idx_txt_0_2_ = chunk.copy()

                shuffle(chunk)
                while chunk == copy_idx_txt_0_2_:
                    shuffle(chunk)
                new_lst.extend(chunk)
                mid_txt = mid_txt[3:]

            if len(mid_txt) == 2:
                if mid_txt[0] == mid_txt[1]:
                    new_lst.extend(mid_txt)
                    break

                else:
                    copy_mid_txt = mid_txt.copy()
                    
                    shuffle(mid_txt)
                    while mid_txt == copy_mid_txt:
                        shuffle(mid_txt) 
                    new_lst.extend(mid_txt)

            new_lst.append(elem[-1])
            all_txt.append(''.join(new_lst))

    final = ' '.join(all_txt)

    return final
                

def main():
    default_txt = 'Lorem Ipsum є псевдо- латинський текст використовується у веб - дизайні, типографіка, верстка, і друку замість англійської підкреслити елементи дизайну над змістом. Це також називається заповнювач ( або наповнювач) текст. Це зручний інструмент для макетів. Це допомагає намітити візуальні елементи в документ або презентацію, наприклад, друкарня, шрифт, або макет. Lorem Ipsum в основному частиною латинського тексту за класичною автор і філософа Цицерона.'
    print(pemrtuate(default_txt))
    

if __name__=='__main__':
    main()
    