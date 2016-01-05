# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.



根据维基百科对h指数的定义：“一名科学家的h指数是指其发表的N篇论文中，有h篇论文分别被引用了至少h次，其余N-h篇的引用次数均不超过h次”。

例如，给定引用次数数组 = [3, 0, 6, 1, 5]，这意味着研究人员总共有5篇论文，每篇分别获得了3, 0, 6, 1, 5次引用。

由于研究人员有3篇论文分别至少获得了3次引用，且其余两篇的引用次数不超过3次，因而其h指数是3。

注意：如果存在多个可能的h值，取最大值作为h指数。

'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = 0
        citations.sort()
        for i in range(len(citations) - 1, -1, -1):
            if count >= citations[i]:
                return count
            count += 1
        return count

#
# if __name__ == '__main__':
#     res = Solution().countPrimes(25)
#     print(res)
