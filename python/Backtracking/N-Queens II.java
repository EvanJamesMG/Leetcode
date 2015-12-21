/*
 N-Queens 问题的变形，只是统计结果的种类，代码更加简单了
*/
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