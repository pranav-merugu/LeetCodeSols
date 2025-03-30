class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyPrice = prices[0];
        int profit = 0;
        for (auto &price: prices){
            if (price < buyPrice){
                buyPrice = price;
            }
            profit = max(profit, price - buyPrice);
        }
        return profit;
    }
};