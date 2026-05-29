class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        sorted_nums = sorted(hashmap.keys(), key=lambda num: hashmap[num], reverse=True)
        return sorted_nums[:k]
