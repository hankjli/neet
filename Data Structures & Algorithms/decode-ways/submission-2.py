class Solution:
    def numDecodings(self, s: str) -> int:
        
        # for each digit
            # if 1 <= cur <= 9
            # can always take cur
                # can take cur + next if 10 <= cur + next <= 26
            
            # if cur == 0, cannot take

        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(dp)):
            cur = s[i - 1]

            if "1" <= cur <= "9":
                dp[i] += dp[i - 1]
            
            double = s[i - 2] + cur
            if "10" <= double <= "26":
                dp[i] += dp[i - 2]
        
        return dp[-1]

