class Solution:
    def reverse(self, x: int) -> int:

        max_pos = 2**31 - 1
        min_neg = -(2**31)

        if x < 0:
            string = list(str(x))
            string = string[1::]
            string = string[::-1]
            string = "".join(string)

            return -int(string) if -int(string) >= min_neg else 0

        else:
            string = list(str(x))
            string = string[::-1]
            string = "".join(string)

            return int(string) if int(string) <= max_pos else 0

        