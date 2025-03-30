class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> countNums;
        for (auto num: nums){
            if (countNums.find(num) != countNums.end()){
                return true;
            } else{
                countNums.insert(num);
            }
        }
        return false;
    }
};