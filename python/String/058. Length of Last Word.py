# coding=utf-8
__author__ = 'EvanJames'
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

'''

'''
此题才体现python强大的处理字符的能力

short and easy
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = s.split()
        if slist ==[]:
            return 0
        else:
            return len(slist[len(slist)-1])


if __name__ == '__main__':
    res = Solution().lengthOfLastWord('Hello World')
    print(res)
