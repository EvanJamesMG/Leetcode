# coding=utf-8
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
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
广度优先搜索 + 奇数行翻转
'''
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None :
            return []
        res = []
        temque = Queue.Queue()
        temque.put(root)
        level = 0
        while temque.empty() is False:
            length = temque.qsize()
            temlist = []
            for i in range(length):
                temroot = temque.get()
                temlist.append(temroot.val)
                if temroot.left:
                    temque.put(temroot.left)
                if temroot.right:
                    temque.put(temroot.right)
            if level % 2 == 1:
                temlist.reverse()
                res.append(temlist)
            else:
                res.append(temlist)
            level +=1
        return res

