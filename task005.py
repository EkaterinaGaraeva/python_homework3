# 5. Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

import random

text_file = open('file.txt', 'w')
for i in range(random.randint(0, 10)):
    index = random.randint(0, 10)
    text_file.write(str(index) + '\n')
text_file.close()

data = open('file.txt', 'r')
data_string = ''
print(f'Числа из файла:')
for line in data:
    print(f'{line.rstrip()}')
    if int(line) % 2 != 0:
        data_string += line

print(f'\nНечетные числа \n{data_string}')

text_file = open('file.txt', 'w')
text_file.write(data_string)

