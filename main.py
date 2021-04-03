import os

# constants
cross_id = 1
nought_id = 2


def gamestat(f: list):
    for j in range(3):
        print(f[j][0] + f[j][1] + f[j][2])


def makemove(f: list, player: int):
    while True:
        try:
            space = int(input("SELECT SPACE (1-9): "))  # except no longer in popa
        except:
            print("[BAD INPUT]")
        if space in range(1, 10):
            row = (space - 1) // 3
            column = (space - 1) % 3
            if f[row][column] == '-':
                f[row][column] = 'X' if player == 1 else 'O'
                break
            else:
                print("[SPACE ALREADY OCCUPIED]")
        else:
            print("[BAD INPUT]")


def checkwin(f: list):
    for k in range(3):
        if f[k][0] == f[k][1] == f[k][2] != '-':
            return cross_id if f[k][0] == "X" else nought_id
        elif f[0][k] == f[1][k] == f[2][k] != '-':
            return cross_id if f[0][k] == "X" else nought_id
    if f[0][0] == f[1][1] == f[2][2] != '-':
        return cross_id if f[0][0] == "X" else nought_id
    elif f[0][2] == f[1][1] == f[2][0] != '-':
        return cross_id if f[0][2] == "X" else nought_id
    else:
        return 0

def main():
    field = [['-','-','-'],['-','-','-'],['-','-','-']]
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
