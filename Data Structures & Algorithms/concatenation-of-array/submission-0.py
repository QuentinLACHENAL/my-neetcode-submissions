class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        newArray = [0] * 2 * length
        for i in (range(2 * length)):
            newArray[i] = nums[i % length ]
        return newArray
