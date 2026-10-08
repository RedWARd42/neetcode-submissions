class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val in count:
                count[val] += 1
            if val not in count:
                count[val] = 1

        arr = []

        for key, val in count.items():
            arr.append([val, key])
        arr.sort()

        res = []

        for i in range(k):
            res.append(arr.pop()[1])

        return res

