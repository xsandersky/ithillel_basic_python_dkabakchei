def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    
    
def main():
    a = float(input())
    print(sign(a))


main()