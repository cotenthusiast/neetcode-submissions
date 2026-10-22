class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True

        running_max = [0, 0, 0]
        for i in range(len(triplets)):
            if running_max == target:
                return True            
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            running_max[0], running_max[1], running_max[2] = max(running_max[0], triplets[i][0]), max(running_max[1], triplets[i][1]), max(running_max[2], triplets[i][2])
        return running_max == target 
