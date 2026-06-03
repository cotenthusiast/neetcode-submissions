class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in lookup_set:
                lookup_set.remove(s[left])
                left += 1

            lookup_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length