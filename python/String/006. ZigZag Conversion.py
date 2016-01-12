# coding=utf-8
__author__ = 'EvanJames'
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

'''

按行遍历，计算每一行的相邻数字之间的间距，分两种情况：
1.开始和结尾行的两个数字之间的间隔都是2(numRows-1)
2.中间行的两个数字之间的间隔是2 * (numRows - 1 - i)与2 * i 交叉进行

'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
        if numRows == 1:
            return s
        for i in range(numRows):
            j = i
            flag = True #通过flag控制两个间隔的切换
            while j < len(s):
                result += s[j]
                if i == 0 or i == numRows - 1: #开始和结尾行的两个数之间的间隔都是2(numRows-1)
                  j += 2 * (numRows - 1)
                else:
                    if flag:
                        j += 2 * (numRows - 1 - i)
                        flag = False
                    else:
                        j += 2 * i
                        flag = True

        return result

# if __name__ == '__main__':
#     res = Solution().largestNumber([23,45,232,8])
#     print(res)
