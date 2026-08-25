class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            key = ''.join(sorted(string))

            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]

        return list(hashmap.values())