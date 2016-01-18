# coding=utf-8
'''

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
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
此题和《118. Pascal's Triangle》类似，但是需要注意的是，上一题给出的numRows是第几行（从1开始），此题给出的rowIndex是行序号（从0开始）。
'''
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        list = [[] for i in range(rowIndex + 1)]
        for i in range(0, rowIndex+1):
            list[i] = [1 for j in range(i + 1)] #先把每一行都填上一
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                list[i][j] = list[i - 1][j - 1] + list[i - 1][j]  #中间部分另外计算
        return list[rowIndex]

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# if __name__ == "__main__":
#     MinStack().push(-2)
#     MinStack().push(0)
#     MinStack().push(-1)
#     result = MinStack().getMin()
#     print(result)
