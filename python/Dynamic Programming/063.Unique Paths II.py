# coding=utf-8
import collections


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
*  动态规划：
初始化第一行和第一列时遇到障碍物就停止, 因为障碍物之后的位置肯定到达不了。

递推公式是如果grid[i][j]没有障碍物, dp[i][j] = dp[i-1][j] + dp[i][j-1], 如果grid[i][j]有障碍物, dp[i][j] = 0。
'''


class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # base case
        dp = [[0 for j in xrange(cols)] for i in xrange(rows)]
        for i in xrange(cols):
            if grid[0][i] == 0: dp[0][i] = 1
            else: break
        for i in xrange(rows):
            if grid[i][0] == 0: dp[i][0] = 1
            else: break

        # dynamic programming
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                dp[i][j] = 0 if grid[i][j] == 1 else dp[i - 1][j] + dp[i][j - 1]
        return dp[rows - 1][cols - 1]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().shell_sort([99, 98, 97, -100, -200, 1])
    print(result)
