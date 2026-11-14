class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(dp)):
            for word in wordDict:
                if i - len(word) >= 0 and dp[i - len(word)] != 0:
                    is_seg = True
                    for j in range(len(word)):
                        # print(word[j])
                        # print(s[i - len(word) + j])
                        if word[j] != s[i - len(word) + j]:
                            is_seg = False
                            break
                        
                    if is_seg:
                        dp[i] = 1
                        break
        
        return dp[-1] == 1