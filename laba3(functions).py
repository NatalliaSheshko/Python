from functools import reduce

#1 Используя функцию map() переписать функцию
#items = [1, 2, 3, 4, 5]
#squared = []
#for i in items:
#    squared.append(i**2)
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
print (squared)

#2. Используйте функцию reduce() и перепишите код
#product = 1
#list = [1, 2, 3, 4]
#for num in list:
#    product = product * num
list = [1, 2, 3, 4]
product = reduce(lambda y, z : y * z, list)
print(product)

#3 Используйте функцию map() и перепишите код
#numbers = [1, 2, 3, 4, 5]
#squared = []
#for num in numbers:
#       squared.append(num ** 2)
#print(squared)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

#4 Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
x = [1, 2, 3]
y = [4, 5, 6]
res = list(zip(x, y))
print (res)

#5 Используйте функцию zip() чтобы преобразовать код:
#for i in range(len(name_hero)):
#    print(name_hero[i], '-', name_real[i])
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]
add = ['-', '-', '-', '-', '-', '-']
name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

name_hero_real = list(zip(name_hero, add, name_real))

print (name_hero_real)

# 6 С помощью функции filter() переместите из
# списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
odd = list(filter(lambda x: x % 2 != 0, numbers))
print(odd)
