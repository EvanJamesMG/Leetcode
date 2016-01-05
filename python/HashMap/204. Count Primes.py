# coding=utf-8
__author__ = 'EvanJames'
'''
Count the number of prime numbers less than a non-negative number, n.

统计小于n的素数（质数）的数目

'''

'''
埃拉托斯特尼筛法 (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

给出要筛数值的范围n，找出sqrt{n}以内的素数p_{1},p_{2},...,p_{k}。先用2去筛，即把2留下，把2的倍数剔除掉；
再用下一个素数，也就是3筛，把3留下，把3的倍数剔除掉；接下去用下一个素数5筛，把5留下，把5的倍数剔除掉；不断重复下去......。

'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        x = 2
        while x * x < n:
            if isPrime[x]:
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)

if __name__ == '__main__':
    res = Solution().countPrimes(25)
    print(res)
