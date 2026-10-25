class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window len formula = r - l + 1
        
        counts = [0] * 26
        res = 1

        l = 0
        for r in range(len(s)):
            cur = s[r]

            count_idx = ord(cur) - ord('A')
            counts[count_idx] += 1

            most_freq_count = max(counts)
            swaps_needed = sum(counts) - most_freq_count

            if swaps_needed <= k:
                cur_len = r - l + 1
                res = max(res, cur_len)
            else: # invalid window, need to shrink till valid
                while sum(counts) - max(counts) > k:
                    removed_char = s[l]
                    count_idx = ord(removed_char) - ord('A')
                    counts[count_idx] -= 1

                    l += 1

        return res