/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

-- Define dp[n + 1], where dp[i] means the least number of perfect square numbers for integer i.
-- Initialization. dp[0] = 0. dp[i] = Integer.MAX_VALUE since we calculate the min number
-- Transit function, dp[i] = min(dp[i], dp[i - j * j]+1), where j * j <= i
-- Final state: dp[n]

https://siddontang.gitbooks.io/leetcode-solution/content/dynamic_programming/perfect_squares.html
http://segmentfault.com/a/1190000003768736
http://buttercola.blogspot.jp/2015/09/leetcode-perfect-squares.html
*/


public class Solution {
    public int numSquares(int n) {
        if (n <= 0) {
            return 0;
        }
         
        int[] dp = new int[n + 1];
         
        for (int i = 1; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
         
        return dp[n];
    }
}
