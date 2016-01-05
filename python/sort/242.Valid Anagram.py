# coding=utf-8
__author__ = 'EvanJames'
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:

You may assume the string contains only lowercase alphabets.


给定两个字符串s和t，写一个函数，判断t是否是s的变位词。
如果t跟s包含相同字符但排列顺序不同，则称t是s的变位词。
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

#
# if __name__ == '__main__':
#     res = Solution().countPrimes(25)
#     print(res)
