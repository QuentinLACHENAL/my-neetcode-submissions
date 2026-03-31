class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i >= (len(nums) - 1):
                return False
            for j in range(k):
                if i + j + 1 >= len(nums):
                    break 
                if nums[i] == nums[i + j + 1]:
                    return True
        return False
            
            
                