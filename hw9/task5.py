def group_by_surname(list_of_enrollees): # returns 4 ints
    mit_dict = {
    'A_I':0,
    'J_P':0,
    'Q_T':0,
    'U_Z':0,
    }

    for value in list_of_enrollees:

        idx_s = value.find(' ') + 1
        fio_char = ord(value[idx_s].upper())  # value[idx] equal char from ASCI table. 'A' = 65....'Z' = 90

        
        if fio_char < 74:
            mit_dict['A_I'] += 1

        elif 73 < fio_char < 81:
            mit_dict['J_P'] += 1
        
        elif 80 < fio_char < 85:
            mit_dict['Q_T'] += 1
                
        else:
            mit_dict['U_Z'] += 1
        
    return mit_dict['A_I'], mit_dict['J_P'], mit_dict['Q_T'], mit_dict['U_Z']


def main():
    a = ['Will Smith', 'Jay Z']
    g1, g2, g3, g4 = group_by_surname(a)

    print(f'A_I: {g1}\nJ_P: {g2}\nQ_T = {g3}\nU_Z = {g4}')


main()