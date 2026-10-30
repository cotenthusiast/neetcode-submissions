class TimeMap:

    def __init__(self):
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}

        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or list(self.map[key].keys())[0] > timestamp:
            return ""
        temp = list(self.map[key].keys())
        last_valid = temp[0]
        left = 0
        right = len(temp) - 1

        while right>=left:
            mid = (left+right)//2
            
            if temp[mid] == timestamp:
                last_valid = timestamp
                break
            if temp[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                last_valid = max(last_valid, temp[mid])
        
        return self.map[key][last_valid]
