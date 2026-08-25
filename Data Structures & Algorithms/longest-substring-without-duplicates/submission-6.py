class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lookup_set = set(s[0])
        max_length = 1
        left = 0
        right = 0
        while right < len(s) - 1:
            right += 1
            while s[right] in lookup_set:
                lookup_set.remove(s[left])
                left+=1
            lookup_set.add(s[right])
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length