board = ["1","2","3","4","5","6","7","8","9"]

for i in range(9):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    move = int(input(("X" if i % 2 == 0 else "O") + " move: "))
    board[move - 1] = "X" if i % 2 == 0 else "O"