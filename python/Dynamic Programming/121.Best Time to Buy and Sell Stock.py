'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
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
分析：动态规划法。

从前向后遍历数组，记录当前出现过的最低价格，作为买入价格，并计算以当天价格出售的收益，

作为可能的最大收益，整个遍历过程中，出现过的最大收益就是所求。
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==None or len(prices)==0:
            return 0
        maxprofit = 0
        curmin = prices[0]
        for i in range(len(prices)):
            curmin = min(prices[i], curmin)
            maxprofit = max(maxprofit, prices[i] - curmin)
        return maxprofit

# if __name__ == "__main__":
#     result = Solution().nthUglyNumber(12)
#     print(result)
