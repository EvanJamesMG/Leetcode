# coding=utf-8
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
1. 声明一个二维的visited数组，初始化为false，表示所有的点均没有访问过。
2. 两层for循环遍历grid数组，遇到没有被访问过的‘1’之后，开始利用BFS思路遍历1周围的1，并将其标记为已访问。
3. 进行了几次BFS，就说明有几个孤岛。

每遇到'1'后, 开始向四个方向 递归搜索. 搜到后变为'0', 因为相邻的属于一个island. 然后开始继续找下一个'1'.
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.DFS(grid, i, j)
                    count += 1
        return count

    def DFS(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
            return
        grid[x][y] = '0'
        self.DFS(grid, x + 1, y)
        self.DFS(grid, x - 1, y)
        self.DFS(grid, x, y + 1)
        self.DFS(grid, x, y - 1)
