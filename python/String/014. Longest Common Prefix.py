# coding=utf-8
__author__ = 'EvanJames'
'''
Write a function to find the longest common prefix string amongst an array of strings.

'''

'''
因为此题是简单题，所以算法不搞那么复杂
brute force的想法，以第一个字符串为标准，对于每个字符串从第一个字符开始，看看是不是和标准一致，如果不同，则跳出循环返回当前结果，否则继续下一个字符。

'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

# if __name__ == '__main__':
#     res = Solution().largestNumber([23,45,232,8])
#     print(res)
