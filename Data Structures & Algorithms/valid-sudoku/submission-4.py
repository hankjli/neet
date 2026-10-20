class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check each row
        for row in board:
            seen = set()

            for char in row:
                if char != ".":
                    if char in seen:
                        return False
                    seen.add(char)
        
        # check each col
        for col in range(9):
            seen = set()

            for row in board:
                char = row[col]

                if char != ".":
                    if char in seen:
                        return False
                    seen.add(char)

        # check each sub-box

        # row indices are row * 3 to row * 3 + 3
        # col indices are col * 3 to col * 3 + 3
        for row in range(3):
            for col in range(3):

                seen = set()

                for r in range(row * 3, row * 3 + 3):
                    for c in range(col * 3, col * 3 + 3):
                        char = board[r][c]

                        if char != ".":
                            if char in seen:
                                return False
                            seen.add(char)

        return True