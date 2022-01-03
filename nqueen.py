# This is simple Sudoku solver using Backtracking DFS
import copy


def solve_n_queen(n):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = []
    board = [["."] * n for i in range(n)]  # nxn board filled with "."

    def backtrack(r):
        if r == n:
            board_copy = copy.deepcopy(board)
            res.append(board_copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res


user_input = input("Please select number of Queens: ")

result = solve_n_queen(int(user_input))

for row in result:
    for column in row:
        print(column)
    print("\n")
