# coding=utf-8
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
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
回文的分割问题。同样是需要穷举出所有符合条件的集合，那么我们还是使用dfs。

'''

class Solution(object):
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True

    def dfs(self, s, stringlist):
        if len(s) == 0: Solution.res.append(stringlist)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist+[s[:i]])

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.res = []
        self.dfs(s, [])
        return Solution.res

# if __name__ == "__main__":
#     result = Solution().getPermutation(3, 4)
#     print(result)
