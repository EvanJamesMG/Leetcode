# coding=utf-8
'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
典型的深度搜索
'''
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        if root is None:
            return self.ans

        self.dfs(root, str(root.val))
        return self.ans
    def dfs(self, root, path):
        if root.left is None and root.right is None:
            self.ans += path,
        if root.left:
            self.dfs(root.left, path + "->" + str(root.left.val))
        if root.right:
            self.dfs(root.right, path + "->" + str(root.right.val))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
