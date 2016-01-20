'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
'''
解题思路：这道题使用bfs来解决。参考：http://chaoren.is-programmer.com/posts/43039.html 使用BFS, 单词和length一块记录, 

dict中每个单词只能用一次, 所以用过即删。dict给的是set类型, 检查一个单词在不在其中(word in dict)为O(1)时间。

设单词长度为L, dict里有N个单词, 每次扫一遍dict判断每个单词是否与当前单词只差一个字母的时间复杂度是O(N*L), 

而每次变换当前单词的一个字母, 看变换出的词是否在dict中的时间复杂度是O(26*L), 所以要选择后者。
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        dict.add(end)
        q = []
        q.append((start, 1))
        while q:
            curr = q.pop(0)
            currword = curr[0]; currlen = curr[1]
            if currword == end: return currlen
            for i in range(len(start)):
                part1 = currword[:i]; part2 = currword[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in dict:
                            q.append((nextword, currlen+1)); 
                            dict.remove(nextword)
        return 0
