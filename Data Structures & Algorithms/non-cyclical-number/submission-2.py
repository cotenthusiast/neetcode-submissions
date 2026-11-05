class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        num = n

        while num not in seen:
            seen.add(num)
            total = 0
            for i in range(len(str(num))):
                total += int(str(num)[i]) ** 2
            if total == 1:
                return True
            num = total

        return False