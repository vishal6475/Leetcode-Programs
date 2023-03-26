class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int maxP = 0, last = prices[0], min = prices[0], max = -1;
        
        for (auto p: prices) {
            if (p > last) max = p;
            else if (p < last and max == -1) min = p;
            else if (p < last) {
                maxP += (max - min);
                min = p;
                max = -1;
            }
            last = p;
        }

        if (max != -1) maxP += (max - min);

        return maxP;
        
    }
};