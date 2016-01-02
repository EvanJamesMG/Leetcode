# coding=utf-8
__author__ = 'EvanJames'
'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

'''


'''
直接看代码，python太尼玛简洁了
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]


# if __name__ == '__main__':
#     res = Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
#     print(res)
