# coding=utf-8
'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''
'''
http://bookshadow.com/weblog/2015/07/27/leetcode-different-ways-add-parentheses/

分而治之。对于输入字符串，若其中有运算符，则将其分为两部分，分别递归计算其值，然后将左值集合与右值集合进行交叉运算，将运算结果放入结果集中；

若没有运算符，则直接将字符串转化为整型数放入结果集中。

'''


class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        def calc(a, b, o):
            return {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}[o](a, b)

        res = []
        for i in range(len(input)):
            ch = input[i]
            if ch == '+' or ch == '-' or ch == '*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for n in left:
                    for m in right:
                        res.append(calc(n, m, ch))

        if len(res) == 0:
            return [int(input)]
        return res

        # 简洁的写法
        # return [eval(`a` + c + `b`)
        #         for i, c in enumerate(input) if c in '+-*'
        #         for a in self.diffWaysToCompute(input[:i])
        #         for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]


'''

参考：Java 代码

// Runtime: 6 ms
public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if (ch == '+' || ch == '-' || ch == '*') {
                List<Integer> left = diffWaysToCompute(input.substring(0, i));
                List<Integer> right = diffWaysToCompute(input.substring(i + 1));
                for (int n : left) {
                    for (int m : right) {
                        switch (ch) {
                        case '+':
                            res.add(n + m);
                            break;
                        case '-':
                            res.add(n - m);
                            break;

                        case '*':
                            res.add(n * m);
                            break;
                        }
                    }
                }
            }
        }

        if (res.size() == 0) {
            res.add(Integer.parseInt(input));
        }

        return res;
    }
}
'''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().maxSubArray([99, 98, 97, -100, -200, 1])
    print(result)
