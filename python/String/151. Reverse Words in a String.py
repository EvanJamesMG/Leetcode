# coding=utf-8
__author__ = 'EvanJames'
'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''

'''
此题才体现python强大的处理字符的能力

short and easy

需要注意的是最后一个单词后面不再添加空格
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        if not s or len(s) == 0:
            return s
        temlist = s.split()
        for i in range(len(temlist)-1, -1, -1):
            res += temlist[i]
            if i != 0:
                res += ' '
        return res

if __name__ == '__main__':
    res = Solution().reverseWords('Hello World 123')
    print(res)
