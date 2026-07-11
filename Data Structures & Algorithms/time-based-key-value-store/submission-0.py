class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.time_map.get(key, [])
        arr.append((timestamp, value))

        self.time_map[key] = arr

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        arr = self.time_map.get(key, [])

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2
            value = arr[mid][0]

            if value == timestamp:
                return arr[mid][1]

            if value > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return arr[r][1] if r > -1 else ""
        
