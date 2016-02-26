# coding=utf-8
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''
'''
先层次遍历，之后选取每层中的最后一个节点
层次遍历之前已经解决：1.先序遍历 2. 队列
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

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        finalres = []
        if root == None:
            return []
        self.preorder(root, 0, res)
        for i in range(len(res)-1):
            finalres.append(res[i][-1])
        return finalres

    def preorder(self, root, level, res):
        if len(res) < level+1: res.append([])
        if root:
            res[level].append(root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)
            
