def fibo(x):
    global x1
    global x2
    global fibo_list
    for i in range(x-2): 
        count = x1 + x2
        fibo_list.append(count)
        x1 = x2
        x2 = count
    return count


def main():
    results = fibo(20)
    print(results)
    print(fibo_list)


x1, x2 = 0, 1
fibo_list = [0, 1]

main()