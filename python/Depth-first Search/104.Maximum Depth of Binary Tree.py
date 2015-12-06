# coding=utf-8
# Definition for singly-linked list.

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
解题思路：
递归
分几种情况考虑：
1，树为空，则为0。
2，根节点如果只存在左子树或者只存在右子树，则返回值应为左子树或者右子树的（最大深度+1）。
3，如果根节点的左子树和右子树都存在，则返回值为（左右子树的最大深度的较大值+1）。
'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left == None and root.right != None:
            return self.maxDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.maxDepth( root.left ) + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    mnode = ListNode(3)
    mnode.next = ListNode(5)
    mnode.next.next = ListNode(6)
    mnode.next.next.next = ListNode(7)
    mnode.next.next.next.next = ListNode(8)

    result = Solution().rotateRight(mnode, 6)
    print(result.val)

