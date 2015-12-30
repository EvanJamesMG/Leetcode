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
结合 算法 3sum
'''
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for i in range(len(nums)):
        tem = threeSum(nums[i+1:], target - nums[i])
        for j in range(len(tem)):
            temlist = [nums[i]]
            temlist.extend(tem[j])
            if temlist not in res:
                res.append(temlist)
    return res

def threeSum(nums2, target2):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums2.sort()

    for i in range(len(nums2)-2):
        tem = target2 - nums2[i]
        j = i + 1
        k = len(nums2) - 1
        while j < k:
            if nums2[j] + nums2[k] < tem:
                j += 1
            elif nums2[j] + nums2[k] > tem:
                k -= 1
            else:
                temlist = [nums2[i], nums2[j], nums2[k]]
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
