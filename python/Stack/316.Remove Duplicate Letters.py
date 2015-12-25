# coding=utf-8
'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once.

You must make sure your result is the smallest in lexicographical order among all possible results.

Example:

Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

题目大意：
给定一个只包含小写字母的字符串，从中移除重复字母使得每个字母只出现一次。你必须确保结果的字典序最小。(字典序就是a<b<c...)
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
首先计算字符串s中每一个字符出现的次数，得到字典counter

遍历字符串s，记当前字符为c，将counter[c] - 1

如果c已经在栈stack中，继续遍历

将字符c与栈顶元素top进行比较，若top > c并且counter[top] > 0则弹栈，重复此过程

将c入栈

'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        stack = list()
        for c in s:
            counter[c] -= 1
            if c in stack:
                continue
            while stack and stack[-1] > c and counter[stack[-1]]:
                stack.pop()
            stack.append(c)
        return ''.join(stack)

if __name__ == "__main__":
    result = Solution().removeDuplicateLetters('cbacdcbc')
    print(result)
