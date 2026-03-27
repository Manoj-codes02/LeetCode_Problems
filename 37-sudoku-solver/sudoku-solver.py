class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Pre-fill sets and store empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i//3)*3 + j//3].add(val)

        def backtrack(index):
            if index == len(empty):
                return True

            row, col = empty[index]
            box = (row//3)*3 + col//3

            for num in range(1, 10):
                d = str(num)

                if d not in rows[row] and d not in cols[col] and d not in boxes[box]:
                    board[row][col] = d
                    rows[row].add(d)
                    cols[col].add(d)
                    boxes[box].add(d)

                    if backtrack(index + 1):
                        return True

                    # backtrack
                    board[row][col] = "."
                    rows[row].remove(d)
                    cols[col].remove(d)
                    boxes[box].remove(d)

            return False

        backtrack(0)