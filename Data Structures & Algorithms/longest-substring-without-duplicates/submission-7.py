class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        max_length = 1
        current_length = 0
        left = 0
        right = 1
        current_set = set([s[0]])
        while right != len(s):
            
            current_length = right - left
            if s[right] not in current_set:
                current_set.add(s[right])
                current_length += 1
                if max_length < current_length:
                    max_length = current_length
                right += 1

            else:
                while s[right] in current_set:
                    current_set.remove(s[left])
                    left += 1

                current_set.add(s[right])
                right += 1

        return max_length
            

