# coding=utf-8
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
http://segmentfault.com/a/1190000003819886

http://bookshadow.com/weblog/2015/11/03/leetcode-longest-increasing-subsequence/

由于这个最长上升序列不一定是连续的，对于每一个新加入的数，都有可能跟前面的序列构成一个较长的上升序列，或者跟后面的序列构成一个较长的上升序列。

比如1,3,5,2,8,4,6，对于6来说，可以构成1,3,5,6，也可以构成2,4,6。

因为前面那个序列长为4，后面的长为3，所以我们更愿意6组成那个长为4的序列，所以对于6来说，它组成序列的长度，实际上是之前最长一个升序序列长度加1，

注意这个最长的序列的末尾是要小于6的，不然我们就把1,3,5,8,6这样的序列给算进来了。这样，我们的递推关系就隐约出来了，假设dp[i]代表加入第i个数能构成的最长升序序列长度，

我们就是要在dp[0]到dp[i-1]中找到一个最长的升序序列长度，又保证序列尾值nums[j]小于nums[i]，然后把这个长度加上1就行了。同时，我们还要及时更新最大长度。

（二叉搜索没整明白，回头看）

'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp) if dp else 0


if __name__ == "__main__":
    result = Solution().nthUglyNumber(12)
    print(result)
