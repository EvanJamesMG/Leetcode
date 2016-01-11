# coding=utf-8
'''
Given a string, find the length of the longest substring without repeating characters. 

For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 

For "bbbbb" the longest substring is "b", with the length of 1.
'''
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
http://fisherlei.blogspot.jp/2012/12/leetcode-longest-substring-without.html
从左往右扫描，当遇到重复字母时，以上一个重复字母的index +1，作为新的搜索起始位置。
直到扫描到最后一个字母。
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        subStr = ''
        rear = 0
        for front in xrange(len(s)):
            if s[front] not in subStr:
                subStr += s[front]
            else:
                maxLen = max(maxLen, len(subStr))
                while s[rear] != s[front]: rear += 1
                rear += 1
                subStr = s[rear : front + 1]
        return max(maxLen, len(subStr))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
