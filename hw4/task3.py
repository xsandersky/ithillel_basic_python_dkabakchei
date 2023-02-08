#1
x1 = int(input('Please enter an integer number: '))
print('Next number for number ' + str(x1) + ' is ' + str(x1 + 1), 'Previous number for number ' + str(x1) + ' is ' +  str(x1 - 1), sep='\n')
print()

#2
x2 = int(input('Please enter an integer number: '))
print('Next number for number ', x1, ' is ', x1 + 1, '\n', 'Previous number for number ', x1, ' is ', x1 - 1, sep='')
print()

#3
x3 = int(input('Please enter an integer number: '))
text = f'''Next number for number {x3} is {x3 + 1}.
Previous number for number {x3} is {x3 - 1}.'''
print(text)
print()

#4
x4 = int(input('Please enter an integer number: '))
print(f"Next number for number {x4} is {x4 + 1}. \nPrevious number for number {x4} is {x4 - 1}.")