# coding=utf-8
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
'''
此题出自 CTCI 题 2.4，依据题意，是要根据值x对链表进行分割操作，具体是指将所有小于x的节点放到不小于x的节点之前，咋一看和快速排序的分割有些类似，

但是这个题的不同之处在于只要求将小于x的节点放到前面，而并不要求对元素进行排序。

这种分割的题使用两路指针即可轻松解决。左边指针指向小于x的节点，右边指针指向不小于x的节点。由于左右头节点不确定，我们可以使用两个dummy节点
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return None
        dummyone = ListNode(0)
        dummytwo = ListNode(0)
        p1 = dummyone
        p2 = dummytwo
        while head:
            if head.val < x:
                dummyone.next = ListNode(head.val)
                dummyone = dummyone.next
            else:
                dummytwo.next = ListNode(head.val)
                dummytwo = dummytwo.next

            head = head.next
        dummytwo.next = None
        dummyone.next = p2.next
        return p1.next
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

