# coding=utf-8

'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
滑动窗口 [left, right] 初始大小为0，滑动的规则如下：

若元素之和 < s，窗口右边沿向右延伸，直到 元素之和≥s 为止。
若元素之和 ≥ s，更新最小长度。然后窗口左边沿右移一位（即移除窗口中第一个元素），重复第1步。
'''
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        start, end, sum = 0, 0, 0
        bestAns = size + 1
        while end < size:
            while end < size and sum < s:
                sum += nums[end]
                end += 1
            while start < end and sum >= s:
                bestAns = min(bestAns, end - start)
                sum -= nums[start]
                start += 1
        return [0, bestAns][bestAns <= size]
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
