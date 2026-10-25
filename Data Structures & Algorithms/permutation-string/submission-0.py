class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.setdefault(char, 0) + 1
        

        sub_counts = {}
        for i in range(len(s1)):
            sub_counts[s2[i]] = sub_counts.setdefault(s2[i], 0) + 1
        
        if s1_counts == sub_counts:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            sub_counts[s2[r]] = sub_counts.setdefault(s2[r], 0) + 1
            sub_counts[s2[l]] -= 1

            if sub_counts[s2[l]] == 0:
                del sub_counts[s2[l]]
            
            if s1_counts == sub_counts:
                return True
            
            l += 1
        
        return False