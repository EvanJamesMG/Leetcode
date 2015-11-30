
/*
维持一个长度为k的window, 每次检查新的值是否与原来窗口中的所有值的差值有小于等于t的.如果用两个for循环会超时O(nk). 
使用treeset( backed by binary search tree) 的subSet函数,可以快速搜索. 复杂度为 O(n logk)
*/
/*	 public class Solution {
	     public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
	         if(k < 1 || t < 0)
	             return false;
	         TreeSet<Integer> set = new TreeSet<Integer>();
	         for(int i = 0; i < nums.length; i++){
	             int n = nums[i];
	             if(set.floor(n) != null && n <= t + set.floor(n) || 
	                     set.ceiling(n) != null && set.ceiling(n) <= t + n)
	                 return true;
	             set.add(n);
	             if (i >= k)
	                 set.remove(nums[i - k]);
	         }
	         return false;
	     }
	 }*/

	import java.util.SortedSet; 
	public class test {
	    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
	    	if (k < 1 || t < 0)
	    		return false;
	     
	    	SortedSet<Long> set = new TreeSet<Long>();
	     
	    	for (int j = 0; j < nums.length; j++) {
	    		long leftBoundary = (long) nums[j] - t;
	    		long rightBoundary = (long) nums[j] + t + 1;
	    		SortedSet<Long> subSet = set.subSet(leftBoundary, rightBoundary);//是返回集合的高点(不包括)。
	     
	    		if (!subSet.isEmpty())
	    			return true;
	     
	    		set.add((long) nums[j]);
	     
	    		if (j >= k) {
	    			set.remove((long) nums[j - k]);
	    		}
	    	}
	     
	    	return false;
	    }
	}

