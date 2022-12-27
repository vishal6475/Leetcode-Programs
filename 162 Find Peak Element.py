
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 0
        
        low = 0
        high = len(nums)-1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid+1
            
        return low
        
sol = Solution()

print(sol.findPeakElement([1,2,1,3,5,6,4]))