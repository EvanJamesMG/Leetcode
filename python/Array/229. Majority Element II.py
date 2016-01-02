# coding=utf-8
__author__ = 'EvanJames'
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

The algorithm should run in linear time and in O(1) space.
'''


'''
空间复杂度 O(1)要求太难了，算法空间复杂度为O(n)

利用 hashmap
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        dic = {}
        length = len(nums)
        for i in nums:
            if i in dic:
                dic[i] = dic.get(i)+1
            else:
                dic[i] = 1

        for i in dic:
            if dic[i] > length/3:
                ans.append(i)
        return ans

if __name__ == '__main__':
    res = Solution().majorityElement([1, 2, 3, 2, 2, 2, 7])
    print(res)
