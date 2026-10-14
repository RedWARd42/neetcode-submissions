class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        group = set(nums)
        max_length = 0
        for num in nums:
            if (num - 1) not in group:
                length = 0
                while (num + length) in group:
                    length += 1
                    max_length = max(length, max_length)
        return max_length

            