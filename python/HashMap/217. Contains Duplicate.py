# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
               d[nums[i]] = 1
        return False

# if __name__ == '__main__':
#     res = Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
#     print(res)
