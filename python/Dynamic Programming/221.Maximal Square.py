# coding=utf-8
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
当我们判断以某个点为正方形右下角时最大的正方形时，那它的上方，左方和左上方三个点也一定是某个正方形的右下角，否则该点为右下角的正方形最大就是它自己了。

这是定性的判断，那具体的最大正方形边长呢？我们知道，该点为右下角的正方形的最大边长，最多比它的上方，左方和左上方为右下角的正方形的边长多1，最好的情况是是它的上方，左方和左上方为右下角的正方形的大小都一样的，这样加上该点就可以构成一个更大的正方形。但如果它的上方，左方和左上方为右下角的正方形的大小不一样，合起来就会缺了某个角落，这时候只能取那三个正方形中最小的正方形的边长加1了。假设dpi表示以i,j为右下角的正方形的最大边长，则有

dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
当然，如果这个点在原矩阵中本身就是0的话，那dpi肯定就是0了。
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        mymax = 0
        dp = [[0 for i in range(0,n)] for j in range(0,m)]
        for i in range(0, n):
            dp[0][i] = int(matrix[0][i])
            mymax = max(mymax, dp[0][i])
        for i in range(0, m):
            dp[i][0] = int(matrix[i][0])
            mymax = max(mymax, dp[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(min(dp[i][j - 1], dp[i-1][j]), dp[i - 1][j - 1])+1
                else:
                    dp[i][j]=0
                mymax = max(mymax, dp[i][j])
        return mymax * mymax


if __name__ == "__main__":
    result = Solution().maximalSquare(["1111","1111","1111"])
    print(result)
