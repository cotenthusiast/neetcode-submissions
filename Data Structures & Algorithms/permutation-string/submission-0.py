class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_map = {} # checked string
        s2_map = {} # running string
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]
            if c1 in s1_map:
                s1_map[c1] += 1
            else:
                s1_map[c1] = 1
                
            if c2 in s2_map:
                s2_map[c2] += 1
            else:
                s2_map[c2] = 1

        if self.check_equal(s1_map, s2_map):
            return True
        i = len(s1)
        while i < len(s2):
            s2_map[s2[i-len(s1)]] -= 1
            if s2[i] in s2_map:
                s2_map[s2[i]] += 1
            else:
                s2_map[s2[i]] = 1
            if self.check_equal(s1_map, s2_map):
                return True
            i += 1
        return False




    def check_equal(self, s1, s2):
        for key, value in list(s2.items()):
            if value == 0:
                del s2[key]
        for key, value in s2.items():
            if not (key in s1 and s1[key] == value):
                return False
        return True

        