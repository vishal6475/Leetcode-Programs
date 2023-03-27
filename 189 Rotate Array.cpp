class Solution {
public:
    void rotate(vector<int>& nums, int k) {

        cout << nums.size() << ":" << k << "\n";

        for (int i=0; i<k; i++) {
            int n = nums.back();
            nums.pop_back();
            nums.insert(nums.begin(), n);
        }
        
    }
};