from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        #1124817413
        #[1124][8][17][4][13]

        @cache
        def climbing_stairs(i):
            if i <= 1:
                return 1
            return climbing_stairs(i - 1) + climbing_stairs(i - 2)

        partitions = []
        current = ""

        for i in range(len(s)):
            c = s[i]

            if c == '0':
                # 0 with nothing valid before it -> impossible
                if i == 0 or s[i - 1] not in '12':
                    return 0
                # if valid 0, steal last number before it and count the both of them as one thing
                # -> remove that number from the current partition, and the "10"/"20" is discarded (only 1 way)
                current = current[:-1]
                partitions.append(current)
                current = ""
                continue

            # previous digit and this one can't make a letter -> cut here
            if current and not (10 <= int(current[-1] + c) <= 26):
                partitions.append(current)
                current = ""

            current += c

        partitions.append(current)

        total = 1
        for p in partitions:
            total *= climbing_stairs(len(p))
        return total