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
解题思路：
一种巧妙的解法。使用两个指针prev和curr，
判断A[curr]是否和A[prev]、A[prev-1]相等，如果相等curr指针继续向后遍历，直到不相等时，
将curr指针指向的值赋值给A[prev+1]，这样多余的数就都被交换到后面去了。最后prev+1值就是数组的长度。
'''
class Solution(object):
    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(A) <= 2: return len(A)
        prev = 1; curr = 2
        while curr < len(A):
            if A[curr] == A[prev] and  A[curr] == A[prev - 1]:
                curr += 1
            else:
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
