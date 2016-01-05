# coding=utf-8
__author__ = 'EvanJames'
'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

'''

'''
创建两个字典来反映两个字符串中的映射关系：

    s_dict[s[i]] = t[i]
    t_dict[t[i]] = s[i]
当映射关系不等时则返回False

'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
                return False
            if t[i] in t_dict.keys() and t_dict[t[i]] != s[i]:
                return False
            s_dict[s[i]] = t[i]
            t_dict[t[i]] = s[i]
        return True

    '''
      另外一种写法：
        def isIsomorphic(self, s, t):
            sourceMap, targetMap = dict(), dict()
            for x in range(len(s)):
                source, target = sourceMap.get(t[x]), targetMap.get(s[x])
                if source is None and target is None:
                    sourceMap[t[x]], targetMap[s[x]] = s[x], t[x]
                elif target != t[x] or source != s[x]:
                    return False
            return True
    '''

#
# if __name__ == '__main__':
#     res = Solution().countPrimes(25)
#     print(res)
