# coding=utf-8
import collections


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
            if A[left] <= A[mid]:
                if A[left] <= target and target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if  A[mid] < target and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().canFinish(3, [[0, 2], [2, 1], [1, 0]])
    print(result)
