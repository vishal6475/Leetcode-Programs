class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        unique = set(nums)
        max_length = 1
        
        for n in unique:
            if n-1 not in unique:
                length = 0
                while n+length in unique:
                    length += 1
                max_length = max(max_length, length)
        return max_length
        
sol = Solution()

print(sol.longestConsecutive([100,4,200,1,3,2]))