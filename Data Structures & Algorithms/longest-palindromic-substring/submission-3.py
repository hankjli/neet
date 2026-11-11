class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        res_len = 0

        for i in range(len(s)):
            
            # first check for odd length palindromes
            l = i
            r = i
            cur = None
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    cur = s[l] + cur + s[r] if cur is not None else s[l]
                    l -= 1
                    r += 1

                    if len(cur) > res_len:
                        res_len = len(cur)
                        res = cur
                else:
                    break
            
            # then check even length palindromes 
            l = i
            r = i + 1
            cur = ""
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    cur = s[l] + cur + s[r]
                    l -= 1
                    r += 1

                    if len(cur) > res_len:
                        res_len = len(cur)
                        res = cur
                else:
                    break
        
        return res
