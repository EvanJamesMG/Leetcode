# coding=utf-8
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''
import sys


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

列举出所有合法的括号匹配，使用dfs。

假设在位置k我们还剩余left个左括号和right个右括号，如果left>0，则我们可以直接打印左括号，而不违背规则。

能否打印右括号，我们还必须验证left和right的值是否满足规则，如果left>=right，则我们不能打印右括号，因为打印会违背合法排列的规则，否则可以打印右括号。

如果left和right均为零，则说明我们已经完成一个合法排列，可以将其打印出来。

'''


class Solution(object):
    def helpler(self, l, r, item, res):
        """
        :type n: int
        :rtype: List[str]
        """

        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0 and l < r:
            self.helpler(l, r - 1, item + ')', res)

    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

# if __name__ == "__main__":
#     result = Solution().maximalSquare(["1111", "1111", "1111"])
#     print(result)
