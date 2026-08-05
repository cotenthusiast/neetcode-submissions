class MinStack:

    def __init__(self):
        self.__stack = []
        self.__mins = [float("inf")]

    def push(self, val: int) -> None:
        self.__stack.append(val)
        min = self.__mins[-1]
        if val < self.__mins[-1]:
            min = val
        self.__mins.append(min)

    def pop(self) -> None:
        self.__stack.pop()
        self.__mins.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__mins[-1]
