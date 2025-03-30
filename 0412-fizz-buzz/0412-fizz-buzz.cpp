class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> result;
        for (int i = 1; i <= n; ++i){
            string FizzBuzz = "";
            if (i % 3 == 0 && i % 5 == 0){
                FizzBuzz += "FizzBuzz";
            } else if (i % 3 == 0){
                FizzBuzz += "Fizz";
            } else if (i % 5 == 0){
                FizzBuzz += "Buzz";
            } else{
                FizzBuzz += to_string(i);
            }
            result.push_back(FizzBuzz);
        }
        return result;
    }
};