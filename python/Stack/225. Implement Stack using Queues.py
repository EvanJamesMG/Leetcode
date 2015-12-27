# coding=utf-8
'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
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
直接看代码
'''

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)

    # @return an integer
    def top(self):
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    # @return an boolean
    def empty(self):
        return self.queue == []


# if __name__ == "__main__":
#     MinStack().push(-2)
#     MinStack().push(0)
#     MinStack().push(-1)
#     result = MinStack().getMin()
#     print(result)