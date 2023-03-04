from random import shuffle
from copy import copy


def pemrtuate(text):
    list_text = text.split(' ')

    all_txt = []

    for elem in list_text:
        new_lst = []
        
        if len(elem) > 3:
            elem = list(elem)
            firs_elem = elem[0]
            last_elem = elem[-1]
            mid_txt = elem[1:-1]

            new_lst.extend(firs_elem)  
            while len(mid_txt) > 2:
                idx_txt_0_2_ = mid_txt[:3]
                copy_idx_txt_0_2_ = idx_txt_0_2_.copy()
                shuffle(idx_txt_0_2_)

                while True:
                    if idx_txt_0_2_ != copy_idx_txt_0_2_:
                        new_lst.extend(idx_txt_0_2_)
                        break
                    shuffle(idx_txt_0_2_)
                
                mid_txt = mid_txt[3:]

            if len(mid_txt) == 2:
                copy_mid_txt = mid_txt.copy()
                shuffle(mid_txt)
                while True:
                    if mid_txt != copy_mid_txt:
                        new_lst.extend(mid_txt)
                        break
                    shuffle(mid_txt)       

            else:
                new_lst.extend(mid_txt)

            new_lst.extend(last_elem)
            new_lst = ''.join(new_lst)
            all_txt.append(new_lst)

        else:
            all_txt.append(elem)

    final = ' '.join(all_txt)

    return final
                

def main():
    default_txt = 'Lorem Ipsum є псевдо- латинський текст використовується у веб - дизайні, типографіка, верстка, і друку замість англійської підкреслити елементи дизайну над змістом. Це також називається заповнювач ( або наповнювач) текст. Це зручний інструмент для макетів. Це допомагає намітити візуальні елементи в документ або презентацію, наприклад, друкарня, шрифт, або макет. Lorem Ipsum в основному частиною латинського тексту за класичною автор і філософа Цицерона.'
    print(pemrtuate(default_txt))
    

if __name__=='__main__':
    main()
    