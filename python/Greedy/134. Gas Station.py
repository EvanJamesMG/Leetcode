# coding=utf-8
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).

You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
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
解题思路：这道题也很tricky，自己想是很难想出来的。如果sum(gas)<sum(cost)的话，那么一定无解。

diff是走完一站邮箱剩下的油，如果加上gas[i]也到不了下一站，那么继续将下一站设置为起点，然后再检查，是不是很巧妙呢？
'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        diff = 0
        stationIndex = 0
        for i in range(n):
            if gas[i]+diff < cost[i]: stationIndex = i+1; diff = 0
            else: diff += gas[i]-cost[i]
        return stationIndex

# if __name__ == "__main__":
#     result = Solution().removeDuplicateLetters('cbacdcbc')
#     print(result)
