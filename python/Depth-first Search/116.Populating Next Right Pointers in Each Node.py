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
 一个递归就搞定了，就是递归让每一个节点他的左右子树通过next链接，直至到最后一层，
 然后递归左右节点，继续让他们的左右子树通过next链接。
'''
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            LR = root.left
            RL = root.right
            while LR and RL:
                LR.next = RL
                LR = LR.right
                RL = RL.left
            self.connect(root.left)
            self.connect(root.right) 

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
