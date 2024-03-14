from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums2 + nums1
    nums.sort()
    leng = len(nums)
    if leng % 2 == 1:
        return nums[leng // 2]
    else:
        return (nums[leng // 2 - 1] + nums[leng // 2]) / 2


class Solution:
    sums1 = [1,3]
    sums2 = [2,4]
    print(findMedianSortedArrays(sums1,sums2))
