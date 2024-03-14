from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l],height[r]) * (r - l)
            if area > ans:
                ans = area
            # 较短的垂直线向中间移动
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
                l = l + 1
        return ans


class Solution:
    print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))