# coding=utf-8
__author__ = 'EvanJames'
'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.


给定一个模式pattern和一个字符串str，判断str是否满足相同的pattern。

测试用例如题目描述。

注意：

pattern和str都只包含小写字母。
pattern和str不包含前导或者后缀空格。
str中的每一个单词之间都由一个空格分开。
pattern中的每一个字母都对应一个长度至少为1的单词。
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        ptnDict, wordDict = {}, {}
        for ptn, word in zip(pattern, words):
            if ptn not in ptnDict:
                ptnDict[ptn] = word
            if word not in wordDict:
                wordDict[word] = ptn
            if wordDict[word] != ptn or ptnDict[ptn] != word:
                return False
        return True


# if __name__ == '__main__':
#     res = Solution().countPrimes(25)
#     print(res)
