class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            t = t.replace(c, "", 1)
        if t == "":
            return True
        return False