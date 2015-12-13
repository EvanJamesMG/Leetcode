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
快速排序。O(nlgn)算法时间复杂度和O(1)空间复杂度，这是最简单的办法，如上即是；
最聪明的办法是使用基于partition的selection algorithm（什么鬼？），最好情况和最坏情况时间复杂度分别为O(n)和O(n^2)，空间复杂度为O(1)。
什么是partition？partition与快速排序息息相关，简单来说，寻找一个参考点ref，对数组元素进行处理，最后的处理结果是index=j之前的元素都小于ref，index=j之后的元素都大于等于ref。

'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]


'''


//
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        n = len(nums)
        start, stop = 0, n
        while start < stop:
            # partition
            j = start
            for i in xrange(start, stop-1):
                if nums[i] > nums[stop-1]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1

            nums[j], nums[stop-1] = nums[stop-1], nums[j]

            # j左侧的数据全部大于nums[j]，右侧的元素全部小于等于nums[j]
            if j+1 == k:
                return nums[j]
            elif j+1 < k:
                start = j+1
            else:
                stop = j
'''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().maxSubArray([99, 98, 97, -100, -200, 1])
    print(result)
