class Solution {
public:
    int compress(vector<char>& chars) {
        if (chars.size() == 1){
            return chars.size();
        }
        string s;
        char prev = chars[0];
        int count = 1;
        for (int i = 1; i < chars.size(); ++i){
            if (chars[i] == prev){
                ++count;
            } else{
                s += prev;
                if (count > 1){
                    s += to_string(count);
                }
                prev = chars[i];
                count = 1;
            }
        }
        s += prev;
        if (count > 1){
            s += to_string(count);
        }
        chars.clear();
        for (auto c: s){
            chars.push_back(c);
        }
        return chars.size();
    }
};