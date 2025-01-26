from random import randrange

import numpy as np

#Вариант 1
#Удалить в списке все числа, которые повторяются более двух раз.
mas = [randrange(1, 5) for i in range(15)]
print (mas)
res = []
for i in mas:
    if i not in res:
        res.append(i)
print(res)


#Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.
mas = [randrange(1, 10) for i in range(20)]
print (mas)
n = int(input("Enter a number: "))
sum = 0

mas2 = []
for i in mas:
    if i > n:
        continue
    elif i < n:
        if i + sum > n:
            continue
        elif i + sum < n:
            mas2.append(i)
            sum += i
        elif i + sum == n:
            mas2.append(i)
            break
    elif i == n:
        mas2 = [i]
        break
print (f'Подмножество данного множества чисел, что сумма его элементов равна {n}: {mas2}')


mas2 = []
for i in mas:
    if i > n:
        print("i > entered number")
    elif i < n:
        if i + sum < n:
            mas2.append(i)
            sum += i
        elif i + sum > n:
            continue
        elif i + sum == n:
            mas2.append(i)
    elif i == n:
        mas2 = mas
        break
print (mas2)


#Вариант 5
#Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.

mas = [randrange(1, 10) for i in range(10)]
print (mas)

minimum = mas[0]
for i in range(1, len(mas)):
    if mas[i] < minimum:
        minimum = mas[i]
if minimum % 2 == 0:
    print(f"Наименьший четный элемент списка: {minimum}")
else:
    print(f'Первый элемент списка: {mas[0]}')

#Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.
a = [9, 10, 5, 6, 0, 0, 5, 0]
print(a)
zero = []
other = []
res = []
for i in a:
    if i == 0:
        zero.append(i)
    else:
        other.append(i)
res = zero + other
print(res)


# Задачние 2.
# 3. Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме
# элементов, стоящих на том же месте в 1-й и 2-й таблицах.

mas1 = np.array([[1,2],[3,4]])
mas2 = np.array([[5,6],[7,8]])

mas3 = mas1 + mas2
print(mas3)