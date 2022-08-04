# my_str = '1, 22, 54, 76, 2'.split(', ')
# # что сделать с элементом, с каким элементом, условие
# my_list = [int(item) for item in my_str if (item > '21')]
# print(my_list)

# # lambda
# f = lambda x: x**2 if x > 10 else x**3
# my_list = [12, 54, 3, 56]
# # # # for item in my_list:
# # # #     f(item)
# # # #     print(f(item))
# # # res = list(map(f, my_list))
# # # print(res)
# # res = list(filter(f, my_list))
# # print(res)

# # zip
# f = lambda x: True if x > 10 else False
# my_list_1 = ['a', 'b', 'c', 'd']
# my_list_2 = [15, 76, 1, 98]
# my_list_3 = [65, 68]

# res = list(zip(my_list_1, my_list_2, my_list_3))

# print(res)

# # enumerate
# my_list_1 = ['a', 'b', 'c', 'd']
# res=list(enumerate(my_list_1))
# print(res)

# # 1. удалить из исходной строки все слова с "абв"

# str_list = 'привет мир! мы очабв любим пайтонабв! семинары'

# # def string(str):
# #     for i in str_list:
# #         if 'абв' in i:
# #             str_list.remove(i)
# #     print(str_list)


# # string(str_list)

# # res = list(filter(lambda i: 'абв' not in i, str_list.split()))
# # print(res)

# res = [word for word in str_list.split() if 'абв' not in word]
# print(' '.join(res))
