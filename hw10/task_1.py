def copydeep(obj, memory=None):
    if memory is None:
        memory = {}

    if id(obj) not in memory:
        memory[id(obj)] = obj
        for elem in obj:
            if isinstance(elem, list):
                value = []
                for val in elem:
                    value.append(copydeep(val, memory))
                return value

            elif isinstance(elem, dict):
                value = {}
                for key, val in elem.items():
                    value[copydeep(key, memory)] = copydeep(val, memory)
                return value
                
            else:
                value = obj
                return value   
    else:
        return memory[id(obj)]


def main():

    test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
    test_data[3]['d'] = test_data
    test_data[-1]['f'] = test_data[-1]
    copy = copydeep(test_data)
    print(test_data)
    # [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
    print(copy)
    # [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
    print(copy[3]['c'] is not test_data[3]['c'])  # True
    print(copy[3]['d'] is not test_data[3]['d'])  # True
    print(copy[3]['d'] is copy)  # True
    print(copy[-1] is not test_data[-1])  # True
    print(copy[-1] is copy[-1]['f'])  # True


main()