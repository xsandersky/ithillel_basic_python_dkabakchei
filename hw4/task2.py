# solution ONLY with 'find'
human_info = input()
a = human_info.find('*')
data_1 = int(human_info[a + 1:a + 5])
b = human_info[::-1].find('*')
data_2 = int(human_info[::-1][b - 1:b - 5:-1])
old = data_2 - data_1
print('Name:', human_info[:a])
print('Age:', old, 'years')

print()

# solution with 'find' and 'rfind'
h_i = 'Taras Shevchenko*1814-03-09*1861-03-10' # через хардкод реализовал
x1 = h_i.find('*')
born = int(h_i[x1 + 1: x1 + 5])
x2 = h_i.rfind('*')
death = int(h_i[x2 + 1: x2 + 5])
age = death - born
print('Name:', h_i[:x1])
print('Age:', age, 'years')