class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_max = 0
        for idx, i in enumerate(nums):
            if idx <= cur_max:                
                if idx + i >= len(nums) - 1:
                    return True
                else:
                    cur_max = max(idx + i, cur_max)
            else:
                return False
            
        return False
        
        
        
        
        
sol = Solution()

print(sol.canJump([3,0,8,2,0,0,1]))