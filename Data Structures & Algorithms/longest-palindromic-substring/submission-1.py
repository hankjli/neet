class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):

            # first check for odd len palindrome
            l = i
            r = i
            cur = ""

            while l >= 0 and r < len(s) and (s[l] == s[r]):
                if l == r:
                    cur = s[r]
                else:
                    cur = s[l] + cur + s[r]
                
                if len(cur) > res_len:
                    res_len = len(cur)
                    res = cur
                
                l -= 1
                r += 1
            
            # then check for even len palindrome
            l = i
            r = i + 1
            cur = ""
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                cur = s[l] + cur + s[r]
                
                if len(cur) > res_len:
                    res_len = len(cur)
                    res = cur
                
                l -= 1
                r += 1
        
        return res
