# coding=utf-8
__author__ = 'EvanJames'
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''

'''
两种思路：
一种思路是先将两个数组合并，之后排序，返回中位数。O(n*logn);
另一种思路是：类似《21. Merge Two Sorted Lists》,每次在两个数组中抽取值较小的数值，最后在新的数组中返回中位数。

需要注意的是：数组中元素的个数若为奇数，中位数就是中间的数；数组中元素的个数若为偶数，中位数是中间的两个数的均值。
'''
#思路二：
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        res = []
        if nums1 == None or len(nums1) == 0:
            return self.getmid(nums2)
        if nums2 == None or len(nums2) == 0:
            return self.getmid(nums1)
        i = 0
        k1, k2 = 0, 0
        while k1 < len1 and k2 < len2:
            if nums1[k1] <= nums2[k2]:
                res.append(nums1[k1])
                k1 += 1
            else:
                res.append(nums2[k2])
                k2 += 1
            i += 1
        if k1 >= len1:
            while k2 < len2:
                res.append(nums2[k2])
                k2 += 1
        else:
            while k1 < len1:
                res.append(nums1[k1])
                k1 += 1
        return self.getmid(res)

    def getmid(self, res):
        length = len(res)
        if length % 2 == 0:
            tem = float(res[length / 2] + res[length / 2 - 1])
            return tem / 2
        else:
            return res[length / 2]

#思路一：
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        list = []
        for i in range(len(nums1)):
            list.append(nums1[i])
        for i in range(len(nums2)):
            list.append(nums2[i])
    
        list.sort()
        length = len(list)
        if length% 2 == 0:
            tem = float(list[length/2]+list[length/2-1])
            return tem/2
        else:
            return list[length/2]

if __name__ == '__main__':
    res = Solution().findMedianSortedArrays([1, 2, 3], [1, 2])
    print(res)
