class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        self.max_at = -1
        self.final_low = 0
        self.final_high = len(nums) - 1
        
        if nums[-1] < nums[0]:
            low = 0
            high = len(nums) - 1
            
            while low <= high:
                mid = (low + high) // 2
                if mid == 0:
                    if nums[1] < nums[0]:
                        self.max_at = mid
                        break
                    else:
                        low = 1
                        continue
                elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    self.max_at = mid
                    break
                
                if nums[mid] > nums[0]:     
                    low = mid + 1  
                else:
                    high = mid - 1    
                    
            if target >= nums[0]:
                self.final_high = self.max_at
            else:
                self.final_low = self.max_at + 1
                
        
        low = self.final_low
        high = self.final_high
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                high = mid - 1         
            else:
                low = mid + 1    
                        
        return -1
        

sol = Solution()

print(sol.search([8,9,2,3,4], 9))