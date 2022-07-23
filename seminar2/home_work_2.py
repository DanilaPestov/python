#  1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sumnum (n):
    res = 0
    for num in str(n):
        if num == '.' or num == ',':
            continue
        res = res + int(num)
    return res

number = input('Введите число: ')
print(f'Сумма цифр -> {sumnum(number)}')

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

n = int(input("Введите число -> "))
for i in range(1, n+1):
    print(factorial(i), end=' ')

# 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input("Введите число n = "))

num = {}
for i in range(1,n+1):
    num[i] = (1+1/i)**i
print(num)
result = 0
for i in num:
    result += round(num[i])
print(f"Сумма: {round(result)}")  

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры пользователем.

n = int(input('Введите число n: '))
array = []
i = 0
for i in range(-n, n+1):
    array.append(i)
print(array)

a = int(input(f'позиция первого элемента от {(n*2+1)*-1} до {n*2}: '))
b = int(input(f'позиция второго элемента от {(n*2+1)*-1} до {n*2}: '))
print(f'Произведение элементов: {array[a]} * {array[b]} = {array[a] * array[b]}')


# 5 Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите значение n: '))
array = []
i = 0
for i in range(n+1):
    array.append(i)

print(f'Изначальный список: {array}')
random.shuffle(array)
print(f'Перемешанный список (1й способ): {array}')

def rnd (sp,n):
    spn = []
    spj = []
    i = 0
    while i <= n:
        j = random.randint(0,n)
        if j not in spj:
            spj.append(j)
            spn.append(sp[j])
            i += 1
    return spn
print(f'Перемешанный список (2й способ): {rnd(array,n)}')
