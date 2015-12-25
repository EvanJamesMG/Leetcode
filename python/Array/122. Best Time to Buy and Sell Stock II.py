# coding=utf-8
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
import sys
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
这个题特别容易想复杂，其实就是只要找到递增的区间差就行(注意：不可以在一天当中同时出现买和卖的行为)
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res = res + prices[i] - prices[i - 1]
        return res

# if __name__ == "__main__":
#     result = Solution().removeDuplicateLetters('cbacdcbc')
#     print(result)
