class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        
        for string in strs:

            counts = [0] * 26

            for i in range(len(string)):

                idx = ord(string[i]) - ord("a")
                counts[idx] += 1
            
            
            counts = tuple(counts)
            anagrams.setdefault(counts, []).append(string)

        res = [word for word in anagrams.values()]
        return res