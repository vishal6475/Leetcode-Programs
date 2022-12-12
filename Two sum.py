class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = dict()
        for idx, number in enumerate(nums):
            print(idx, number)
            if target-number in check:
                return [check[target-number], idx]
            else:
                check[number] = idx
            print(check)
            
        return None
    


sol = Solution()
print(sol.twoSum([2,7,11,15, 4], 6))