# coding=utf-8
import collections
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
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
注意此题不包含重复元素

'''


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        if len(nums)==1:
            return nums[0]
        if nums[0] < nums[-1]:#数组未进行旋转的情况（旋转后的数组中第一个元素总是大于等于最后一个元素 （eg:34512））
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if right - left == 1:#结束状态，此时两指针的距离为1，左指针指向第一个递增子数组的结尾，右指针指向第二个递增字数组的开始
                mid = right
                break
            mid = (left + right) / 2

            if nums[left] <= nums[mid]:#此时中间指针指向左递增子数组中元素，目标值在右递增字数组的第一个，因此令左指针项向右缩进
                left = mid
            elif nums[mid] <= nums[right]:#此时中间指针指向右递增子数组中元素，目标值在右递增字数组的第一个，因此令右指针项向左缩进
                right = mid
        return nums[mid]

