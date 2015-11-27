# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
归并排序，最佳时间复杂度O(n log n)  最坏的时间复杂度O(n log n)
由于题目对时间复杂度和空间复杂度要求比较高，所以查看了各种解法，最好的解法就是归并排序，由于
链表在归并操作时并不需要像数组的归并操作那样分配一个临时数组空间，所以这样就是常数空间复杂度了，当然这里不考虑递归所产生的系统调用的栈。

这里涉及到一个链表常用的操作，即快慢指针的技巧。设置slow和fast指针，
开始它们都指向表头，fast每次走两步，slow每次走一步，fast到链表尾部时，slow正好到中间，这样就将链表截为两段。
'''

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def merge(self, head1, head2):
        if head1 == None: return head2
        if head2 == None: return head1
        dummy = ListNode(0)                             #归并时，新建一个链表头结点
        p = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
        if head1 == None:
            p.next = head2
        if head2 == None:
            p.next = head1
        return dummy.next

    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = head; fast = head                        #快慢指针技巧的运用，用来截断链表。
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None                                #head1和head2为截为两条链表的表头
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

