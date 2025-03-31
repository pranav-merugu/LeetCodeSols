class Solution {
public:
    string reverseWords(string s) {
        string word = "";
        stringstream ss(s);
        stack<string> words;

        while (ss >> word){
            words.push(word);
        }
        string result = "";
        while (!words.empty()){
            if (words.size() != 1){
                result += words.top() + " ";
            } else{
                result += words.top();
            }
            words.pop();
        }
        return result;
    }
};