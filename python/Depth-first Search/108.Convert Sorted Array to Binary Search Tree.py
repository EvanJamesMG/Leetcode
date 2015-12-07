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

'''
* 这道题是二分查找树的题目，要把一个有序数组转换成一颗二分查找树。
* 其实从本质来看，如果把一个数组看成一棵树（也就是以中点为根，左右为左右子树， 依次下去）数组就等价于一个二分查找树。
* 所以如果要构造这棵树，那就是把中间元素转化为根，然后递归构造左右子树。所以我们还是用二叉树递归的方法来实现，以根作为返回值，
* 每层递归函数取中间元素，作为当前根和赋上结点值，然后左右结点接上左右区间的递归函数返回值。时间复杂度还是一 次树遍历O(n)，
* 总的空间复杂度是栈空间O(logn)加上结果的空间O(n)，额外空间是O(logn)，总体是O(n)。
'''
class Solution(object):

    def sortedArrayToBST(self, arr):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
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
#     mnode = ListNode(3)
#     mnode.next = ListNode(5)
#     mnode.next.next = ListNode(6)
#     mnode.next.next.next = ListNode(7)
#     mnode.next.next.next.next = ListNode(8)
#
#     result = Solution().rotateRight(mnode, 6)
#     print(result.val)
#
