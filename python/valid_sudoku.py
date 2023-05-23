class Solution(object):
    def isValidSudoku(self, board):
        def calc_box(i, j):
            box = None
            if i < 3:
                if j < 3:
                    box = 0
                elif j < 6:
                    box = 1
                else:
                    box = 2
            elif i < 6:
                if j < 3:
                    box = 3
                elif j < 6:
                    box = 4
                else:
                    box = 5
            else:
                if j < 3:
                    box = 6
                elif j < 6:
                    box = 7
                else:
                    box = 8
            return box

        r = {}
        c = {}
        b = {}
        dicts = [r, c, b]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]

                if num not in r:
                    r[num] = [i]
                    c[num] = [j]
                    b[num] = [calc_box(i, j)]
                else:
                    r[num].append(i)
                    c[num].append(j)
                    b[num].append(calc_box(i, j))

        for d in dicts:
            for k, v in d.items():
                for item in v:
                    if v.count(item) > 1 and k != ".":
                        return False
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
