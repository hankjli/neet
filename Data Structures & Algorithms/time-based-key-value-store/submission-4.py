class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.store:
            return ""
        
        values = self.store[key]
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = int((l + r) / 2)
            cur = values[mid]

            if cur[1] <= timestamp:
                res = cur[0]

                l = mid + 1
            else:
                r = mid - 1
        
        return res

