# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

def sum(num):
    result = 0
    for i in range(1, len(num), 2):
        result += num[i]
        print(f'{num[i]}', end=' ')
    return result

num = [2, 3, 5, 9, 3]
print(f'\nСумма элементов, стоящих на нечетных позициях: {sum(num)}')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list_num = [2, 3, 4, 5, 6]
i = 0
print(list_num)
while i < len(list_num)/2:
    result = list_num[i] * list_num[len(list_num)-1-i]
    i += 1
    print(result, end=' ')

# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def func(x):
    min = x[0] % 1
    max = x[0] % 1
    y = []
    for i in range(len(x)):
        y.append(round(x[i] % 1, 2))
        if y[i] < min and y[i] != 0:
            min = y[i]
        if y[i] > max:
            max = y[i]
    return max, min

num = [1.1, 1.2, 3.1, 5, 10.01]
max, min = func(num)
print(num)
print(round((max-min), 2))

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def func(n: int) -> str:
    num = ''
    while n > 0:
        num += str(int(n % 2))
        n //= 2
    return num
number = int(input('Введите число: '))
print(f'десятичное число {number} -> двоичное число {func(number)}')

# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(k):
    if k < 0:
        if k in [-1]:
            return 1
        elif k in [-2]:
            return -1
        else:
            return fib(k+2)-fib(k+1)
    else:
        if k in [1, 2]:
            return 1
        else:
            return fib(k-1)+fib(k-2)


k = int(input('Введите число: '))
list = []

for i in range(-k, k+1):
    list.append(fib(i))
print(list)
