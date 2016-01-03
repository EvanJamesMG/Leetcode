/*
Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return: ["AAAAACCCCC", "CCCCCAAAAA"].
哈希表法

复杂度

时间 O(N) 空间 O(N)

思路

最简单的做法，我们可以把位移一位后每个子串都存入哈希表中，如果哈希表中已经有这个子串，而且是第一次重复，则加入结果中。如果已经遇到多次，则不加入结果中。如果哈希表没有这个子串，则把这个子串加入哈希表中。

*/
public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> res = new LinkedList<String>();
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for(int index = 10; index <= s.length(); index++){
            // 从第10位开始作为结尾，位移一位，比较一次子串
            String substr = s.substring(index - 10, index);
            if(map.containsKey(substr)){
                // 如果是第一次遇到，则加入结果
                if(map.get(substr) == 1){
                    res.add(substr);
                }
                // 标记为已经遇到过一次了
                map.put(substr, 2);
            } else {
                // 如果不存在，则加入表中
                map.put(substr, 1);
            }
        }
        return res;
    }
}