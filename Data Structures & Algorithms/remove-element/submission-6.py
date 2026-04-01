class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums)
        for i in range(len(nums)):
            if i >= last:
                break
            if nums[i] == val:
                while last > 0 and nums[last - 1] == val:
                    last -= 1
                if i >= last:
                    break
                tmp = nums[i]
                nums[i] = nums[last - 1]
                nums[last - 1] = tmp
                last -= 1
        return last
