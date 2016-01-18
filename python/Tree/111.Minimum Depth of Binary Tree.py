# coding=utf-8
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
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
2，根节点如果只存在左子树或者只存在右子树，则返回值应为左子树或者右子树的（最小深度+1）。
3，如果根节点的左子树和右子树都存在，则返回值为（左右子树的最小深度的较小值+1）。

这道题是树的题目，其实跟Maximum Depth of Binary Tree非常类似，只是这道题因为是判断最小深度，
所以必须增加一个叶子的判断（因为如果一个节点如果只有左子树或者右子树，我们不能取它左右子树中小的作为深度，
因为那样会是0，我们只有在叶子节点才能判断深度，而在求最大深度的时候，因为一定会取大的那个，所以不会有这个问题）。
这道题同样是递归和非递归的解法，递归解法比较常规的思路，比Maximum Depth of Binary Tree多加一个左右子树的判断，
'''

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return self.minDepth( root.right ) + 1
        if root.left != None and root.right == None:
            return self.minDepth( root.left ) + 1
        return min( self.minDepth( root.left ), self.minDepth( root.right ) ) + 1



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

