# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sumnum(n):
    res = 0
    for num in str(n):
        if num == '.' or num == ',':
            continue
        res = res + int(num)
    return res


number = input('Введите число: ')
res = sum(map(sumnum, number))
print(res)

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Введите число -> "))
for i in range(1, n+1):
    print(factorial(i), end=' ')

res = list(n for n in range(1, n+1))
li=list(map(lambda n: factorial(n), res))
print(li)

# 3. Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите значение n: '))
array = [i for i in range(n+1)]
print(f'Изначальный список: {array}')
array_new = map(random.shuffle(array), array)
print(f'Перемешанный список: {array}')

# 4. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

from random import randint

num = [randint(1, 10) for i in range(10)]
print(num)
sumnum = [num[i] for i in range(1, len(num), 2)]
# sumnum = list(filter(lambda i: not i%2, num))
print(sumnum)
print(f'Сумма элементов, стоящих на нечетных позициях: {sum(sumnum)}')


# Задача №4. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def list_pos(n):
    my_li = [((1 + 1/i)**i) for i in range(1, n + 1)]
    new_list = dict(enumerate(my_li))
    print(new_list)
    print(f'сумма: ')
    return sum(my_li)

print(list_pos(4))
