class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:

        print(key)

        if key not in self.store:
            return ""

        values = self.store[key]

        l = 0
        r = len(values) - 1

        while l < r:
            mid = int((l + r) / 2)
            cur = values[mid]

            if cur[1] > timestamp:
                r = mid - 1
            elif cur[1] < timestamp:
                l = mid + 1
            else:
                return cur[0]
        
        # after exiting loop l == r

        cur = values[l]
        if cur[1] > timestamp:
            if l > 0:
                return values[l - 1][0]
            else:
                return ""
        else:
            return cur[0]

        
        # [4, 6, 12, 56, 62]
