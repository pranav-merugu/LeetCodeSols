class Solution {
public:
    int climbStairs(int n) {
        if (n == 1){
            return 1;
        }
        vector<int> fib = {1, 1};
        for (int i = 2; i <= n; ++i){
            fib.push_back(fib[i-1] + fib[i-2]);
        }
        return fib[n];
    }
};