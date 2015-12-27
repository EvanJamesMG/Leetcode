# coding=utf-8
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
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
开辟两个栈，一个栈是普通的栈，一个栈用来维护最小值的队列。
'''

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minnum = []
        self.mstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """

        if len(self.minnum) == 0 or x <= self.minnum[-1]:
            self.minnum.append(x)
        self.mstack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        tem = self.mstack.pop()
        if len(self.minnum) != 0 and self.minnum[-1] == tem:
            self.minnum.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.mstack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minnum[-1]


# if __name__ == "__main__":
#     MinStack().push(-2)
#     MinStack().push(0)
#     MinStack().push(-1)
#     result = MinStack().getMin()
#     print(result)