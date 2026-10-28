class Solution:
    def countLetters(self, s: str) -> int:

        # aaaa

        l = 0
        res = 0

        for r in range(len(s)):
            if r == len(s) - 1 or s[r] != s[r + 1]:
                sub_len = r - l + 1

                cur_total = int(((sub_len + 1) * (sub_len)) / 2)
                res += cur_total

                l = r + 1
        
        return res