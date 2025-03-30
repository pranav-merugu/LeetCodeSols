class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        unordered_set numsRange(nums.begin(), nums.end());
        vector<int> result;
        for (int i = 1; i <= nums.size(); ++i){
            if (numsRange.find(i) == numsRange.end()){
                result.push_back(i);
            }
        }
        return result;
    }
};