a = 1223338555550

b = max(str(a))

maxi = 0

while a != 0:
    if a % 10 > maxi:
        maxi = a % 10
    a = a // 10


print(b, maxi)