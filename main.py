import os

# constants
cross_id = 1
nought_id = 2


def gamestat(f: dict):
    for j in range(1, 4):
        print(f[j][1] + f[j][2] + f[j][3])


def makemove(f: dict, player: int):
    while True:
        try:
            space = int(input("SELECT SPACE (1-9): "))
            if space in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                row = (space - 1) // 3
                column = (space - 1) % 3
                if f[row][column] == '-':
                    f[row][column] = 'X' if player == 1 else 'O'
                    break
                else:
                    print("[SPACE ALREADY OCCUPIED]")
            else:
                print("[BAD INPUT]")
        except:
            print("[BAD INPUT]")


def checkwin(f: dict):
    for k in range(1, 4):
        if f[k][1] == f[k][2] == f[k][3] != '-':
            return cross_id if f[k][1] == "X" else nought_id
        elif f[1][k] == f[2][k] == f[3][k] != '-':
            return cross_id if f[1][k] == "X" else nought_id
    if f[1][1] == f[2][2] == f[3][3] != '-':
        return cross_id if f[1][1] == "X" else nought_id
    elif f[1][3] == f[2][2] == f[3][1] != '-':
        return cross_id if f[1][3] == "X" else nought_id


def main():
    field = {1: {1: '-', 2: '-', 3: '-'}, 2: {1: '-', 2: '-', 3: '-'}, 3: {1: '-', 2: '-', 3: '-'}}
    winner_id = 0
    os.system('cls')
    for move in range(1, 10):
        player_id = cross_id if move % 2 != 0 else nought_id
        gamestat(field)
        print(f"PLAYER {player_id} GO:")
        makemove(field, player_id)
        winner_id = checkwin(field)
        os.system('cls')
        if winner_id != 0:
            gamestat(field)
            print(f'PLAYER {winner_id} HAS WON IN {move} moves!')
            break
    if winner_id == 0:
        print("DRAW!")


if __name__ == "__main__":
    main()



