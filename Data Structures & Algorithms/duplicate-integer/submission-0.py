class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contained = {}
        for i in range(len(nums)):
            if(nums[i] in contained):
                return True
            contained[nums[i]] = i
        return False