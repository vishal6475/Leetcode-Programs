class Solution {
public:
    int houserob(vector<int>& nums) {

        int l = nums.size();

        if (l == 1) return nums[0];
        else if (l == 2) return max(nums[0], nums[1]);
        else if (l == 3) return max(nums[0]+nums[2], nums[1]);
        else{
            vector<int> opt(nums.size(), 0);
            opt[0] = nums[0];
            opt[1] = nums[1];
            opt[2] = nums[0]+nums[2];

            for(int i=3; i<nums.size(); i++){
                opt[i] = nums[i] + max(opt[i-2], opt[i-3]);
            }
            return *max_element(opt.begin(), opt.end());
        }        
    }

    int rob(vector<int>& nums) {

        int ln = nums.size();

        if (ln == 1) return nums[0];
        else{
            vector<int> nums1(nums.begin(), nums.end()-1);
            vector<int> nums2(nums.begin()+1, nums.end());

            return max(houserob(nums1), houserob(nums2));
        }
        
    }
};