/*
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
*/

#python 版本

'''
这类型问题统称为递归回溯问题，也可以叫做对决策树的深度优先搜索（dfs）。
N皇后问题有个技巧的关键在于棋盘的表示方法，这里使用一个数组就可以表达了。
比如board=[1, 3, 0, 2]，这是4皇后问题的一个解，意思是：在第0行，皇后放在第1列；在第1行，皇后放在第3列；在第2行，皇后放在第0列；
在第3行，皇后放在第2列。这道题提供一个递归解法，下道题使用非递归。check函数用来检查在第k行，皇后是否可以放置在第j列。
'''
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
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
        return res
        
        
        
#Java 版本
'''
我们把这一题分成几个小问题

1. 传统的dfs递归

2. 验证放置Queen的地方是否合法

3. 输出Board结果

这么做的好处就是，一开始，我们不用建立一个庞大的Board，我们选用一个数组对应Board里面的每一行，数组每一个值对应这一行放置Queen的列号

比如： int[ ] {3,1,4,2} 代表放置的地点分别为[1,3], [2,1], [3,4], [4,2] 这么一来，我们用很简单的用数组表示了整个Board，

而且在isValid函数里判断的时候会非常简洁，而且把输出Board单独隔离了出来


dfs的循环是指这一行里，从第一列到最后一列放置的所有可能，如果放置的地点通过isValid验证，通过cur+1进入下一行进行递归，如果没通过验证，试下一个位置，如果所有位置都不Valid，跳回上一层

采用int[ ]的好处是，每一次我们只需改变一个数字就相当于改变了棋子的放置位置

isValid函数，首先int[ ]代表行，这样就避免了每一行出现重复的Queen （因为你不可能在一个int里面放2个值）这样简化了验证 接下来我们只需验证列和对角线

验证列的时候，要验证这一行之前的行有没有重复的（注意是验证之前的喔）

验证对角线，根据对角线性质，长 ＝ 宽 那么我们不难写出 Math.abs(loc[i] - loc[cur]) == (cur - i) 

最后loc［］里面记录的是解的信息（如果有解）我们把它转换成String, 输出Board即可
'''
'''
public class Solution 
{
	public ArrayList<String[]> solveNQueens(int n) 
    {  
        ArrayList<String[]> res = new ArrayList<String[]>();  
        int[] loc = new int[n];  //记录皇后处于哪一列，列数组
        dfs(res,loc,0,n);  
        return res;  
    }  
    public void dfs(ArrayList<String[]> res, int[] loc, int cur, int n)
    {  
        if(cur==n)   
            printboard(res,loc,n);  
        else
        {  
            for(int i=0;i<n;i++)
            {  
                loc[cur] = i;  
                if(isValid(loc,cur))  
                    dfs(res,loc,cur+1,n);  
            }  
        }  
    }  
    public boolean isValid(int[] loc, int cur)
    {  
        for(int i=0;i<cur;i++)//只需要保证与那些已经就位的皇后不冲突即可  
        {  
            if(loc[i]==loc[cur]||Math.abs(loc[i]-loc[cur])==(cur-i)) //验证对角线，根据对角线性质，长 ＝ 宽 
                       return false;                                 // 那么我们不难写出 Math.abs(loc[i] - loc[cur]) == (cur - i) 
        }  
        return true;  
    }  
    public void printboard(ArrayList<String[]> res, int[] loc, int n)
    {  
        String[] ans = new String[n];  
        for(int i=0;i<n;i++)
        {  
            String row = new String();  
            for(int j=0;j<n;j++)
            {  
                if(j==loc[i]) row += "Q";  
                else row += ".";  
            }  
            ans[i] = row;  
        }  
        res.add(ans);  
    }  
}
'''
