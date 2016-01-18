# coding=utf-8
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

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
  * 根据中序序列和先序序列构造二叉树，后序的最后一个结点一定是根结点，
  * 该结点可以把中序序列分成左右两部分，对应于左右子树的中序序列，
  * 根据左右两部分中结点的个数又可以把先序序列中除去头第一个结点的序列分成两部分，
  * 对应于左右子树的先序序列，这样就可以递归构造左右子树。
'''

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (preorder == None and inorder == None) or (len(preorder)==0 and len(inorder)==0):
            return None
        mhash = {}
        for i in range (len(inorder)):
            mhash[inorder[i]] =i

        return self.mhelp(preorder, 0, len(preorder)-1, inorder, 0, len(preorder)-1, mhash)

    def mhelp(self, preorder, pL, pR, inorder, inL, inR, mhash):
        if pL > pR or inL > inR :
            return None
        root = TreeNode(preorder[pL])
        index = mhash.get(root.val)
        root.left = self.mhelp(preorder, pL+1, pR - (inR - index), inorder, inL, index-1, mhash)
        root.right = self.mhelp(preorder, pL+1 + index - inL, pR, inorder, index + 1, inR, mhash)
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
