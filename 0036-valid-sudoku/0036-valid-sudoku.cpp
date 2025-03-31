class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (auto &v: board){
            unordered_set<int> nums;
            for (auto c: v){
                if (c != '.'){
                    if (nums.find(c - '0') != nums.end()){
                        return false;
                    } else{
                        nums.insert(c - '0');
                    }
                }
            }
        }

        for (int i = 0; i < 9; ++i){
            unordered_set<int> colNums;
            for (auto &v: board){
                if (v[i] != '.'){
                    if (colNums.find(v[i] - '0') != colNums.end()){
                        return false;
                    } else{
                        colNums.insert(v[i] - '0');
                    }
                }
            }
        }

        unordered_set<int> boxNums[9];
        for (int i = 0; i < 9; ++i){
            for (int j = 0; j < 9; ++j){
                int boxInd = (i / 3) * 3 + (j / 3);
                if (board[i][j] != '.'){
                    if (boxNums[boxInd].find(board[i][j]) != boxNums[boxInd].end()){
                        return false;
                    } else{
                        boxNums[boxInd].insert(board[i][j]);
                    }
                }
            }
        }



        return true;
    }
};