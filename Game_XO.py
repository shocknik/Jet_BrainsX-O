# -*- coding: utf-8 -*-
global winer
global user_move
global user_move1
prev_XoY = [(j, i) for j in range(1, 4) for i in range(1, 4)]
XoY = [[prev_XoY[j * 3 + i] for i in range(3)] for j in range(3)]  # система координат(двухмерный массив)
winer = False
def fun_input():
    global user_move
    global user_move1
    user_move = input('Enter the coordinates:')
    lst = user_move.split()
    while lst[0].isdigit() is False or lst[1].isdigit() is False:
        print("You should enter numbers!")
        user_move = input()
        lst = user_move.split()
    user_move1 = tuple(int(x) for x in user_move.split())


def check_corr(par):  # функция корректности ввода координат и печать обновленного поля
    step_full = False
    while step_full == False:
        for i in range(3):
            for j in range(3):
                if user_move1 == XoY[i][j] and field_xo[i][j] != '_':
                    print("This cell is occupied! Choose another one!")
                    fun_input()
                elif user_move1[0] > 3 or user_move1[1] > 3:
                    print("Coordinates should be from 1 to 3!")
                    fun_input()
                elif user_move1 == XoY[i][j] and field_xo[i][j] == '_':
                    field_xo[i][j] = par
                    step_full = True
    print('---------')
    for i in range(len(field_xo)):
        print('|', end=' ')
        for j in range(len(field_xo[i])):
            print(field_xo[i][j], end=' ')
        print('|')
    print('---------')


def analysis_field():  # функция анализа поля
    global winer
    winer = False
    count_of_x = one_str.count('X')
    count_of_o = one_str.count('O')
    Impossible = False
    if (count_of_x >= 2 * count_of_o or count_of_o >= 2 * count_of_x) and (count_of_o > 0 and count_of_x > 0):
        print('Impossible')
        Impossible = True
    for i in range(2):
        if field_xot[i] == ['X', 'X', 'X'] and field_xot[i - 1] == ['O', 'O', 'O'] and Impossible is False:
            Impossible = True
            print('Impossible')
            break
        if field_xot[i] == ['O', 'O', 'O'] and field_xot[i - 1] == ['X', 'X', 'X'] and Impossible is False:
            Impossible = True
            print('Impossible')
            break
    a = False
    b = False
    c = False
    e = False
    i = 0
    j = 0
    # сравнение элементов поля
    for i in range(len(field_xo)):
        if field_xo[i][j] == field_xo[i][j - 1] == field_xo[i][j - 2] and Impossible is False:
            a = True
            if field_xo[i][j] == 'X':
                print('X wins')
                winer = True
            elif field_xo[i][j] == 'O':
                print('O wins')
                winer = True
            break
    for j in range(len(field_xo[i])):
        if field_xo[i][j] == field_xo[i - 1][j] == field_xo[i - 2][j] and a is False and Impossible is False:
            b = True
            if field_xo[i][j] == 'X':
                print('X wins')
                winer = True
            elif field_xo[i][j] == 'O':
                print('O wins')
                winer = True
            break

    for i in range(len(field_xo)):
        for j in range(len(field_xo[i])):
            if field_xo[i][j] == ' ' or field_xo[i][j] == '_' and a is False and b is False and Impossible is False:
                print('Game not finished')
                c = True
            break
    if field_xo[1][1] == field_xo[0][0] == field_xo[2][2] or field_xo[1][1] == field_xo[0][2] == field_xo[2][0]:
        if field_xo[1][1] == 'X':
            c = True
            print('X wins')
            winer = True
        elif field_xo[1][1] == 'O':
            print('O wins')
            winer = True
            c = True
    if a is False and b is False and c is False and e is False and Impossible is False:
        print('Draw')
# создание поля

one_str = ['_' for n in range(9)]  # ввод элементов поля (х и 0)
field_xo = [[one_str[j + 3 * i] for j in range(3)] for i in range(3)]  # создание матрицы 3*3 из введенного списка
field_xot = [[one_str[3 * j + i] for j in range(3)] for i in range(3)]  # транспонированная матрица
print('---------')  # создание поля и распечатка (начало)
for i in range(len(field_xo)):
    print('|', end=' ')
    for j in range(len(field_xo[i])):
        print(field_xo[i][j], end=' ')
    print('|')
print('---------')  # создание поля и распечатка (окончание)


count_of_step = 0
move_x = True
move_o = False
while count_of_step < 9 and winer is False:
    if move_x is True:  # ход игрока Х
        fun_input()  # функция ввода координат
        check_corr('X')  # проверка правильности ввода и печать
        analysis_field()  # анализ поля
        move_x = False
        move_o = True
        count_of_step += 1
    elif move_o is True:  # ход игрока O
        fun_input()  # функция ввода координат
        check_corr('O')  # проверка правильности ввода и печать
        analysis_field()  # анализ поля
        move_x = True
        move_o = False
        count_of_step += 1
    continue



