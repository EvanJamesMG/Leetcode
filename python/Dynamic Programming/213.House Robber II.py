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
连成圈也就是说明第一间和最后一件不能同时抢，一开始想如何在转换方程里体现出来，并没有什么思路。

后来看了别人的Blog，其实就将它们分成不包含第一间和不包含最后一间的两个array就可以了。

把第一家和最后一家分别去掉，各算一遍能抢的最大值，然后比较两个值取其中较大的一个即为所求.

将环形DP问题转化为两趟线性DP问题，可以复用House Robber的代码。

'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))

    def rob1(self, num):
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
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i-1])
        return dp[size]


if __name__ == "__main__":
    result = Solution().nthUglyNumber(12)
    print(result)
