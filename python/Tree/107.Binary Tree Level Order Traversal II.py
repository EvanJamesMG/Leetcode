# coding=utf-8
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

'''
广度优先搜索 + 链表的翻转
'''
import Queue

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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        reslist = []
        que = Queue.Queue()
        if root == None:
            return []
        que.put(root)
        while que.empty() == False:
            temlist = []
            length = que.qsize()
            for i in range(length):
                temroot = que.get()
                temlist.append(temroot.val)
                if temroot.left:
                    que.put(temroot.left)
                if temroot.right:
                    que.put(temroot.right)
            reslist.append(temlist)
        reslist.reverse()
        return reslist


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    mnode = TreeNode(1)
    mnode.left = TreeNode(2)
    mnode.right = TreeNode(3)
    mnode.left.left = TreeNode(4)
    mnode.left.right = TreeNode(5)

    result = Solution().levelOrderBottom(mnode)
    print(result)

