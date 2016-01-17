# coding=utf-8
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
'''
将链表分为3段 ，第二段翻转后，前面和第一段相连，后面和第三段相连
'''

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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        dummyone = ListNode(0)
        dummytwo = ListNode(0)
        p1 = dummyone
        p2 = dummytwo
        p3 = None

        k = 0
        while head:
            k += 1
            if k <= m-1:                 # 第一段链表提取
                dummyone.next = ListNode(head.val)
                dummyone = dummyone.next

            if k >= m and k <= n:        # 第二段链表提取
                dummytwo.next = ListNode(head.val)
                dummytwo = dummytwo.next
                if k == n:
                    dummytwo.next = None
            if k == n+1:                 # 第三段链表提取
                p3 = head
                break
            head = head.next
        p2start = self.reverse(p2.next)
        p2end = p2start
        while p2end.next:                # 找到翻转后的第二段链表的结尾节点，以和第三段链表相连
            p2end = p2end.next
        dummyone.next = p2start          # 第一段链表的结尾和第二段链表的开头相连
        p2end.next = p3                  # 第二段链表的结尾和第三段链表的开头相连
        return p1.next                   # 返回第一段链表的开头，此时三个链表已经重新相连了

    def reverse(self, head):  #链表翻转
        if head == None:
            return None

        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev

        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    mnode = ListNode(3)
    mnode.next = ListNode(5)
    mnode.next.next = ListNode(6)

    result = Solution().reverseBetween(mnode, 1, 2)
    print(result.val)

