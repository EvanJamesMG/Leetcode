# coding=utf-8
import collections
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

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
由于旋转前数组有序，故旋转后，数组被分为两个有序的子区间（无旋转时为一个有序区间）。
算法同样采用折半查找的思想进行搜索，但上下界first、last的更新相比常规的折半查找略微复杂。
    关键点在于确定mid位于旋转点之前，还是之后：
    若mid在旋转点之前left和mid之间的元素都有序（在一个有序子区间中）。例如 [4 5 6 7 8 9  || 1 2 3]
    若mid在旋转点之后mid和right之间的元素都有序（在一个有序子区间中）。例如 [7 8 || 1 2 3 4 5 6]
    
参考 http://zhangxc.com/2013/11/leetcode-search-in-rotated-sorted-array
'''
class Solution(object):
    def search(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0; right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == A[mid]:
                return mid
            if A[left] <= A[mid]: #此时mid处于旋转点之前,left和mid之间的元素都有序（在一个有序子区间中）。例如 [4 5 6 7 8 9  || 1 2 3]
                if A[left] <= target and target < A[mid]:#若if成立，则target在[left,mid)之间，否则在[mid+1,right)之间
                    right = mid - 1
                else:
                    left = mid + 1
            else:                 #此时mid处于旋转点之后,mid和right之间的元素有序， 例如[7 8 || 1 2 3 4 5 6]
                if  A[mid] < target and target <= A[right]:#若if成立，则target在(mid,right]之间，否则在[left,mid)之间
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
