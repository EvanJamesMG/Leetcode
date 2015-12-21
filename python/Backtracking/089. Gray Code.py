# coding=utf-8
'''
题意：
格雷码是二进制数字系统，其中，两个连续值仅在一个比特上不同。
给定一个非负整数n来表示码的总位数，打印出格雷码的序列。格雷码序列都是以0开始的。
比如, 给定 n = 2, 返回 [0,1,3,2]. 它的格雷码的序列为:
00 - 0
01 - 1
11 - 3
10 - 2
注意：
对于给定的 n ,它的格雷码不是唯一定义的。
比如，根据上述定义[0,2,3,1]同样也是一个有效的格雷码序列。
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
算法分析：
* 其实这道题的正解是找规律：
    以3位格雷码为例。
    0 0 0
    0 0 1  ======>>  n-1位格雷码
    0 1 1
    0 1 0
-------------------
    1 1 0
    1 1 1  ======>>   1<<(n-1)[即为 (1<<2)==100]  + n-1位格雷码的逆序即为(10 11 01 00)
    1 0 1
    1 0 0

'''


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        tem = self.grayCode(n - 1)
        addnum = 1 << n-1
        res = tem
        for i in range(len(tem) - 1, -1, -1):
            res.append(addnum + tem[i])
        return res


# if __name__ == "__main__":
#     result = Solution().maximalSquare(["1111", "1111", "1111"])
#     print(result)
