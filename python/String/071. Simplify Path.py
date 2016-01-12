# coding=utf-8
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
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
题目的要求是输出Unix下的最简路径，Unix文件的根目录为"/"，"."表示当前目录，".."表示上级目录。

例如：

输入1：

/../a/b/c/./..

输出1：

/a/b

模拟整个过程：

1. "/" 根目录

2. ".." 跳转上级目录，上级目录为空，所以依旧处于 "/"

3. "a" 进入子目录a，目前处于 "/a"

4. "b" 进入子目录b，目前处于 "/a/b"

5. "c" 进入子目录c，目前处于 "/a/b/c"

6. "." 当前目录，不操作，仍处于 "/a/b/c"

7. ".." 返回上级目录，最终为 "/a/b"

使用一个栈来解决问题。遇到'..'弹栈，遇到'.'不操作，其他情况下压栈。
'''


class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        i = 0
        res = ''
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != "/":   # 寻找'/'的位置
                end += 1
            sub = path[i + 1:end]                         # 找出夹在两个'/'之间的元素
            if len(sub) > 0:
                if sub == "..":                           # 遇到'..'弹栈
                    if stack != []: stack.pop()
                elif sub != ".":                          # 遇到'.'不操作
                    stack.append(sub)                     # 遇到其他的情况，压栈
            i = end
        if stack == []: return "/"
        for i in stack:
            res += "/" + i
        return res


        # if __name__ == "__main__":
        #     MinStack().push(-2)
        #     MinStack().push(0)
        #     MinStack().push(-1)
        #     result = MinStack().getMin()
        #     print(result)
