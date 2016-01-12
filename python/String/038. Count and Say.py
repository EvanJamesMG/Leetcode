# coding=utf-8
__author__ = 'EvanJames'
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

'''

'''
就是每次统计该位置前面一个数，最后得出第n个字符串
'''


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        curRes = '1'
        start = 1
        while start < n:
            count = 1
            res = ''
            for j in range(1, len(curRes)):
                if curRes[j] == curRes[j - 1]:  # 统计相同的字符的个数
                    count += 1
                else:
                    res += str(count)
                    res += curRes[j - 1]
                    count = 1
            res += str(count)
            res += curRes[len(curRes) - 1]
            start += 1
            curRes = res  # 刚得出的字符串作为新的输入
        return curRes


if __name__ == '__main__':
    res = Solution().countAndSay(4)
    print(res)
