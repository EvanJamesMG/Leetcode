# coding=utf-8
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
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
和 <Combination Sum> 这题类似，此题要求每个candidates中的元素只能在1-9之间，且元素中个数唯一，且元素数组长度为K

基本思路是先排好序，然后每次递归中把剩下的元素一一加到结果集合中，并且把目标减去加入的元素，
然后把剩下元素（这次不包含当前加入的元素）放到下一层递归中解决子问题.
最后在到达目标值且数组长度为K时，加入

'''


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def DFS(self, candidates, k, target, start, valuelist):
        length = len(candidates)
        if target == 0 and len(valuelist) == k:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, k, target - candidates[i], i + 1, valuelist + [candidates[i]])

    def combinationSum3(self, k, n):
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        Solution.ret = []
        self.DFS(candidates, k, n, 0, [])
        return Solution.ret

# if __name__ == "__main__":
#     result = Solution().combine(1, 1)
#     print(result)
