
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 0:
            return [-1, -1]
        
        left, right = -1, -1        
        n = len(nums)        
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:                
                if mid == n-1:
                    right = mid
                elif nums[mid] < nums[mid+1]:
                    right = mid
                    
                if mid == 0:
                    left = mid
                    break
                elif nums[mid] > nums[mid-1]:
                    left = mid
                    break
                else:
                    high = mid - 1
                    continue
            
            if target < nums[mid]:
                high = mid - 1         
            else:
                low = mid + 1  
                
        if left > -1 and right == -1:
            low = left
            high = n-1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    if mid == n-1:
                        right = mid
                        break
                    elif nums[mid] < nums[mid+1]:
                        right = mid
                        break
                    else:
                        low = mid + 1
                        continue
                
                if target < nums[mid]:
                    high = mid - 1         
                else:
                    low = mid + 1  
            
                        
        return [left, right]
        
sol = Solution()

print(sol.searchRange([5,7,7,8,8,10], 8))