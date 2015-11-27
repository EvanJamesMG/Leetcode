# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
递归用的太巧妙了 ==+
'''

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        tem = head.next
        forward = head.next.next
        tem.next = head
        head.next = self.swapPairs(forward)
        return tem
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

