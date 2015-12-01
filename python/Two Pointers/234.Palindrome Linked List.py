# coding=utf-8
'''
解题思路：
首先利用快慢指针将链表分为前后两部分，
将第二部分翻转，然后和第一部分比较
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast  = fast.next.next
            slow = slow.next
        secondHead = slow.next
        slow.next = None

        #翻转第二部分链表
        p1 = secondHead
        p2 = p1.next

        while p1 and p2:
            tem = p2.next
            p2.next = p1
            p1 = p2
            p2 = tem
        secondHead.next = None

        # 比较两个子链表
        L1 = head
        L2 = p1
        while L2:
            if L1.val != L2.val:
                return False
            L1 = L1.next
            L2 = L2.next

        return True

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

