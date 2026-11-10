class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        res = 0

        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                res = max(res, r - l + 1)
            
            else: # is a duplicate character
                while s[r] in seen:
                    del seen[s[l]]
                    l += 1
                    
            seen[s[r]] = r

        return res