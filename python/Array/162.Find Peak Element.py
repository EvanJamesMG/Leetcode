# coding=utf-8
import collections
'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''

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
二分查找  O(logn)

有人可能有疑问，如果有多个波峰，那么二分查找还有效吗？对本题而言，依然有效，因为题目只让你返回一个peak，不是所有的peak。满足下面的代码条件的点必然是peak中的一个。

如果中间元素大于其相邻后续元素，则中间元素左侧(包含该中间元素）必包含一个局部最大值。如果中间元素小于其相邻后续元素，则中间元素右侧必包含一个局部最大值。

'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            if low == high:
                return low
            mid = (low + high) / 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
