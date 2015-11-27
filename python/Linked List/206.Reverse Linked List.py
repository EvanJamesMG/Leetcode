# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p2 = None
        while head:
            next = head.next
            head.next = p2
            p2 = head
            head = next
        return p2


    '''
    递归的方法
    def reverseList(self, head):
        return self.doReverse(head, None)
    def doReverse(self, head, beforeHead):
        if head is None:
            return beforeHead
        next = head.next
        head.next = beforeHead
        return self.doReverse(next, head)
    '''


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

