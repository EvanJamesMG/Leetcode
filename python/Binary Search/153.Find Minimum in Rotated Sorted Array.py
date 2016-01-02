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
            if num[mid] <= num[high]: 
                high = mid - 1
            else:
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
