# coding=utf-8
__author__ = 'EvanJames'
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''


'''
   两边夹的策略

    两个指标i j往中间走。每次计算i和j之间的面积，如果比目前最大面积大，则更新最大面积，否则让两者之间较小的数的指标往前走。

    如果height[i] <= height[j]，那么i++，因为在这里height[i]是瓶颈，j往里移只会减少面积，不会再增加area。

    这是一个贪心的策略，每次取两边围栏最矮的一个推进，希望获取更多的水。
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            temwater = min(height[left], height[right]) *(right - left)
            if temwater > res:
                res = temwater
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res


# if __name__ == '__main__':
#     res = Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 10)
#     print(res)
