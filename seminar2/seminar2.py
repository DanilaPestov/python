# # 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# def searchNumber(a: int, b: int) -> list:
#     my_list = [1]
#     while len(my_list) < a:
#         my_list.append(my_list[-1]*b)
#     return my_list


# print(searchNumber(5, -3))

# # def func(x):
# #     s = 1
# #     print(s, end=' ')
# #     for i in range(1, x):
# #         s = s * (-3)
# #         print(s, end=' ')
# # n = int(input())
# # func(n)

# # 2. Напишите программу, в которой пользователь будет задавать две строки,
# # а программа - определять количество вхождений одной строки в другой.

# st1 = 'привет, привет привет, мир'
# st2 = 'привет'
# def finder(a: str, b: str):
#     t = 0
#     for i in range(len(a) - len(b)):
#         if (a[i : i + len(b)] == b):
#             t += 1
#     return t
# print(finder(st1,st2))

def find_line(string:str, under_strind:str):
    print(string.count(under_strind))

user_string = input('Введите текст: ')
user_understring = input('Введите текст: ')
find_line(user_string, user_understring)
