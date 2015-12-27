# coding=utf-8
'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.

Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.

You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
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
维护两个栈inStack与outStack，其中inStack接收push操作新增的元素，outStack为pop/peek操作提供服务

由于栈具有后进先出（Last In First Out）的性质，栈A中的元素依次弹出并压入空栈B之后，栈A中元素的顺序会被逆转

当执行pop或者peek操作时，如果outStack中元素为空，则将inStack中的所有元素弹出并压入outStack，然后对outStack执行相应操作

由于元素至多只会从inStack向outStack移动一次，因此peek/pop操作的平摊开销为O(1)
'''

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.inStack = []
        self.outStack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.inStack.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        self.outStack.pop()

    # @return an integer
    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    # @return an boolean
    def empty(self):
        return len(self.inStack) + len(self.outStack) == 0

# if __name__ == "__main__":
#     result = Solution().removeDuplicateLetters('cbacdcbc')
#     print(result)
