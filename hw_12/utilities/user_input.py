def get_input_str(promt, value = None):
    while True:
        user_input = input(promt)
        
        if value is not None:
            while user_input not in value:
                user_input = input(promt)
            break

        if any(char.isdigit() for char in user_input):
            continue
        else:
            break

    return user_input


def get_input_int(promt):
    while True:
        user_input = input(promt)

        if user_input.isdigit():
            user_input = int(user_input)
            break

    return user_input