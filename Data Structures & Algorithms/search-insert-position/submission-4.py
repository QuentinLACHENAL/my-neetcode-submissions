class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while R - L > 0:
            half = (L + R) // 2
            if nums[half] < target:
                L = half + 1
            elif nums[half] > target:
                R = half - 1
            elif nums[half] == target:
                return half
        if nums[L] < target:
            return L + 1
        else:
            return L