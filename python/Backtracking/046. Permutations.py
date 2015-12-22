# coding=utf-8
'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
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
穷举一个集合的全排列。这个就是python递归巧妙的使用了。
'''


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res

# if __name__ == "__main__":
#     result = Solution().combine(1, 1)
#     print(result)
