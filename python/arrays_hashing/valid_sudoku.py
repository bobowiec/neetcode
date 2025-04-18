import collections
from typing import List


class Solution:

    # Time complexity: O(n^2), Space complexity: O(n^2), where n = 9
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set())
        columns = collections.defaultdict(set())
        squares = collections.defaultdict(set()) # key: a pair (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                char = board[r][c]

                if char == ".":
                    continue
                if char in rows[r] or char in columns[c] or char in squares[(r // 3, c // 3)]:
                    return False
                rows[r].add(char)
                columns[c].add(char)
                squares[(r // 3, c // 3)].add(char)
        return True
    
    # Brute Force: Time complexity: O(n^2), Space complexity: O(n^2), where n = 9
    def isValidSudokuBruteForce(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True