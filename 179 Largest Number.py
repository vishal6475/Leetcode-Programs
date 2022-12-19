
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        nums.sort(reverse=True)
        res = ''
        for ele in nums:
            res += ele
        
        return res
        

sol = Solution()

#print(sol.largestNumber([10, 2, 0, 0, 5, 34, 547, 32534, 58 , 2,3436, 76, 8, 354]))
print(sol.largestNumber([3,30,34,5,9]))