# coding=utf-8
# Definition for singly-linked list.
'''
深度优先搜索
'''
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
 * 本题使用一维线性规划解决。
 * 如果n等于0时，结果为0；（但是代码中的初始值要设置为1）
 * 如果n等于1时，只有一个节点，结果为1；
 * 如果n等于2时，根节点有两种选择，结果为2；
 * 如果n大于3时，根节点有n种选择，确定根节点后分别计算左右子树的可能情况，
 * 然后相乘就是当前根节点下所有的变形种类，
 * 之后在求和即可。算法实现如下：
'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            return 2
        rec = range(n+1)
        rec[0] = 1
        rec[1] = 1
        rec[2] = 2
        for i in range(3, n+1):
            tem = 0
            for k in range(i):
                tem += rec[k]*rec[i-k-1]
            rec[i] = tem
        return rec[n]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     mnode = ListNode(3)
#     mnode.next = ListNode(5)
#     mnode.next.next = ListNode(6)
#     mnode.next.next.next = ListNode(7)
#     mnode.next.next.next.next = ListNode(8)
#
#     result = Solution().rotateRight(mnode, 6)
#     print(result.val)
#
