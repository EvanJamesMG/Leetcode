# coding=utf-8
__author__ = 'EvanJames'
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question
'''


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

        # 解法二
        # mlist = {}
        # reslist = []
        # for i in range(len(nums)):
        #     if nums[i] not in mlist:
        #         mlist[nums[i]] = 1
        #         reslist.append(nums[i])
        # nums[0:len(reslist)-1] = reslist
        # return len(mlist)

# if __name__ == '__main__':
#     res = Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 10)
#     print(res)
