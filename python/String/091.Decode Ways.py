'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
# coding=utf-8
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
动态规划, 看一位是0还是1~9，看两位是不是在10~26之间。dp[N] = M 表示字符串s的前N位有M种解码方式。

f[i]表示从头到第i位有多少种方法
那么就是
i如果是能和i-1构成 1..26...
那么f[i] = f[i-1] + f[i-2]
意思就是i单独的一种方法，和与i-1一起构成两位的方法。
如果不能f[i] = f[i-1]

到此，感觉就做完啦。
不过。。。不过。。。我没有考虑0啊。。。
有0要特殊处理。。。
首先第一位肯定不能有0 ， 也不能有连续的0
10，20这种只f[i] = f[i-2]
00,30,40...等都是非法的。。。。
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s: return 0
        # dp[M] means decode ways for first M letters of s
        dp = [0 for i in xrange(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in xrange(2, len(s) + 1):
            if s[i-1] != '0': dp[i] += dp[i-1]             #注意这里s[i-1]实则表示数组中的第i个数字，因为数组是从0开始的
            if 10 <= int(s[i-2:i]) <= 26: dp[i] += dp[i-2] #同理s[i-2：i]实则表示数组中的第i-1到i之间的数字，因为数组是从0开始的
        return dp[len(s)]


if __name__ == "__main__":
    result = Solution().numSquares(12)
    print(result)
