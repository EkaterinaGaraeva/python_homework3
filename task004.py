# 4. Дана последовательность чисел. Получить список неповторяющихся элементов 
# исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

from random import randint

def list_of_non_repeating_elements(list_of_numbers):
    list_of_elements = []
    for i in list_of_numbers:
        if i not in list_of_elements:
            list_of_elements.append(i)
    list.sort(list_of_elements)
    return list_of_elements


lst = [randint(0, 9) for i in range(10)]
print(lst)
print(list_of_non_repeating_elements(lst))

