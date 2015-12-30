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
二分查找首先找到目标点，之后左右寻找边界
'''

class Solution(object):
    def searchRange(self, A, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                list = [0, 0]
                if A[right] == target: list[1] = right  # 防止边界取不到的情况 right正好是最后一个数时，（if A[i] != target: list[1] = i - 1; break）用不上，右边界无法赋值，因此要提前在这里赋值

                for i in range(mid, right + 1):
                    if A[i] != target: list[1] = i - 1; break
                for i in range(left, mid + 1):
                    if A[i] == target: list[0] = i; break
                return list
        return [-1, -1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().canFinish(3, [[0, 2], [2, 1], [1, 0]])
    print(result)
