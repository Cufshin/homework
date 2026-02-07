# Консольные крестики-нолики 3x3
# Ввод координат: строка столбец (от 1 до 3)

def print_board(field):
    print("\n   1   2   3")
    for i in range(3):
        print(f"{i + 1}  {field[i][0]} | {field[i][1]} | {field[i][2]}")
        if i != 2:
            print("  ---+---+---")


def check_game(field):
    # проверка строк
    for row in field:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return row[0]

    # проверка столбцов
    for col in range(3):
        if field[0][col] != " " and field[0][col] == field[1][col] == field[2][col]:
            return field[0][col]

    # диагонали
    if field[0][0] != " " and field[0][0] == field[1][1] == field[2][2]:
        return field[0][0]

    if field[0][2] != " " and field[0][2] == field[1][1] == field[2][0]:
        return field[0][2]

    # проверка на ничью
    for row in field:
        if " " in row:
            return None

    return "draw"


def get_move(field):
    while True:
        move = input("Введите ход (строка столбец): ").split()

        if len(move) != 2:
            print("Нужно ввести два числа.")
            continue

        if not move[0].isdigit() or not move[1].isdigit():
            print("Введите числа от 1 до 3.")
            continue

        r = int(move[0]) - 1
        c = int(move[1]) - 1

        if r < 0 or r > 2 or c < 0 or c > 2:
            print("Координаты должны быть от 1 до 3.")
            continue

        if field[r][c] != " ":
            print("Эта клетка уже занята.")
            continue

        return r, c


def main():
    field = [[" "] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(field)
        r, c = get_move(field)
        field[r][c] = current_player

        result = check_game(field)
        if result == "X" or result == "O":
            print_board(field)
            print(f"Победил игрок {result}")
            break
        elif result == "draw":
            print_board(field)
            print("Ничья")
            break

        current_player = "O" if current_player == "X" else "X"


main()
