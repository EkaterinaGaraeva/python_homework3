# 3. Составить список простых множителей натурального числа N

# Решето Эратосфена
def simple_multipliers(n):
    simple_mult = []
    for i in range(n + 1):
        simple_mult.append(i)
    simple_mult[1] = 0
    i = 2
    while i <= n:
        if simple_mult[i] != 0:
            j = i + i
            while j <= n:
                simple_mult[j] = 0
                j = j + i
        i += 1
    simple_mult = set(simple_mult)
    simple_mult.remove(0)
    return simple_mult

def list_of_all_multipliers(n):
    list_of_multipliers = []
    for i in range(2, n + 1):
        if (int(n % i) == 0):
            list_of_multipliers.append(i)
    if len(list_of_multipliers) == 1:
        list_of_multipliers == [n]
    return list_of_multipliers
        
def list_of_simple_multipliers(list_of_multipliers):
    simple_multipliers = []
    for j in list_of_multipliers: 
        if (len(list_of_all_multipliers(j)) == 1):
            simple_multipliers.append(j)  
    return simple_multipliers

number = 100 # простые числа до 100
n = 46

print(f'Простые числа до {number}: {simple_multipliers(number)}')
print(f'Все множители числа N = {n} (кроме 1): {list_of_all_multipliers(n)}')
print(f'Простые множители числа N = {n}: {list_of_simple_multipliers(list_of_all_multipliers(n))}')



