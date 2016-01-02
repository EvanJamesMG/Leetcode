# coding=utf-8
__author__ = 'EvanJames'
'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

题目大意：
给定一组排好序且无重复的整数，返回整数范围的汇总。

例如给定数组 [0,1,2,4,5,7]， 返回 ["0->2","4->5","7"]。

解题思路：
将逐一递增的整数序列化简为（起点->终点）即可。
'''

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        x, size = 0, len(nums)
        ans = []
        while x < size:
            c, res = x, str(nums[x])
            while x + 1 < size and nums[x + 1] - nums[x] == 1:
                x += 1
            if x > c:
                res += "->" + str(nums[x])
            ans.append(res)
            x += 1
        return ans
# if __name__ == '__main__':
#     res = Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
#     print(res)
