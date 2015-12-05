# coding=utf-8

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
    使用两根指针(下标)，一个指针(下标)遍历数组，另一个指针(下标)只取不重复的数置于原数组中
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return -1
        if len(nums) <= 1:
            return len(nums)
        newindex = 0
        for i in range(len(nums)):
            if nums[i] != nums[newindex]:
                newindex += 1
                nums[newindex] = nums[i]
        return newindex + 1

'''
    解法二 hashmap
    mlist = {}
    reslist = []
    for i in range(len(nums)):
        if nums[i] not in mlist:
            mlist[nums[i]] = 1
            reslist.append(nums[i])
    nums[0:len(reslist)-1] = reslist
    return len(mlist)
'''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
