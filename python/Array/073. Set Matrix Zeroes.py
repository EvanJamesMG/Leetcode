# coding=utf-8
__author__ = 'EvanJames'
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''



'''

with O(rows+cols) extra space
分别记录两个向量x, y，保存行和列是否有0，再次遍历数组时查询对应的行和列然后修改值。

'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0

# if __name__ == '__main__':
#     res = Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 10)
#     print(res)
