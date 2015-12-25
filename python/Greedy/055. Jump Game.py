# coding=utf-8
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
import sys
import collections

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
用贪心策略，刚开始step = A[0]，到下一步step--, 并且取step = max(step, A[1])，

这样step一直是保持最大的能移动步数，局部最优也是全局最优
'''
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        step = A[0]
        for i in range(1, len(A)):
            if step > 0:
                step -= 1
                step = max(step, A[i])
            else:
                return False
        return True

# if __name__ == "__main__":
#     result = Solution().removeDuplicateLetters('cbacdcbc')
#     print(result)
