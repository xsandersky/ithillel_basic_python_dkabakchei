def main():
    kilograms = float(input())

    calculate_wheat_chess_position_kilograms = 10 / 0.035
    count_seeds_on_n_position = 1

    for i in range(97, 105):
        for j in range(1, 9):
            count_seeds_on_n_position

            if count_seeds_on_n_position >= calculate_wheat_chess_position_kilograms:
                print(f'Искомая: {chr(i) + str(j)}')
                break
        
            count_seeds_on_n_position = count_seeds_on_n_position + count_seeds_on_n_position

        if count_seeds_on_n_position>= calculate_wheat_chess_position_kilograms:
            break


main()