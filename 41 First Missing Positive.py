
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] = -1
            
        for ele in nums:
            if ele >=1 and ele <= n: 
                cur = ele
                while nums[cur-1] >=1 and nums[cur-1] <= n:
                    nxt = nums[cur-1]
                    nums[cur-1] = 0
                    cur = nxt
                
                nums[cur-1] = 0
                
        for i in range(n):
            if nums[i] != 0:
                return i+1
        
        return n+1
        
sol = Solution()

print(sol.firstMissingPositive([7,1,9,3,12, -1, 0, 5, 2, 6, 8, 5, 234, 100, 4, 4,]))
#print(sol.firstMissingPositive([3, 4, 1, 5, 2, 6]))
