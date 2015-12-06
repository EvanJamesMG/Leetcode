# coding=utf-8
# Definition for singly-linked list.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# coding=utf-8
'''
recursive的解法比较简练
1.停止条件是 left==None & right==None
2. left.val==right.val 比较left.left right.right & left.right right.left
'''

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.sym(root.left, root.right)

    def sym(self, left, right):
        if left == None and right == None:
            return True
        if left and right and left.val == right.val:
            return self.sym(left.right, right.left) and self.sym(left.left, right.right)
        else:
            return False



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

