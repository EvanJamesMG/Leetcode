# coding=utf-8
'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
import sys


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
碰到这种问题，一律dfs。和之前遇到的出现重复元素的情况一样，进行剪枝，如果元素重复，直接跳过这一元素，

'''

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer

    def subsetsWithDup(self, S):
        def dfs(depth, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)
            if depth == len(S): return
            prenum = None
            for i in range(start, len(S)):
                if S[i] == prenum:continue
                prenum = S[i]
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res

# if __name__ == "__main__":
#     result = Solution().getPermutation(3, 4)
#     print(result)
