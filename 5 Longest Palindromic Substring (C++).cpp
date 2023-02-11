class Solution {
public:
    string longestPalindrome(string s) {
    string str(s);
    int length = str.size();
    int arr[length][length];

    // BASE CASE:
    int max_length=0, max_i=0, max_j=0;
        
    for (int i=0; i<length; i++) {
        for (int j=i; j<length; j++){
            arr[i][j] = 0;
            if (i == j) {
                arr[i][j] = 1;
                if ((j-i+1) > max_length) {
                    //cout << "Here" << i << " " << j << endl;
                    max_length = j-i+1;
                    max_i=i;
                    max_j=j;
                }
            }
            if (j==i+1)
                if(str[i] == str[j]) {
                    arr[i][j] = 1;
                    if ((j-i+1) > max_length) {
                        //cout << "Here" << i << " " << j << endl;
                        max_length = j-i+1;
                        max_i=i;
                        max_j=j;
                    }
                }
        }
    }

    // ALGORITHM:
    for (int len=3; len<=length; len++) {
        for (int i=0; i<=length-len; i++) {
            int j = i+len-1;
            if (arr[i+1][j-1] == 1)
                if (str[i] == str[j]) {
                    arr[i][j] = 1;
                    if ((j-i+1) > max_length) {
                        //cout << "Here" << i << " " << j << endl;
                        max_length = j-i+1;
                        max_i=i;
                        max_j=j;
                    }
                }
        }
    }


    return str.substr(max_i, max_j+1-max_i);
        
    }
};