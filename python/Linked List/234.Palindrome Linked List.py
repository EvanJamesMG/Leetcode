# coding=utf-8
'''
你可以在O(n)时间复杂度和O(1)空间复杂度完成吗？
解题思路：
1). 使用快慢指针寻找链表中点.将链表分隔为两部分链表
2). 将链表的后半部分就地逆置，然后比对前后两半的元素是否一致
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        fast = head
        slow = head

        # 快慢指针寻找链表的中间分隔
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        secondHead = slow.next
        slow.next = None

        # 翻转第二部分链表
        p1 = secondHead
        p2 = p1.next

        while p1 and p2:
            tem = p2.next
            p2.next = p1
            p1 = p2
            p2 = tem
        secondHead.next = None

        # 比较两个子链表(若链表中有奇数个元素，则L2短;若链表中有偶数个元素，L1和L2的长度相同)
        L1 = head
        L2 = p1
        while L2:
            if L1.val != L2.val:
                return False
            L1 = L1.next
            L2 = L2.next

        return True

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

