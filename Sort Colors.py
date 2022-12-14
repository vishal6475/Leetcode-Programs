
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        z, o, t = 0, 0, 0
        
        for n in nums:
            if n == 0: z += 1
            if n == 1: o += 1
            if n == 2: t += 1
        
        nums[:z] = [0 for _ in range(z)]
        nums[z:z+o] = [1 for _ in range(o)]
        nums[z+o:z+o+t] = [2 for _ in range(t)]
             
        return nums

sol = Solution()

print(sol.sortColors([2,0,1]))