class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapOne = {}
        mapTwo = {}

        for i in range(len(s)):
            if s[i] not in mapOne:
                mapOne[s[i]] = 1
            else:
                mapOne[s[i]] += 1
            if t[i] not in mapTwo:
                mapTwo[t[i]] = 1
            else:
                mapTwo[t[i]] += 1
            
        if mapOne != mapTwo:
            return False
        
        return True
                