#1
x1 = int(input())
print('Please enter an integer number: ' + str(x1), 'Next number for number ' + str(x1) + ' is ' + str(x1 + 1), 'Previous number for number ' + str(x1) + ' is ' +  str(x1 - 1), sep='\n')
print()

#2
x2 = int(input())
print('Please enter an integer number: ', x1, '\n', 'Next number for number ', x1, ' is ', x1 + 1, '\n', 'Previous number for number ', x1, ' is ', x1 - 1, sep='')
print()

#3
x3 = int(input())
text = f'''Please enter an integer number: {x3}
Next number for number {x3} is {x3 + 1}.
Previous number for number {x3} is {x3 - 1}.'''
print(text)
print()

#4
x4 = int(input())
print(f"Please enter an integer number: {x4} \nNext number for number {x4} is {x4 + 1}. \nPrevious number for number {x4} is {x4 - 1}.")