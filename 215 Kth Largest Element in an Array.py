class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # counting sort
        minn, maxx = min(nums), max(nums)
        count = [0 for _ in range(maxx - minn + 1)]
        
        for n in nums:
            count[n-minn] += 1
        
        found = 0
        for i in range(maxx - minn, -1, -1):
            found += count[i]
            if found >= k:
                return i + minn
            
        
        
        """ 
        # using quicksort method- Not very good performance
        k = len(nums) - k
        
        def partition(start, end):        
            pivot = start
            for i in range(start, end):
                if nums[i] < nums[end]:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    pivot += 1
                    
            nums[pivot], nums[end] = nums[end], nums[pivot]
            return pivot
            
        low, high = 0, len(nums)-1
        while low <= high:
            pivot = partition(low, high)
            if pivot == k:
                return nums[pivot]
            if k < pivot:
                high = pivot - 1
            else:
                low = pivot + 1
        """
            
        
sol = Solution()

print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))