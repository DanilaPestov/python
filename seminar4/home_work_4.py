# 1. Вычислить число c заданной точностью d
# при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}

import math

d = float(input('Задайте точность d: '))
count = 0
while d % 1 != 0:
    d *= 10
    count += 1
print(round(math.pi, count))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def f(x):
    res = []
    n = 2
    while x > 1:
        if x % n == 0:
            res.append(n)
            x /= n
        else:
            n += 1
    return res

x = int(input('Введите натуральное число x: '))
print(f'Список простых множителей числа {x} ->', f(x))

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# пример: [0, 4, 2, 5, 4, 5, 3, 5, 2] -> [0, 4, 2, 5, 3]

spisok = input('Задайте последовательность чисел через пробел: ').split(' ')
spisok = [int(x) for x in spisok]
new = [0]
for i in range(1,len(spisok)):
    for j in range(0, i):
        val = True
        if spisok[j] == spisok[i]:
            val = False
            break
    if val == True:
        new.append(spisok[i])
print(spisok, '->', new)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите натуральную степень k = '))
ko = []
for i in range(0, k+1):
    ko.append(random.randint(0, 10))

line = ''
for i in range(0, k+1):
    if i == 0:
        if ko[i] > 0:
            line = line+'+'+str(ko[i])+'=0'
        else:
            line = line+'=0'
    elif i == 1:
        if ko[i] > 1:
            line = str(ko[i])+'*x'+line
        elif ko[i] == 1:
            line = 'x'+line
    else:
        if ko[i] > 1:
            line = str(ko[i])+'*x^'+str(i)+'+'+line
        if ko[i] == 1:
            line = 'x^'+str(i)+'+'+line
ko.reverse()
print(ko)
print(f'{k=}->', line)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def funcwrite(text, ko): 
    with open(text, 'w', encoding='utf-8') as file:
        for i in ko:
            file.write(f'{i} ')
    return

def funcread(text):  
    ko = []
    with open(text, 'r', encoding='utf-8') as file:
        a = file.readline().split(' ')
        for i in range(0, len(a)-1):
            ko.append(int(a[i]))
    return ko

k = int(input('Введите натуральную степень k = '))  
ko1 = []
ko2 = []
for i in range(0, k+1):
    ko1.append(random.randint(-10, 10)) 
    ko2.append(random.randint(-10, 10))  
funcwrite('file1.txt', ko1)
funcwrite('file2.txt', ko2)
ko3 = []
ko3 = funcread('file1.txt')
print(ko3, '- Первый список коэффициентов многочлена')
ko4 = []
ko4 = funcread('file2.txt')
print(ko4, '- Второй список коэффициентов многочлена')
ko5 = []
for i in range(0, len(ko3)):  
    ko5.append(ko3[i]+ko4[i])
print(ko5, '- сумма коэффициентов многочленов')
ko5.reverse()
line = ''
for i in range(0, k+1):
    if i == 0:
        if ko5[i] > 0:
            line = line+'+'+str(ko5[i])+'=0'
        elif ko5[i] < 0:
            line = line+str(ko5[i])+'=0'
        else:
            line = line+'=0'
    elif i == 1:
        if ko5[i] > 1:
            line = str(ko5[i])+'*x'+line
        if ko5[i] < 1:
            line = '('+str(ko5[i])+'*x)'+line
        elif ko5[i] == 1:
            line = 'x'+line
    else:
        if ko5[i] > 1:
            line = str(ko5[i])+'*x^'+str(i)+'+'+line
        elif ko5[i] < 1:
            line = '('+str(ko5[i])+'*x^'+str(i)+')+'+line
        elif ko5[i] == 1:
            line = 'x^'+str(i)+'+'+line
print(line)
funcwrite('fileSumma.txt', line)