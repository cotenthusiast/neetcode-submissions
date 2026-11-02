class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def backtrack(word1, word2, i1, i2, cache):
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            if (i1 == len(word1)):
                cache[(i1, i2)] = len(word2) - i2
                return cache[(i1, i2)]
            if (i2 == len(word2)):
                cache[(i1, i2)] = len(word1) - i1
                return cache[(i1, i2)]
            if word1[i1] == word2[i2]:
                return backtrack(word1, word2, i1 + 1, i2 + 1, cache)
            else:
                count = min(
                    1 + backtrack(word1, word2, i1 + 1, i2 + 1, cache), #replace
                    1 + backtrack(word1, word2, i1, i2 + 1, cache),     #insert
                    1 + backtrack(word1, word2, i1 + 1, i2, cache)      #delete
                )
                cache[(i1, i2)] = count
                return count

        cache = {}
        return backtrack(word1, word2, 0, 0, cache)