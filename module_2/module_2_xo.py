def check_winner():
    for row in area:
        if row[0] == row[1] == row[2] and row[0] != '*':
            return row[0]

    for column in range(3):
        if area[0][column] == area[1][column] == area[2][column] and area[0][
            column] != '*':
            return area[0][column]


    if area[0][0] == area[1][1] == area[2][2] and area[0][0] != '*':
        return area[0][0]
    if area[0][2] == area[1][1] == area[2][0] and area[0][2] != '*':
        return area[0][2]

    return None

def draw_area():
    for i in area:
        print(*i)
    print()

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print("Добро пожаловать в крестики-нолики")
print("-----------------------------------")
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестики")
    row = int(input("Введите номер строки 0, 1 или 2: "))
    column = int(input("Введите номер столбца 0, 1 или 2: "))
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print("Пропускаете ход")
        draw_area()
        continue

    draw_area()

    winner = check_winner(area)
    if winner:
        print(f'Победитель: {winner}')
    else:
        print('Нет победителя')

    #if check_winner() == "X":
    #    print("Победа крестиков")
    #    break
    #elif check_winner() == "0":
    #    print("Победа ноликов")
    #    break
    #elif check_winner() == "*" and turn == 9:
    #    print("Ничья")
    #    break



