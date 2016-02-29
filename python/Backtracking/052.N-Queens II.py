/*
 N-Queens 问题的变形，只是统计结果的种类，代码更加简单了
*/

#python 版本
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True
        def dfs(depth, valuelist):
            if depth==n: res.append(valuelist); return
            for i in range(n):
                if check(depth,i): 
                    board[depth]=i
                    s='.'*n
                    dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]])
        board=[-1 for i in range(n)]
        res=[]
        dfs(0,[])
        return len(res)


#Java 版本
'''
public class Solution 
{
    private int res=0;
    public int totalNQueens(int n) 
    {  
        int[] loc = new int[n];  //记录皇后处于哪一列，列数组
        dfs(loc,0,n);  
        return res;  
    }  
    public void dfs(int[] loc, int cur, int n)
    {  
        if(cur==n)   
            res++;  
        else
        {  
            for(int i=0;i<n;i++)
            {  
                loc[cur] = i;  
                if(isValid(loc,cur))  
                    dfs(loc,cur+1,n); 
            }  
        }  
    }  
    public boolean isValid(int[] loc, int cur)
    {  
        for(int i=0;i<cur;i++)//只需要保证与那些已经就位的皇后不冲突即可  
        {  
            if(loc[i]==loc[cur]||Math.abs(loc[i]-loc[cur])==(cur-i)) //验证对角线，根据对角线性质，长 ＝ 宽 
                                                                     //那么我们不难写出 Math.abs(loc[i] - loc[cur]) == (cur - i) 
                return false;  
        }  
        return true;  
    }  

}
'''
