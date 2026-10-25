class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed = [(position[i], speed[i]) for i in range(len(position))]

        pos_speed.sort()
        res = 0
        prev_times_needed = []

        for i in range(len(position) - 1, -1, -1):
            time_needed = ((target - pos_speed[i][0]) / pos_speed[i][1])

            if not prev_times_needed:
                prev_times_needed.append(time_needed)
                res += 1
            elif time_needed <= prev_times_needed[-1]:
                continue
            else:
                prev_times_needed.append(time_needed)
                res += 1
        
        return res