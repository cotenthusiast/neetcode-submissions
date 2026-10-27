from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        q = deque()
        visited = {beginWord}

        def one_letter_apart(a: str, b: str) -> bool:
            diff = 0
            for x, y in zip(a, b):      # walk both words in parallel
                if x != y:
                    diff += 1
                    if diff > 1:        # early exit: already too different
                        return False
            return diff == 1

        def distances(q: deque, current_distance: int, current_word: str) -> None:
            for word in wordList:
                if word not in visited and one_letter_apart(word, current_word):
                    visited.add(word)                         # mark when enqueuing
                    q.append((word, current_distance + 1))

        distances(q, 0, beginWord)

        while q:
            current_word, current_distance = q.popleft()
            if current_word == endWord:
                return current_distance + 1     # steps + 1 = number of words
            distances(q, current_distance, current_word)

        return 0
            