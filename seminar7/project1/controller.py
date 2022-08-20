from re import X
from init import input_num
from calculator import s, m, su, d
from view import print_num


def get_num():
    a = (input_num())
    c = input('действие: ')
    b = (input_num())
    if c == '+':
        print(f'{a} {c} {b} = {s(a, b)}')
    elif c == '*':
        print(f'{a} {c} {b} = {m(a, b)}')
    elif c == '-':
        print(f'{a} {c} {b} = {su(a, b)}')
    elif c == '/':
        print(f'{a} {c} {b} = {d(a, b)}')

