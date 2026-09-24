class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"{": "}", "[": "]", "(": ")"}

        openings = []

        for char in s:

            if char in open_to_close:
                openings.append(char)
            else:
                # must be a closing

                if len(openings) > 0 and open_to_close[openings[-1]] == char:
                    openings.pop()
                else:
                    return False

        if len(openings) == 0:
            return True
        else:
            return False