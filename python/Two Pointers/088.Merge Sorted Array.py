# coding=utf-8
'''
解题思路：
首先利用快慢指针将链表分为前后两部分，
将第二部分翻转，然后和第一部分比较
'''
import Queue

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
这是一道数组操作的题目，思路比较明确，就是维护三个index，分别对应数组A，数组B，和结果数组。
然后A和B同时从后往前扫，每次迭代中A和B指向的元素大的便加入结果数组中，然后index-1，另一个不动。
这里从后往前扫是因为这个题目中结果仍然放在A中，如果从前扫会有覆盖掉未检查的元素的可能性
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        indexA = m-1
        indexB = n-1
        while indexA >= 0 and indexB >= 0:
            if nums1[indexA] > nums2[indexB]:
                nums1[indexA+indexB+1] = nums1[indexA]
                indexA -= 1
            else:
                nums1[indexA+indexB+1] = nums2[indexB]
                indexB -= 1
        while indexB >= 0:
             nums1[indexA+indexB-1] = nums2[indexB]
             indexB -= 1

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    mnode = TreeNode(1)
    mnode.left = TreeNode(2)
    mnode.right = TreeNode(3)
    mnode.left.left = TreeNode(4)
    mnode.left.right = TreeNode(5)

    result = Solution().isPalindrome('')
    print(result)

