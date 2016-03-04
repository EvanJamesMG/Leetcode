# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array of n integers where n > 1, nums, 

return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''


'''
解法非常的巧妙

由于output[i] = (x0 * x1 * ... * xi-1) * (xi+1 * .... * xn-1)

因此执行两趟循环：

第一趟正向遍历数组，计算x0 ~ xi-1的乘积

第二趟反向遍历数组，计算xi+1 ~ xn-1的乘积
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        size = len(nums)
        output = [1] * size
        left = 1
        for x in range(size - 1):
            left *= nums[x]
            output[x + 1] *= left
        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right
        return output

# if __name__ == '__main__':
#     res = Solution().majorityElement([1, 2, 3, 2, 2, 2, 7])
#     print(res)
