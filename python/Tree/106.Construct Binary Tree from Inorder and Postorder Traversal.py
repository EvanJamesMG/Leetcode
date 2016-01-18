# coding=utf-8
'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

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
  * 根据中序序列和后序序列构造二叉树，后序的最后一个结点一定是根结点，
  * 该结点可以把中序序列分成左右两部分，对应于左右子树的中序序列，
  * 根据左右两部分中结点的个数又可以把后序序列中除去最后一个结点的序列分成两部分，

  * 对应于左右子树的后序序列，这样就可以递归构造左右子树。
'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        hmap = {}
        if (inorder ==None and postorder ==None) or (len(inorder) == 0 and len(postorder) ==0):
            return None
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        return self.mhelp(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, hmap)

    def mhelp(self, inorder, inL, inR, postorder, pL, pR, hmap):
        if inL > inR or pL > pR:
            return None
        root = TreeNode(postorder[pR])
        index = hmap.get(root.val)
        root.left = self.mhelp(inorder, inL, index-1, postorder, pL, pL+index-inL-1, hmap)
        root.right = self.mhelp(inorder, index+1, inR, postorder, pR-inR+index,pR-1, hmap)
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
