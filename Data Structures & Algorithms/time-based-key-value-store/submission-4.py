class TimeMap:

    def __init__(self):
        self.key_val_timestamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr = self.key_val_timestamp.get(key, [])

        arr.append((value, timestamp))

        self.key_val_timestamp[key] = arr

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_val_timestamp:
            return ""

        arr = self.key_val_timestamp[key]

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return arr[r][0] if r != -1 else ""
