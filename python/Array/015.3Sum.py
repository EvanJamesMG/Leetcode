# coding=utf-8

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
类似于3Sum Closest  也是先排序，后夹逼
'''
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()

    for i in range(len(nums)-2):
        tem = -nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[j] + nums[k] < tem:
                j += 1
            elif nums[j] + nums[k] > tem:
                k -= 1
            else:
                temlist = [nums[i], nums[j], nums[k]]
                if temlist not in res:
                    res.append(temlist)
                j += 1
                k -= 1
    return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
# if __name__ == "__main__":
#
#     result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
#     print(result)
#
