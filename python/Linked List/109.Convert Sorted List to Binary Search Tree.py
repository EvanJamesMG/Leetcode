# coding=utf-8
# Definition for singly-linked list.
'''
将链表转化为数组处理，这样就转化到convert-sorted-array-to-binary-search-tree 这个题了
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
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.sortedArrayToBST(arr)

    def sortedArrayToBST(self,arr):
        length = len(arr)
        if arr == None or length ==0:
            return None
        if length == 1:
            return TreeNode(arr[0])
        root = TreeNode(arr[length/2])
        root.left = self.sortedArrayToBST(arr[:length/2])
        root.right = self.sortedArrayToBST(arr[length/2+1:])
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().numTrees(3)
#     print result

