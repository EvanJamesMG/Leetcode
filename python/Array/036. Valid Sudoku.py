'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''
'''
给定部分棋盘，验证数独游戏的有效性。
每一行，每一列，每个3*3的区域（不重复的区域）不能出现重复数字
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y] == tmp: return False
            for i in range(9):
                if board[x][i] == tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[(x / 3) * 3 + i][(y / 3) * 3 + j] == tmp: return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                tmp = board[i][j]
                board[i][j] = 'D'
                if isValid(i, j, tmp) == False:
                    return False
                else:
                    board[i][j] = tmp
        return True        
