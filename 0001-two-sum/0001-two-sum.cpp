class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> complement;
        for (int i = 0; i < nums.size(); ++i){
            int comp = target - nums[i];
            if (complement.find(comp) != complement.end()){
                return {complement[comp], i};
            }
            complement[nums[i]] = i;
        }
        return {};
    }
};