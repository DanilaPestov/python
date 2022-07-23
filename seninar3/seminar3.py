# # 1 задайте список. напишите программу присутствует ли в списке некое число

# a = ['asd12', '12', 'asd', '87']
# for i in a:
#     if '12' in i:
#         print(i)

# # 2 напишите программу, которая определит позицию второго вхоюдения строки в списке

# a = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
# count = 0
# for i in range(len(a)):
#     if a[i] == 'qwe':
#         count += 1
#         if count > 1:
#             print(i)
#             break

# 3 реализуйте алгоритм случайных чисел без использования встроенного генераторв псевдослучайных чисел

import time
def find_num(x):
    a = str(time.time())
    b = ''
    count = 1
    while count <= x:
        b += a[-count]
        count += 1
    return int(b)
   
print(find_num(4))
