class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # need to keep track of prev day temperatures
            # need to preserve ORDER and TEMP
        
        res = [0] * len(temperatures)

        prev_days = []

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while prev_days and temp > temperatures[prev_days[-1]]:
                res[prev_days[-1]] = i - prev_days[-1]
                prev_days.pop()
            
            prev_days.append(i)
        
        return res