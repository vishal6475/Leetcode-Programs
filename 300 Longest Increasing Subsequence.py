import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # O(n * logn)
        
        opt = [nums[0]]
        
        for n in nums:
            if n > opt[-1]:
                opt.append(n)
            else:
                opt[bisect.bisect_left(opt, n)] = n
                    
        return len(opt)
        
        """
        # DP approach 1- O(n * n)
        opt = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    opt[i] = max(opt[i], opt[j]+1)
                    
        return max(opt)
        """
                    
        
sol = Solution()

print(sol.lengthOfLIS([90, 100, 70, 60, 40, 40, 20, 200]))