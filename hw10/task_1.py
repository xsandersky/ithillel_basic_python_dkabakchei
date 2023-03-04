def copydeep(obj, memory=None):
    if memory is None:
        memory = {}

    if id(obj) in memory:
        return memory[id(obj)]

    if isinstance(obj, list):
        new_lst = []
        memory[id(obj)] = new_lst
        for val in obj:
            new_lst.append(copydeep(val, memory))
        return new_lst

    elif isinstance(obj, dict):
        new_dict = {}
        memory[id(obj)] = new_dict
        for key, val in obj.items():
            new_dict[copydeep(key)] = copydeep(val, memory)
        return new_dict
                
    else:
        return obj
        

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