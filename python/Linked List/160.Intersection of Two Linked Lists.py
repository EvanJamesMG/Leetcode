# coding=utf-8
'''
指针pa、pb分别指向链表A和B的首节点。
遍历链表A，记录其长度lengthA，遍历链表B，记录其长度lengthB。
因为两个链表的长度可能不相同，比如题目所给的case，lengthA=5，lengthB=6，则作差得到lengthB-lengthA=1，
将指针pb从链表B的首节点开始走1步，即指向了第二个节点，pa指向链表A首节点，然后它们同时走，每次都走一步，当它们相等时，就是交集的节点。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

