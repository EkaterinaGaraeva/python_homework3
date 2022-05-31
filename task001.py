# 1. Найти НОК двух чисел

import math
import random

n = random.randint(2, 99)
m = random.randint(2, 99)

print(f'НОК чисел {n} и {m} равен {(n * m) // math.gcd(n , m)}')

def find_nok(a, b):
    i = min(a, b)
    while True:
        if i%a==0 and i%b==0:
            break
        i += 1
    return i

print(f'НОК чисел {n} и {m} равен {find_nok(n, m)}')
