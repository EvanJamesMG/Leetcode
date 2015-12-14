# coding=utf-8
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
  爬梯子问题实质上就是斐波那契数列：
 * 当n=1时，ways=1
 * 当n=2时，有[2] [1,1]两种情况，ways=2
 * 当n=3时，有[1,1,1] [1,2] [2,1]三种情况，ways=3
 * 当n=4时，有[1,1,1,1] [2,2] [1,1,2] [1,2,1] [2,1,1]五种情况，ways=5
 * 当n=5时，有[1,1,1,1,1] [2,2,1] [2,1,2] [1,2,2] [1,1,1,2] [1,1,2,1] [1,2,1,1] [2,1,1,1]八种情况，ways=8
 * 当n>3时，n对应的情况数字为n-1和n-2之和。此时，规律正好和斐波那契数列出现的规律对应。
 * 斐波拉切数列是这样一个数列：1、1、2、3、5、8、13、21、……在数学上，其被以递归的方法定义：F0=0，F1=1，Fn=F(n-1)+F(n-2)（n>=2）
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]*(n+1)
        res[0] = 0
        if n>= 1:
            res[1] = 1
        if n >= 2: 
            res[2] = 2
        if n>=3:
            for i in range(3, n+1):
                res[i] = res[i-1] + res[i-2]
        return res[n]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().shell_sort([99, 98, 97, -100, -200, 1])
    print(result)
