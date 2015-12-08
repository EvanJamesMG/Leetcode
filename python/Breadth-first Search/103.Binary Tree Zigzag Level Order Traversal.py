# coding=utf-8
# Definition for singly-linked list.
'''
深度优先搜索
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
        if root == None :
            return []
        res = []
        temque = Queue.Queue()
        temque.put(root)
        level = 0
        while temque.empty() is False:
            length = temque.qsize()
            temlist = []
            for i in range(length):
                temroot = temque.get()
                temlist.append(temroot.val)
                if temroot.left:
                    temque.put(temroot.left)
                if temroot.right:
                    temque.put(temroot.right)
            if level % 2 == 1:
                temlist.reverse()
                res.append(temlist)
            else:
                res.append(temlist)
            level +=1
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
