# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        nums.sort()
        return nums[len(nums)/2]


# if __name__ == '__main__':
#     res = Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 10)
#     print(res)
