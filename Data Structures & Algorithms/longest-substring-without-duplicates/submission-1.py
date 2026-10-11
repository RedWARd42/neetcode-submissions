class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left = 0
        length = 0
        for i in range(len(s)):
            while s[i] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[i])
            length = max(length, i - left + 1)
        return length

            
                