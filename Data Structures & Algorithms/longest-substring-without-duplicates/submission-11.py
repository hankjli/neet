class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        seen = {}

        l = 0
        for r in range(len(s)):
            cur = s[r]

            if cur not in seen:
                seen[cur] = r
            else:
                while l < seen[cur]:
                    del seen[s[l]]
                    l += 1
                
                l += 1
                seen[cur] = r
            
            cur_len = r - l + 1
            res = max(cur_len, res)
        
        return res