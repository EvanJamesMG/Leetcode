# coding=utf-8
# Definition for singly-linked list.
'''
先统计链表中的节点个数，然后根据给定的k,将链表分为两部分，注意这里k可能大于链表的长度，要进行取余操作
之后将链表一放在链表二的结尾处即可
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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or head.next ==None or k==0 :
            return head
        length = 0
        p1 = head
        p2 = head
        while p1:
            length += 1
            p1 = p1.next
        k = k % length
        if k == 0:
            return head
        for i in range(1, length-k):
            p2 = p2.next
        listtwo = p2.next
        p2.next = None
        listone = head
        cur = listtwo
        while cur.next:
            cur = cur.next
        cur.next = listone

        print(listtwo.val)
        return listtwo



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    mnode = ListNode(3)
    mnode.next = ListNode(5)
    mnode.next.next = ListNode(6)
    mnode.next.next.next = ListNode(7)
    mnode.next.next.next.next = ListNode(8)

    result = Solution().rotateRight(mnode, 6)
    print(result.val)

