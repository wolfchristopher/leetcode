


def gameOfLife(board) -> None:
    # Original | New | State
    #    0     |  0  |   0
    #    1     |  0  |   1
    #    0     |  1  |   2
    #    1     |  1  |   3

    ROWS, COLS = len(board), len(board[0])

    def countNeighbours(row, col):
        neighbours = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if ((i == row and j == col) or i < 0 or j < 0 or i >= ROWS or j >= COLS):
                    continue
                if board[i][j] in [1, 3]:
                    neighbours += 1
        return neighbours

    for row in range(ROWS):
        for col in range(COLS):
            neighbours = countNeighbours(row,col)
            if board[row][col]:
                if neighbours in [2, 3]:
                    board[row][col] = 3
            elif neighbours == 3:
                board[row][col] = 2

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                board[row][col] = 0
            elif board[row][col] in [2, 3]:
                board[row][col] = 1









