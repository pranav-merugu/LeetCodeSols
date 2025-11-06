#include <map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> letters = {};
        for (char c: s){
            letters[c]++;
        }

        for (char c: t){
            letters[c]--;
        }

        for (const auto& pair: letters){
            if (pair.second != 0){
                return false;
            }
        }

        return true;
    }
};