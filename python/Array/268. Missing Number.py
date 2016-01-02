# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''


'''
解法非常的巧妙

解法：等差数列前n项和 - 数组之和

真心怀疑自己的智商
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)

# if __name__ == '__main__':
#     res = Solution().majorityElement([1, 2, 3, 2, 2, 2, 7])
#     print(res)
