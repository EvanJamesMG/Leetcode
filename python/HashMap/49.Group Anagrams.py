# coding=utf-8
__author__ = 'EvanJames'
'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

For the return value, each inner list’s elements must follow the lexicographic order.
All inputs will be in lower-case.
'''

'''
利用字典来分组，因为一个word经过排序后，如果一样则属于一个分组，另外组内升序直接sort即可

python 字典 一个key可以对应多个value

'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
          :type strs: List[str]
          :rtype: List[List[str]]
        """
        ref = {}
        length = len(strs)
        for str in strs:
            word = "".join(sorted(str))
            if word in ref:
                ref[word] = ref[word] + [str]
            else:
                ref[word] = [str]
        res = []
        for key in ref:
            l = ref[key]
            l.sort()
            res.append(l)

        return res

if __name__ == '__main__':
    res = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
