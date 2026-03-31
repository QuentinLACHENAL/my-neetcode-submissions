class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        for i, num in enumerate(sortedNums):
            if (i + 1) < len(nums):
                if num == sortedNums[i + 1]:
                    return True
        return False