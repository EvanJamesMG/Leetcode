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
这里的区别是维护一个局部最优不足以求得后面的全局最优，这是由于乘法的性质不像加法那样，累加结果只要是正的一定是递增，
乘法中有可能现在看起来小的一个负数，后面跟另一个负数相乘就会得到最大的乘积。不过事实上也没有麻烦很多，
我们只需要在维护一个局部最大的同时，在维护一个局部最小，这样如果下一个元素遇到负数时，就有可能与这个最小相乘得到当前最大的乘积和，这也是利用乘法的性质得到的。

因为最大值有可能由前一个的最大值/最小值 * 当前值得到，所以要有两个array来 保存每个Index的最大值和最小值

并且要与当前值比较，有可能只保留当前值

'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)

        minDP = [0 for i in range(length)]
        maxDP = [0 for i in range(length)]

        minDP[0] = nums[0]
        maxDP[0] = nums[0]
        maxProduct = nums[0]

        for i in range(1, length):
            minDP[i] = min(min(minDP[i-1] * nums[i], maxDP[i-1] * nums[i]), nums[i])
            maxDP[i] = max(max(minDP[i-1] * nums[i], maxDP[i-1] * nums[i]), nums[i])
            maxProduct = maxDP[i] if maxDP[i] > maxProduct else maxProduct

        return maxProduct


if __name__ == "__main__":
    result = Solution().nthUglyNumber(12)
    print(result)
