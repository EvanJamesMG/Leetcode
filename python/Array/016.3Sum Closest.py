# coding=utf-8
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
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
先排序，后夹逼
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        ret = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tsum = nums[i] + nums[j] + nums[k]
                if abs(tsum - target) < abs(ret - target):
                    ret = tsum
                if tsum < target:
                    j += 1
                elif tsum > target:
                    k -= 1
                else:
                    return tsum
        return ret 


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
