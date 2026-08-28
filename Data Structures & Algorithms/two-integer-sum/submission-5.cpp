class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashmap;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int remainder = target - num;
            if (hashmap.contains(remainder)) {
                return {hashmap[remainder], i};
            } else {
                hashmap[num] = i;
            }
        }
    }
};
