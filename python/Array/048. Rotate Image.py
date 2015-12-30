# coding=utf-8
__author__ = 'EvanJames'
'''
题意：

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

'''
解题思路：先将矩阵转置，然后将矩阵的每一行翻转，就可以得到所要求的矩阵了。
'''


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 翻转
        for i in range(n):
            matrix[i].reverse()

# if __name__ == '__main__':
#     res = Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 10)
#     print(res)
