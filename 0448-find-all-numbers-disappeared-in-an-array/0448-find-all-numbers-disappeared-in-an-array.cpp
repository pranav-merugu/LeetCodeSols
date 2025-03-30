class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (auto num: nums){
            int index = abs(num) - 1;
            nums[index] = -1 * abs(nums[index]);
        }
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i){
            if (nums[i] > 0){
                result.push_back(i+1);
            }
        }
        return result;
    }
};