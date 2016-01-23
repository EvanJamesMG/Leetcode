# coding=utf-8

__author__ = 'EvanJames'
'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


'''
解题思路：这道题考察的显然不是dfs，为什么？因为这道题不需要给出如何分割的答案，只需要判断是否可以分割为字典中的单词即可。

我们考虑使用动态规划，这个思路看代码的话不难，用python写起来也比较清晰。
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]


if __name__ == "__main__":

    result = Solution().wordBreak('leetcode',['leet','code'])
    print(result)
