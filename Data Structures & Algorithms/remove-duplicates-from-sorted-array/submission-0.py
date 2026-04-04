class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 1 #to replace
        j = 1 #unique nmbrs
        val = nums[0]
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                val = nums[j]
                j += 1
                i += 1
            else:
                j += 1
        return i
                
