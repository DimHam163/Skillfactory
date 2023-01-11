# ПЛАН: 1 - написать функцию для вывода в консоль нашего игрового поля start_board
#       2 - написать функцию для принятия (ввода) пользователем, то что он ставит в виде 'Х' или '0' и определения что именно он ввел! обозначим ее  player_input
#       3 - написать функцию тчобы можно было проверить есть ли выигрышная комбинация
start_board = list(range(1, 10))  # для начала создаем список из цифр в виде массива
win_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5,
                                                                                                 7)]  # назначаем переменную, где будут храниться выигрышные комбинации при помощи кортежа, который в отличии списка не изменяется (я данный модуль повторил снова и снова)))


def paint_board():  # рисуем доску
    print(''' Hello in\n the Game''')  # функцию для вывода в консоль нашего игрового поля start_board
    for i in range(3):
        print('|', start_board[0 + i * 3], '|', start_board[1 + i * 3], '|', start_board[2 + i * 3],
              '|')  # берем значения из списка start_board и выводим числа обозначающие клетки нашего поля
    print("   Go !!! ")


def player_input(player_XO):  # функция которая выводит символ введенный пользователем
    while True:
        tap = input('В какое поле поставить: ' + player_XO)  # пользователь вводит один из симоволов XO
        if not (tap in '123456789'):  # если пользователь ввел цифру не из этого списка
            print('Увы, такой клетки нет, повторите попытку:')  # водится данное сообщение
            continue  # и даем пользователю вновь ввсети данные, то есть повторяем цикл
        tap = int(tap)  # приобразем в целое число
        if str(start_board[tap - 1]) in 'X0':  # далее проверяем занята ли клетка введенная пользователем,  в связи  с чем указываем -1 так как индекс поля начинается с 0
            print('Данная клетка занята')
            continue  # после чего повторяем цикл palyer_input, чтобы польователь вновь смог выбрать свободную клетку
        start_board[
            tap - 1] = player_XO  # если пользователь ввел свободную клетку, то прерываем крайний цикл и предоставляем вновь ввести данне клетки
        break


def win_():  # функция которая проверяет выигрышную клетку
    for a in win_combination:  # вторая глобальная переменная
        if (start_board[a[0] - 1]) == (start_board[a[1] - 1]) == (start_board[a[2] - 1]):
            # то есть интерпретатор будет проверять каждый кортеж указанные в переменной,
            # то есть обращаемся к каждому инжекусу наших цифр по этому отнимаем от каждого элемента 1
            # так как списки у нас начинаются с 1 с индексмо 0. Если после перебора клеток (данные указанные в кортежах) будут равны то значит True
            return start_board[a[1] - 1]  # то мы возвращаем а 1 - 1
    else:
            return False  # если нет выигрышной комбинации, то функция будет возвращать False


def main():  # функция для подсчтеа победы
    counter = 0
    while True:
        paint_board()
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        if counter > 3:
            winners = win_()
            if winners:
                paint_board()
                print(winners, '-  ' "Победа!!!")
                break
        counter += 1
        if counter > 8:
            paint_board()
            print(' "Победила Дружба" ')
            break

main()
