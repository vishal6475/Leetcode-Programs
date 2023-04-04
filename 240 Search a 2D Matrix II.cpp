class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int i = 0, j = matrix[0].size()-1;

        while (i < m && j >= 0) {
            if (matrix[i][j] == target) {
                matrix.clear();
                return true;
            }

            if (matrix[i][j] < target) i++;
            else j--;
        }

        matrix.clear();
        return false;        
    }
};