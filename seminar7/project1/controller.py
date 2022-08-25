from init import input_num
from calculator import s, m, su, d
from view import print_num
from loggirovanie import timer
from data import init_data


def get_num():
    a = (input_num())
    c = input('действие: ')
    b = (input_num())
    init_data(a,b,c)
    timer((a, c, b))
    if c == '+':
        print_num(f'{a} {c} {b} = {s(a, b)}')
    elif c == '*':
        print_num(f'{a} {c} {b} = {m(a, b)}')
    elif c == '-':
        print_num(f'{a} {c} {b} = {su(a, b)}')
    elif c == '/':
        print_num(f'{a} {c} {b} = {d(a, b)}')

