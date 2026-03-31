class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffList = {}
        for i, num in enumerate(nums):
            diff = target - num
            if num in diffList:
                return [diffList[num], i]
            diffList[diff] = i