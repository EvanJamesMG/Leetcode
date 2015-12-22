# coding=utf-8
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6] 
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
和 <Combination Sum> 这题类似，此题要求每个candidates中的元素只能出现一次。

基本思路是先排好序，然后每次递归中把剩下的元素一一加到结果集合中，并且把目标减去加入的元素，
然后把剩下元素（这次不包含当前加入的元素）放到下一层递归中解决子问题.
最后在满足条件且在res不存在相同数组时，加入

'''
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.ret:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i+1, valuelist + [candidates[i]])

    def combinationSum2(self, candidates, target):
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret
# if __name__ == "__main__":
#     result = Solution().combine(1, 1)
#     print(result)
