# coding=utf-8

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
board最外面四条边上的'O'肯定不会被'X'包围起来, 从这些'O'入手, 使用BFS求出所有相邻的'O', 把这些'O'改为另一种符号, 比如'$'。
然后再扫描一遍board, 把'O'换成'X', 把'$'换成'O'。
'''
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []: return
        lineNum = len(board)
        colNum = len(board[0])
        queue = collections.deque()
        visited = [[False for j in xrange(colNum)] for i in xrange(lineNum)]
        for i in xrange(colNum):
            if board[0][i] == 'O': queue.append((0, i))
            if board[lineNum-1][i] == 'O': queue.append((lineNum - 1, i))
        for i in xrange(1, lineNum - 1):
            if board[i][0] == 'O': queue.append((i, 0))
            if board[i][colNum-1] == 'O': queue.append((i, colNum - 1))
        while queue:
            t = queue.popleft()
            if board[t[0]][t[1]] == 'O': board[t[0]][t[1]] = '$'
            visited[t[0]][t[1]] = True
            if t[0] + 1 < lineNum and board[t[0] + 1][t[1]] == 'O' and visited[t[0] + 1][t[1]] == False: # 下
                queue.append((t[0] + 1, t[1]))
            if t[0] - 1 >= 0 and board[t[0] - 1][t[1]] == 'O' and visited[t[0] - 1][t[1]] == False:      # 上
                queue.append((t[0] - 1, t[1]))
            if t[1] + 1 < colNum and board[t[0]][t[1] + 1] == 'O' and visited[t[0]][t[1] + 1] == False:  # 右
                queue.append((t[0], t[1] + 1))
            if t[1] - 1 >= 0 and board[t[0]][t[1] - 1] == 'O' and visited[t[0]][t[1] - 1] == False:      # 左
                queue.append((t[0], t[1] - 1))
        for i in xrange(lineNum):
            for j in xrange(colNum):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '$': board[i][j] = 'O'

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    result = Solution().canFinish(3,[[0,2],[2,1],[1,0]])
    print(result)