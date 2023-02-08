class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i=0, j=0, len=0;
        std::map<char, int> sub;
        
        for (j=0; j < s.size(); j++) {
            if(sub.find(s[j]) != sub.end() && sub[s[j]] >= i ) {
                len = max(len, j-i);
                i = sub[s[j]] + 1;
                
            }
            sub[s[j]] = j;            
        }
        len = max(len, j-i);
        
        return len;
    }
};