# coding=utf-8
# Definition for singly-linked list.
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
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
'''
广度优先搜索 + 奇数行翻转
'''

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        temque = [root]
        level = 0
        while len(temque) != 0:
            length = len(temque)
            temlist = []
            for i in range(length):
                temroot = temque.pop(0)    #队列是从头部先出，因此这里是pop(0)
                temlist.append(temroot.val)
                if temroot.left:
                    temque.append(temroot.left)
                if temroot.right:
                    temque.append(temroot.right)
            if level % 2 == 1:
                temlist.reverse()
                res.append(temlist)
            else:
                res.append(temlist)
            level += 1
        return res


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
