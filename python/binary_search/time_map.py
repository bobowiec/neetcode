class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_store.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] < timestamp:
                left = mid + 1
            elif values[mid][1] > timestamp:
                right = mid - 1
            else:
                return values[mid][0]
        return values[right][0] if right != -1 else ""
