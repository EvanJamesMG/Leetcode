# coding=utf-8

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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0); dummy.next = head
        p1 = p2 = dummy
        for i in range(n): p1 = p1.next
        while p1.next:
            p1 = p1.next; p2 = p2.next
        p2.next = p2.next.next
        return dummy.next

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

