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
首先我们需要知道，对于一个区间A，如果A[start] < A[stop]，那么该区间一定是有序的了。

假设在一个轮转的排序数组A，我们首先获取中间元素的值，A[mid]，mid = (start + stop) / 2。因为数组没有重复元素，那么就有两种情况：

A[mid] <= A[high]，那么最小值一定在左半区间，譬如[7,0,1,2,4,5,6]，这件元素为2，2 < 7，我们继续在[7,0,1,2]这个区间查找。

A[mid] > A[high]，那么最小值一定在右半区间，譬如[4,5,6,7,0,1,2]，中间元素为7，7 > 4，最小元素一定在[7,0,1,2]这边，于是我们继续在这个区间查找。

'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        ans = num[0]
        size = len(num)
        low, high = 0, size - 1
        while low <= high:
            mid = (low + high) / 2
            if num[mid] <= num[high]: # min位于上升沿左侧
                high = mid - 1
            else: # min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
            ans = min(ans, num[mid])
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().canFinish(3, [[0, 2], [2, 1], [1, 0]])
    print(result)
