
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = 0
        c_sum = 0
        
        for ele in nums:
            if ele + c_sum > 0:
                c_sum += ele
            else:
                max_sum = max(max_sum, c_sum)
                c_sum = 0
            max_sum = max(max_sum, c_sum)            
        
        if max_sum == 0:
            max_sum = nums[0]
            for i in range(1, len(nums)):
                if nums[i] > max_sum: max_sum = nums[i]
        return max_sum            
        

sol = Solution()

print(sol.maxSubArray([8]))