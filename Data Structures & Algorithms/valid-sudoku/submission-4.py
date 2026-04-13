class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for r in range(9):
            joe = set()
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in joe:
                    return False
                joe.add(val)

        # columns
        for c in range(9):
            joe = set()
            for r in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in joe:
                    return False
                joe.add(val)

        # 3x3 boxes
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                joe = set()
                for r in range(3):
                    for c in range(3):
                        val = board[box_r + r][box_c + c]
                        if val == '.':
                            continue
                        if val in joe:
                            return False
                        joe.add(val)

        return True
