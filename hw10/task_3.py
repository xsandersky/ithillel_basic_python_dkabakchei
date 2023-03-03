from random import shuffle

def my_shuffle(lst):
    new_lst = []
    new_lst.extend(lst)

    while True:
        if new_lst != lst:
            break
        shuffle(new_lst)        
    return new_lst


def pemrtuate(text):
    list_text = text.split(' ')
    final_text = ''

    for elem in list_text:
        if len(elem) < 4:
            final_text = final_text + elem + ' '
            continue

        else:
            final_text = final_text + elem[0]
            last_char = elem[-1]

            origin_middle_txt = list(elem[1:-1])
            #shuffle_origin_middle_txt = ''.join(my_shuffle(origin_middle_txt))
            shuffle_origin_middle_txt = my_shuffle(origin_middle_txt)
            while True:
                if shuffle_origin_middle_txt != origin_middle_txt:
                    break
                shuffle_origin_middle_txt = my_shuffle(origin_middle_txt)
            
            shuffle_origin_middle_txt = ''.join(shuffle_origin_middle_txt)
            final_text = final_text + shuffle_origin_middle_txt + last_char + ' '
    return final_text


def main():
    my_list = 'За реузлтьаатми длосдіжнеь ооднго аглнісйкього уінвсрееитут, не має зчнаннея, в якмоу пояркду рзтооашвнаі лтіери у совлі. Гоолвен, щоб пшреа та оастння ліетри блуи на сєвому мсіці. Ретша летір мжоуть сділаувти в абосюлтно впиакдомову поярдук, все ондо ткест чатиитмтьеся без пброемл. Прчиниою цгоьо є те, що ми чтаимєо не кножу бкуву окером, а усе совло раозм.'
    print(pemrtuate(my_list))
    

if __name__=='__main__':
    main()
    