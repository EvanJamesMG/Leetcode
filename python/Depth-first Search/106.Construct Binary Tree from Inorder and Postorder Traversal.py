# coding=utf-8
'''
Given inorder and traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''
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
  * 根据中序序列和后序序列构造二叉树，后序的最后一个结点一定是根结点，
  * 该结点可以把中序序列分成左右两部分，对应于左右子树的中序序列，
  * 根据左右两部分中结点的个数又可以把后序序列中除去最后一个结点的序列分成两部分，

  * 对应于左右子树的后序序列，这样就可以递归构造左右子树。
'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[len(postorder) - 1])
        index = inorder.index(postorder[len(postorder) - 1])
        root.left = self.buildTree(inorder[ 0 : index ], postorder[ 0 : index ])
        root.right = self.buildTree(inorder[ index + 1 : len(inorder) ], postorder[ index : len(postorder) - 1 ])
        return root
