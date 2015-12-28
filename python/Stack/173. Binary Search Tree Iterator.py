# coding=utf-8
'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''
import sys
import collections


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
http://bookshadow.com/weblog/2014/12/31/leetcode-binary-search-tree-iterator/

维护一个栈，从根节点开始，每次迭代地将根节点的左孩子压入栈，直到左孩子为空为止。

调用next()方法时，弹出栈顶，如果被弹出的元素拥有右孩子，则以右孩子为根，将其左孩子迭代压栈。
'''


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left



'''
采用根的中序遍历法将树节点保存在list中也可以实现树的迭代

但是空间复杂度O(size)，size为树的大小，不满足题目要求

中序遍历法求解的Python代码如下：

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.tree = []
        self.inOrderTraverse(root)
        self.idx = -1
        self.size = len(self.tree)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        self.idx += 1
        return self.idx < self.size

    # @return an integer, the next smallest number
    def next(self):
        return self.tree[self.idx]

    def inOrderTraverse(self, root):
        if root is None:
            return
        self.inOrderTraverse(root.left)
        self.tree.append(root.val)
        self.inOrderTraverse(root.right)

'''

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# if __name__ == "__main__":
#     MinStack().push(-2)
#     MinStack().push(0)
#     MinStack().push(-1)
#     result = MinStack().getMin()
#     print(result)
