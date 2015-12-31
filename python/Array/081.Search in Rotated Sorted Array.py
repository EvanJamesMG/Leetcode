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
和这题的第一版本<<Search in Rotated Sorted Array>>类似，只是可能出现重复数字，而有了重复数字会使问题变得非常复杂。

例如对于数组 1 2 2 2 2 2 3，对第1个2进行翻转后，会得到2 2 2 2 3 1 2,这个数组首尾下标为0和6，得到中间位置的下标为3，

于是首尾和中间位置的元素都相同，我们无法判断索要找的数字是在前半段还是在后半段，这种情况下，只能够从头开始以O(n)时间进行一次搜索。

如果不是以上的情况，还是可以按照第一版本<Search in Rotated Sorted Array>的思路进行二分查找。

'''


class Solution(object):
    def search(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2

            if A[mid] == A[left] == A[right]:
                for i in range(left, right + 1):
                    if A[i] == target:
                        return True
                return False

            if target == A[mid]:
                return True
            if A[left] <= A[mid]:
                if A[left] <= target and target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if A[mid] < target and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().canFinish(3, [[0, 2], [2, 1], [1, 0]])
    print(result)
