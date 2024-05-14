class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], index]
            lookup[num] = index
        return []