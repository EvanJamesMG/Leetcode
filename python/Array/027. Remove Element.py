# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return -1
        newindex = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[newindex]=nums[i]
                newindex +=1
        return newindex


if __name__ == '__main__':
    res = Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 10)
    print(res)
