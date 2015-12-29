# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array

such that nums[i] = nums[j] and the difference between i and j is at most k.
'''

'''
解题思路：
使用dict保存数组中数字的下标
'''


class Solution:

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = dict()
        for x in range(len(nums)):
            idx = numDict.get(nums[x])
            if idx >= 0 and x - idx <= k:
                return True
            numDict[nums[x]] = x
        return False


if __name__ == '__main__':
    res = Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 10)
    print(res)
