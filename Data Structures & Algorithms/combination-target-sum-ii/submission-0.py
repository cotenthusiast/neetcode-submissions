from typing import List


class Solution:

  def combinationSum2(
      self, candidates: List[int], target: int
  ) -> List[List[int]]:
    result = []
    # Sort the candidates so we can easily skip duplicates
    candidates.sort()

    def backtrack(start: int, current_path: List[int], target_left: int):
      if target_left == 0:
        result.append(list(current_path))
        return
      if target_left < 0:
        return

      for i in range(start, len(candidates)):
        # Skip duplicates at the same level of recursion
        if i > start and candidates[i] == candidates[i - 1]:
          continue

        # Since candidates are sorted, if the current number exceeds
        # the remaining target, all subsequent numbers will too.
        if candidates[i] > target_left:
          break

        current_path.append(candidates[i])
        # Pass i + 1 because each element can only be used once
        backtrack(i + 1, current_path, target_left - candidates[i])
        current_path.pop()  # Backtrack

    backtrack(0, [], target)
    return result