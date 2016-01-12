# coding=utf-8
'''
解题思路：将不是字母的字符去掉，然后转换成小写，然后简单的回文判断。

python 中两个常用的函数
isalnum():如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
lower():转换字符串中所有大写字符为小写
'''
import Queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        while start<=end:
            while start<=end and not s[start].isalnum():
                start +=1
            while start<=end and not s[end].isalnum():
                end -=1
            if start<=end and s[start].lower() != s[end].lower():
                return False
            start +=1
            end -= 1
        return True

        # if s == None or len(s) == 0:
        #     return True
        # sTmp = ''
        # for i in range(0, len(s)):
        #     if s[i] >= 'a' and s[i] <= 'z' or s[i] >= '0' and s[i] <= '9' or s[i] >= 'A' and s[i] <= 'Z':
        #         sTmp += s[i]
        # sTmp = sTmp.lower()
        # for i in range(0, len(sTmp)/2):
        #     if sTmp[i] != sTmp[len(sTmp)-1-i]:
        #         return False
        # return True

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    mnode = TreeNode(1)
    mnode.left = TreeNode(2)
    mnode.right = TreeNode(3)
    mnode.left.left = TreeNode(4)
    mnode.left.right = TreeNode(5)

    result = Solution().isPalindrome('')
    print(result)

