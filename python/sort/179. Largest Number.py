# coding=utf-8
__author__ = 'EvanJames'
'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an intege
'''



'''
排序思路：对于两个备选数字a和b，如果str(a) + str(b) > str(b) + str(a)，则a在b之前，否则b在a之前

按照此原则对原数组从大到小排序即可

时间复杂度O（nlogn）

易错样例：
Input:     [0,0]
Output:    "00"
Expected:  "0"
'''

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp=self.compare)
        sb=''
        for x in num:
            sb += str(x)
        if sb.replace('0', '') == '':
            return '0'
        return num

    def compare(self, a, b):
        return [1, -1][a + b > b + a]

# if __name__ == '__main__':
#     res = Solution().largestNumber([23,45,232,8])
#     print(res)
