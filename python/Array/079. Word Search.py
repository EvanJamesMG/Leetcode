# coding=utf-8
'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


'''
使用dfs来搜索，为了避免已经用到的字母被重复搜索，将已经用到的字母临时替换为'#'就可以了

'''


class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x, y, word):
            if len(word) == 0: return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x - 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # down
            if x < len(board) - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y - 1, word[1:]):
                    return True
                board[x][y] = tmp
            # right
            if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if (dfs(i, j, word[1:])):
                        return True
        return False

# if __name__ == "__main__":
#     result = Solution().combine(1, 1)
#     print(result)
