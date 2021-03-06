# coding=utf-8
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
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

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.sumNumbersRec(root, 0)
        return self.sum

    def sumNumbersRec(self, root, partialSum):
        if root == None:
            return
        partialSum = partialSum *10 + root.val
        if root.left == None and root.right == None:
            self.sum += partialSum
        else:
            self.sumNumbersRec(root.left, partialSum)
            self.sumNumbersRec(root.right, partialSum)
