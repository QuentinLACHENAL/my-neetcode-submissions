class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while (L <= R):
            idx = int(((R - L) / 2) + L)
            if nums[idx] < target:
                L = idx + 1
            elif nums[idx] > target:
                R = idx - 1
            else:
                return idx
        return -1
