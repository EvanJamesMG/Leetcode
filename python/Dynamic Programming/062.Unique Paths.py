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
*
*  具体而言，定义m*n维二维数组dp[][],dp[i][j]表示从s出发到达格子(i,j)的路径数目，
*  现在我们可以思考如果写dp方程。通过观察网格特征和走法，我们可以分析得知，到达（i,j）只有两种走法，
*  第一是从（i-1,j）向下到(i,j)，第二是从（i,j-1）向右到（i,j），而dp[i][j-1]和dp[i-1][j]是已经保存的中间计算结果，
*  所以可以得到dp递推方程为dp[i][j] = dp[i][j-1] + dp[i-1][j]。所以可以从(0,0)开始不断计算到右侧和下方的格子的路径总数，
*  直到算出dp[m-1][n-1]，算法时间复杂度为O（mn），空间复杂度也为O（mn）。
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]

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
