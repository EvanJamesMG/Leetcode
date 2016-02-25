# coding=utf-8
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''
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
http://blog.csdn.net/murmured/article/details/50073521
http://www.cnblogs.com/grandyang/p/4997417.html

设sell[i] 卖出操作的最大利润。它需要考虑的是，第i天是否卖出。（手上有stock在第i天所能获得的最大利润）

buy[i] 买进操作的最大利润。它需要考虑的是，第i天是否买进。（手上没有stock在第i天所能获得的最大利润）

所以，显然有状态转移方程

buy[i] = max(buy[i-1] , sell[i-2] – prices[i])  //前天买入的，要休息一天再买入，所以是sell[i-2]在状态转移
sell[i] = max(sell[i-1], buy[i-1] + prices[i])
最后显然有sell[n-1] > buy[n-1] 所以我们返回sell[n-1]
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2: return 0
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]                     #当天买入
        buy[1] = max(-prices[0], -prices[1])    #最大收益，是看这两天买到得哪一个还便宜些
        sell[1] = max(0, prices[1] - prices[0])
        for i in xrange(2, n):
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])

        return sell[n - 1]

if __name__ == "__main__":
    result = Solution().nthUglyNumber(12)
    print(result)
