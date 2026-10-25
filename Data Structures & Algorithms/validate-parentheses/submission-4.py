class Solution:
    def isValid(self, s: str) -> bool:

        open_to_close = {"[":"]", "(":")", "{":"}"}

        openings = []
        

        for char in s:
            if char in open_to_close:
                openings.append(char)
            else: # closing parenthesis
                if not openings:
                    return False
                    
                needed_close = open_to_close[openings[-1]]

                if needed_close == char:
                    openings.pop()
                else:
                    return False

        return len(openings) == 0