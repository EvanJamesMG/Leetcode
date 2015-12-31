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
要求只能扫一遍而且要in place, 只能通过交换A中的元素来实现。p0是指向0的指针, p2是指向2的指针, i是用于遍历的指针。
如果当前元素A[i]是2, 则交换A[i]和A[p2]的值, 然后p2前移, i不动, 当i > p2就终止, 这样就排除了2的干扰，因为i前面的元素总是0或1。
若A[i]是0, 交换A[i]和A[p0]的值, p0和i都后移, 若A[i]是1, 只要i后移即可, 换句话说, 总是把0往前放
'''
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == []: return
        length = len(A);
        p0 = 0; p2 = length - 1
        i = 0
        while i <= p2:
            if A[i] == 2:
                A[p2], A[i] = A[i], A[p2]
                p2 -= 1
            elif A[i] == 0:
                A[p0], A[i] = A[i], A[p0]
                p0 += 1
                i += 1
            else:
                i += 1

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
