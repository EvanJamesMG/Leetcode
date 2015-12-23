# coding=utf-8
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
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
这道题也是穷举全排列，只是集合中可能有重复的元素。分两步：1，对集合进行排序。2，进行剪枝，如果元素重复，直接跳过这一元素，
'''


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):

        num.sort()
        return self.helper(num)

    def helper(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        previousNum = None
        for i in range(len(num)):
            if num[i] == previousNum: continue
            previousNum = num[i]
            for j in self.helper(num[:i] + num[i + 1:]):
                if ([num[i]] + j) not in res:
                    res.append([num[i]] + j)
        return res

# if __name__ == "__main__":
#     result = Solution().combine(1, 1)
#     print(result)
