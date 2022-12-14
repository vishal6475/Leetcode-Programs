class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        opt = [0 for _ in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])
        else:
            opt[0] = nums[0]
            opt[1] = nums[1]
            opt[2] = nums[0] + nums[2]
            for i in range(3, len(nums)):
                opt[i] = nums[i] + max(opt[i-2], opt[i-3])
            return max(opt[len(nums)-1], opt[len(nums)-2])        


sol = Solution()

print(sol.rob([2, 7, 9, 3, 1, 8, 2, 7, 9]))