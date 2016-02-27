# coding=utf-8
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
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
该题是对二叉树进行层次优先遍历，层次遍历主要采用队列的形式进行存储，通过将每个节点的左孩子和右孩子放入队列中，
然后每次从队列中取出元素即可。比较好理解，直接上代码了。
'''
from Queue import Queue


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        que = Queue()
        res = []
        if root is None:
            return res
        que.put(root)
        while que.qsize()>0:
            quelength = que.qsize()
            temlist = []
            for i in range(quelength):
                temroot = que.get()
                if temroot.left is not None:
                    que.put(temroot.left)
                if temroot.right is not None:
                    que.put(temroot.right)
                temlist.append(temroot.val)
            res.append(temlist)
        return res

'''
     方法二：
　   比如一棵树如下：
　　　　　　　　　　　　　　　 　1
　　　　　　　　　　　　　　　/ 　  \
　　　　　　　　　　　　　　 2       3
　　　　　　　　　　　　　 /  \     /   \
　　　　　　　　　　　　　4    5   6     7
　　二叉树的先序遍历为{1，2，4，5，3，6，7}，可以看到这个遍历顺序实际上就是dfs。
    在这个遍历中，我们可以用一个level来记录节点的高度，根节点高度为0。
'''


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def levelOrder(self, root):
        res = []
        self.preorder(root, 0, res)
        return res



