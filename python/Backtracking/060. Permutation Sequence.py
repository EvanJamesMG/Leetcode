# coding=utf-8
'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
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
这道题也是穷举全排列，貌似python 会超时，体会思想吧
'''


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = []
        for i in range(n):
            nums.append(i+1)
        res = self.helper(nums)
        return str(res[k - 1])

    def helper(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.helper(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + j)
        return res

if __name__ == "__main__":
    result = Solution().getPermutation(3, 4)
    print(result)
