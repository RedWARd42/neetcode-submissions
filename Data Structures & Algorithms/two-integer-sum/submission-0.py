class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i in range(len(nums)):
            compli = target - nums[i]
            if compli in tracker:
                return [tracker[compli], i]
            if nums[i] not in tracker:
                tracker[nums[i]] = i