# coding=utf-8
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
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

枚举C(n, k)
暴力DFS枚举

'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if n <= 0 or n < k:
            return res
        self.helper(n, k, 1, [], res)
        return res

    def helper(self, n, k, start, item, res):
        if len(item) == k:
            res.append(item[:])
            return
        for i in range(start, n + 1):  # try each possibility number in current position
            item.append(i)
            self.helper(n, k, i + 1, item, res)  # after selecting number for current position, process next position
            item.pop()  # clear the current position to try next possible number


if __name__ == "__main__":
    result = Solution().combine(1, 1)
    print(result)
