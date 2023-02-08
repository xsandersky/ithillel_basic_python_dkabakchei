#1
a = input().split('_')
a[0] = a[0].capitalize()
a[1] = a[1].capitalize()
a[2] = a[2].capitalize()
a = ''.join(a)
print(a)

print()

#2
txt = 'employee_first_name'
txt = txt.title()
txt = txt.split('_')
txt = ''.join(txt)
print(txt)