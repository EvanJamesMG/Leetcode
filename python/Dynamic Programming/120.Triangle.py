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
若不考虑空间复杂度可以从上到下进行动态规划求值

再对最后一行求最小值 但空间复杂度为O（n^2）

要想空间复杂度为O（n）,要从下到上进行 对于每任以层的任一点

其最小值为其下一层对应两点的最小值加其本身值 根据此可以得出代码如下：
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        res = [0] * n
        for i in range(0, n):
            res[i] = triangle[n-1][i]
        for i in range(n - 2, -1, -1):  #从倒数第二排到第一排
            for j in range(0, i+1):     #  j >=0 and j<=i
                res[j] = triangle[i][j] + min(res[j], res[j + 1])
        return res[0]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().nthUglyNumber(12)
    print(result)
