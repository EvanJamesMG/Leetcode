# coding=utf-8

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

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
