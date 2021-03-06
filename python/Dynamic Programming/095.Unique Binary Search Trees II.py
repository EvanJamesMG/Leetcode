'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# coding=utf-8
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
  * 与《Unique Binary Search Trees》类似
  * 不同之处在于：这道题比1难的就是不是返回个数，而是返回所有结果。
  * 这道题的解题依据依然是：
  * 当数组为 1，2，3，4，.. i，.. n时，基于以下原则的BST建树具有唯一性：
  * 以i为根节点的树，其左子树由[1, i-1]构成， 其右子树由[i+1, n]构成。
  * 在循环中调用递归函数求解子问题
'''
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1, n)

    def helper(self, start, end):
        result = []
        if start > end:
            result.append(None)
            return result

        for i in xrange(start, end + 1):
            # generate left and right sub tree
            leftTree = self.helper(start, i - 1)
            rightTree = self.helper(i + 1, end)
            # link left and right sub tree to root(i)
            for j in xrange(len(leftTree)):
                for k in xrange(len(rightTree)):
                    root = TreeNode(i)
                    root.left = leftTree[j]
                    root.right = rightTree[k]
                    result.append(root)

        return result

# if __name__ == "__main__":
#
#     result = Solution().rotateRight(mnode, 6)
#     print(result.val)
#
