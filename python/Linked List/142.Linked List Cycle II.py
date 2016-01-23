# coding=utf-8
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
'''
使用快慢指针。若链表存在环，两指针必在环中相遇，此时将慢指针移回头结点，
两指针以相同的速度移动，在环开始的节点处再次相遇。

图中(http://www.cnblogs.com/zuoyuan/p/3701877.html)，head到环路起点的距离为K，起点到fast和slow的相遇点的距离为M，环路周长为L。假设，在fast和slow相遇时，fast走过了Lfast，slow走过了Lslow。根据题意：

　　　　　Lslow=K+M；Lfast=K+M+n*L（n为正整数）；Lfast=2*Lslow

　　　　   可以推出：Lslow=n*L；K=n*L-M

　　　　　则当slow重新回到head，而fast还在相遇点，slow和fast都向前走，且每次走一个节点。

　　　　   则slow从head走到起点走了K，而fast从相遇点出发也走了K，而fast向前走了距离K后到了哪里呢？由于K=（n-1）*L+（L-M），所以fast转了n-1圈，再走L-M，也到了起点。这样起点就找到了。
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next is not None and node.next.next is not None:
            if node.next.val == node.next.next.val:
                val_prev = node.next.val
                while node.next is not None and node.next.val == val_prev:
                    node.next = node.next.next
            else:
                node = node.next

        return dummy.next

# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

