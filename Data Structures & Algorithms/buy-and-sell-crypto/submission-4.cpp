class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = prices[0];
        int sum = 0;
        int max = 0;
        for (int i = 1; i < prices.size(); i++){
            if (prices[i] <= min) {
                min = prices[i];
            } else {
                sum = prices[i] - min;
                if (sum > max){
                    max = sum;
                }
            }
        }

        return max;
    }
};
