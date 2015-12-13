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
时间 O(n)   空间O(1)

扫描一遍数组，若当前i，前面i-1的结果若为负的话，新序列就从当前A[i]开始算起了，不然就将当前A[i]附加上去。

'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mymax = nums[0]
        sum = 0
        for i in range(len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            mymax = max(mymax, sum)
        return mymax


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().maxSubArray( [99,98,97,-100,-200,1])
    print(result)
