# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            tem = nums[i]
            if tem in d:
                d.pop(tem)
            else:
                d[tem] = 1
        return d.keys()[0]

# if __name__ == '__main__':
#     res = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#     print(res)
