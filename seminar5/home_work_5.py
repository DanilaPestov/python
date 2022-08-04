# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'добрый мабвый день! как пройти к забвнему выходу?'
word_mis = 'абв'


def del_word(text, word):
    text = text.split()
    for i in text:
        if word in i:
            text.remove(i)
    return text


res = del_word(text, word_mis)
print(' '.join(res))


# list comprehension
res1 = [i for i in text.split() if word_mis not in i]
print(' '.join(res1))

# filter
res2 = list(filter(lambda i: word_mis not in i, text.split()))
print(' '.join(res2))


# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

from random import randint

player1 = input("Введите имя игрока 1: ")
player2 = input("Введите имя игрока 2: ")
fst_cnd = int(input("Сколько конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первым ходит игрок {player1}")
else:
    print(f"Первым ходит игрок {player2}")

def sweet(player):
    x = int(input(f"{player}, возьми от 1 до 28 конфет: "))
    while x < 1 or x > 28:
        x = int(input(f"{player}, надо от 1 до 28 конфет: "))
    return x


def res(player, k, counter, end_cnd):
    print(f"Игрок {player}, взял {k} конфет, у него {counter} конфет. Осталось {end_cnd} конфет.")


counter1 = 0
counter2 = 0

while fst_cnd > 28:
    if flag:
        k = sweet(player1)
        counter1 += k
        fst_cnd -= k
        flag = False
        res(player1, k, counter1, fst_cnd)
    else:
        k = sweet(player2)
        counter2 += k
        fst_cnd -= k
        flag = True
        res(player2, k, counter2, fst_cnd)

if flag:
    print(f"Поздавляем! Выиграл игрок {player1}, УРА!")
else:
    print(f"Поздравляем! Выиграл игрок {player2}, УРА!")


# 3. Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))


def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# с данной задачай почувствовал себя собакой, взял решение у одногруппников, смотрел вроде что то понял, но сам подобное не напишу, 
# по идее надо было написать код, что бы он сам создавал файл, а данный работает при налии файла с текстом в папке

with open('/Users/pest/Documents/Учеба (Разработчик)/python/seminar5/first_file.txt', 'r') as data:
    my_str = data.read()

def code_rle(sl):
    str_code = ''
    prev_char = ''
    count = 1
    for char in sl:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = code_rle(my_str)
print(str_code)
one_str = str_code

with open('/Users/pest/Documents/Учеба (Разработчик)/python/seminar5/cod_file.txt', 'w') as data:
    data.write(one_str)