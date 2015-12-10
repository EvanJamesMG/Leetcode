/*
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note: Given target value is a floating point. You are guaranteed to have only one unique value in the BST that is closest to the target.
*/


/* 递归法

复杂度

时间 O(logN) 空间 O(H)

思路

根据二叉树的性质，我们知道当遍历到某个根节点时，最近的那个节点要么是在子树里面，要么就是根节点本身。

所以我们根据这个递归，返回子树中最近的节点，和根节点中更近的那个就行了。

代码
*/

public class Solution {
    public int closestValue(TreeNode root, double target) {
        // 选出子树的根节点
        TreeNode kid = target < root.val ? root.left : root.right;
        // 如果没有子树，也就是递归到底时，直接返回当前节点值
        if(kid == null) return root.val;
        // 找出子树中最近的那个节点
        int closest = closestValue(kid, target);
        // 返回根节点和子树最近节点中，更近的那个节点
        return Math.abs(root.val - target) < Math.abs(closest - target) ? root.val : closest;
    }
}



/* 迭代法

复杂度

时间 O(logN) 空间 O(H)

思路

记录一个最近的值，然后沿着二叉搜索的路径一路比较下去，并更新这个最近值就行了。

因为我们知道离目标数最接近的数肯定在二叉搜索的路径上。

代码*/

public class Solution {
    public int closestValue(TreeNode root, double target) {
        int closest = root.val;
        while(root != null){

            // 二叉搜索
            root = target < root.val ? root.left : root.right;
			
			// 如果该节点的离目标更近，则更新到目前为止的最近值
            closest = Math.abs(closest - target) < Math.abs(root.val - target) ? closest : root.val;
        }
        return closest;
    }
}