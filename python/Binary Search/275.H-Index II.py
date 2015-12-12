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

题目大意：
给定研究人员的文章引用次数的数组（每一篇文章的引用次数都是非负整数），编写函数计算该研究人员的h指数。

根据维基百科对h指数的定义：“一名科学家的h指数是指其发表的N篇论文中，有h篇论文分别被引用了至少h次，其余N-h篇的引用次数均不超过h次”。

例如，给定引用次数数组 = [3, 0, 6, 1, 5]，这意味着研究人员总共有5篇论文，每篇分别获得了3, 0, 6, 1, 5次引用。

由于研究人员有3篇论文分别至少获得了3次引用，且其余两篇的引用次数不超过3次，因而其h指数是3。

注意：如果存在多个可能的h值，取最大值作为h指数。

分析：O(logn) 二分搜索

给定数组已经为有序的数字

临界条件：找到一个 citation[i] == len - i 的点；
如果 citation[i] > len - i ，说明还可以往左试探；
如果 citation[i] < len - i ，说明还可以往右试探；

'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            mid = (low + high) / 2
            if N - mid == citations[mid]:
                return N - mid
            elif N - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return N - low


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().canFinish(3, [[0, 2], [2, 1], [1, 0]])
    print(result)
