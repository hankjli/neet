class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = {}
        t_counts = {}

        for i in range(len(s)):
            s_counts[s[i]] = s_counts.setdefault(s[i], 0) + 1
            t_counts[t[i]] = t_counts.setdefault(t[i], 0) + 1
        
        return s_counts == t_counts