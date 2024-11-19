import math

import numpy as np
import random
from numpy import number

#1
#По введенному числу (от 0 до 7) напечатать название цифры.
n = int(input("Enter a number from 1 to 7: "))
if n == 1:
    print("One")
elif n == 2:
    print("Two")
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Five")
elif n == 6:
    print("Six")
elif n == 7:
    print("Seven")
else:
    print("You enter incorrect number")


#2
# Натуральное число, записанное в десятичной системе счисления, называется сверхпростым, если оно
# остается простым при любой перестановке своих цифр. Определить все сверхпростые числа до n.

n = int(input("Enter a number: "))
if n == 2:
    print(n)
for i in range(1, n + 1, 2):#иду с шагом 2
    is_prime = True
    for j in range(3, int(math.sqrt(i)) + 1):
        if i % j == 0: #проверяю, делится ли число без остатка
            is_prime = False
            break
    if is_prime:
        print(i)

#3
# Сформировать одномерный список целых чисел A, используя генератор случайных чисел
# (диапазон от 0 до 99). Размер списка n ввести с клавиатуры. В соответствии со своим вариантом
# Найти номера минимального и максимального элементов первой половины списка


n = int(input("Enter a number: "))
mas = [random.randint(0,99) for i in range(n)]
print(mas)
halfMas = len(mas)//2
halves = mas[:halfMas], mas[halfMas:]
firstHalfMas = halves[0]
print(firstHalfMas)
maxi = max(firstHalfMas)
maxInd = mas.index(maxi)
mini = min(firstHalfMas)
minInd = mas.index(mini)
print(f"Номер максимального элемента = {maxInd}\n")
print(f"Номер минимального элемента = {minInd}")


