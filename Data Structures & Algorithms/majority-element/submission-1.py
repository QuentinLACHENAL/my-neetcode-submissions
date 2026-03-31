class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        for num in nums:
            if not num in numsDict:
                numsDict[num] = 1
            else:
                numsDict[num] += 1
        for key in numsDict:
            if numsDict.get(key) > (len(nums) / 2):
                return key