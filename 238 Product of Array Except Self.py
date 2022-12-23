class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left = [1] * len(nums)
        right = [1] * len(nums)
        n = len(nums)
        
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = nums[i] * left[i-1]
        
        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = nums[i] * right[i+1]
        
        nums[0] = right[1]
        nums[n-1] = left[n-2]
        
        for i in range(1, n-1):
            nums[i] = left[i-1] * right[i+1]
            
        return nums
        
        
        
sol = Solution()

print(sol.productExceptSelf([-1,1,0,-3,3]))