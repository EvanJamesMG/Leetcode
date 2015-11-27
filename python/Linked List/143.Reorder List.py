# coding=utf-8
# Definition for singly-linked list.
'''
利用快慢指针将原链表在中点分为两部分，然后将第二部分链表反转，然后依次将链表二中的节点插入到链表一中的空隙中
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        label = True
        slow = head
        fast = head
        p1 = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp2 = slow.next             # 得到第二部分链表
        slow.next = None              # 将第一部分的链表截断
        p2 = self.reverse(temp2)      # 将第二部分链表反转
        while p2:                     # 将翻转后的第二部分链表节点依次插入到第一部分链表的间隙中
            tem = p1.next
            p1.next = ListNode(p2.val)
            p1.next.next = tem
            p1 = p1.next.next
            p2 = p2.next

        print(head.val)


    def reverse(self, head):    #链表反转

        if head == None:
            return head
        pre = None
        cur = head
        while cur:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem

        head = pre

        return head


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    mnode = ListNode(3)
    mnode.next = ListNode(5)
    mnode.next.next = ListNode(6)
    mnode.next.next.next = ListNode(7)

    result = Solution().reorderList(mnode)
    print(result.val)

