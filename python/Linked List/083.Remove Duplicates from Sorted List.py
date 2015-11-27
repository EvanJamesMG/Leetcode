# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        p1 = head
        while p1:
            p2 = p1.next
            while p2:
                if p2.val == p1.val:
                    p2 = p2.next
                else:
                    break
            p1.next = p2
            p1 = p2

        return head 
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

