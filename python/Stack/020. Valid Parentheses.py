# coding=utf-8
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
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
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True


# if __name__ == "__main__":
#     MinStack().push(-2)
#     MinStack().push(0)
#     MinStack().push(-1)
#     result = MinStack().getMin()
#     print(result)