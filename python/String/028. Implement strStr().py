# coding=utf-8
__author__ = 'EvanJames'
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''

'''
因为此题是简单题，所以算法不搞那么复杂
brute force的想法.
也可是运用KMP
'''
class Solution(object):
    def strStr(self, haystack, needle):
        if haystack==None or needle==None:
            return 0
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if i+len(needle) > len(haystack):
                return -1
            m = i
            for j in range(len(needle)):
                if needle[j] == haystack[m]:
                    if j == len(needle)-1:
                        return i
                    m += 1

                else:
                    break
        return -1

# if __name__ == '__main__':
#     res = Solution().largestNumber([23,45,232,8])
#     print(res)
