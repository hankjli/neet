class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_counts = {}
        t_counts = {}

        for c in s:
            s_counts[c] = s_counts.setdefault(c, 0) + 1
        
        for c in t:
            t_counts[c] = t_counts.setdefault(c, 0) + 1
        
        return s_counts == t_counts