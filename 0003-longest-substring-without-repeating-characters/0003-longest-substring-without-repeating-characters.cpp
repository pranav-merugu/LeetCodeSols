class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        //Sliding window
        if (s.size() == 0){
            return 0;
        }
        int left, right = 0;
        int longest = 1;
        unordered_set<char> chars;
        while (right < s.size()){
            while (chars.find(s[right]) != chars.end()){
                chars.erase(s[left]);
                ++left;
            }
            chars.insert(s[right]);
            longest = max(longest, right - left + 1);
            ++right;
        }
        return longest;
    }
};