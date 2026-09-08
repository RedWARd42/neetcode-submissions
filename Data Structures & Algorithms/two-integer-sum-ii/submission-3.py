class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            compli = target - numbers[i]
            if compli in hashmap:
                return [hashmap[compli] + 1, i + 1]
            if numbers[i] not in hashmap:
                hashmap[numbers[i]] = i