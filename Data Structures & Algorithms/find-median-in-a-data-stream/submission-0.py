class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        left = 0
        right = len(self.stream) - 1
        mid = 0
        while left<=right:
            mid = (left+right) // 2
            if self.stream[mid] == num:
                self.stream.insert(mid, num)
                return
            elif self.stream[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        self.stream.insert(left, num)

    def findMedian(self) -> float:
        if len(self.stream) % 2 != 0:
            return self.stream[len(self.stream)//2]
        else:
            return (self.stream[len(self.stream)//2] + self.stream[len(self.stream)//2-1] ) /2
        
        