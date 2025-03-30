class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> complement;
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i){
            int comp = target - nums[i];
            if (complement.find(comp) != complement.end()){
                result.push_back(complement[comp]);
                result.push_back(i);
                break;
            }
            complement[nums[i]] = i;
        }
        return result;
    }
};