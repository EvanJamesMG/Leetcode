# coding=utf-8
__author__ = 'EvanJames'
'''
Given a string S, find the longest palindromic substring in S.

You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ''
        for i in range(len(s)):
            len1 = len(self.getlongestpalindrome(s, i, i))
            if len1 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i)
            len2 = len(self.getlongestpalindrome(s, i, i + 1))
            if len2 > len(palindrome): palindrome = self.getlongestpalindrome(s, i, i + 1)
        return palindrome
    # @return a string
    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1 : r]

# if __name__ == '__main__':
#     res = Solution().largestNumber([23,45,232,8])
#     print(res)
