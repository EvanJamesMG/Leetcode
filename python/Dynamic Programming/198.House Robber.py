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
思路分析：典型的动态规划，和求最大和子数组有点类似，global[i] 表示num[0...i]之间的最优解，

那么DP方程可以写作global[i] = Max(global[i-2] +  num[i], global[i-1]),

分别对应于取num[i]（此时不能取num[i-1]）和不取num[i]的最优解，然后取max即可。

是一个一维DP，时间和空间复杂度都是O（n）。
'''

class Solution(object):
    def rob(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(num)
        if size == 0:
            return 0
        if size == 1:
            return num[0]
        dp = [0] * (size+1)
        dp[0] = 0
        dp[1] = num[0]
        for i in range(2, size+1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i-1])  #num[i]与上面的解释对应，但是数组是从0开始的，所以这里通过i-1与之对应
        return dp[size]



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().shell_sort([99, 98, 97, -100, -200, 1])
    print(result)
