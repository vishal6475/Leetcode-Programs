class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        power = [[]]
        subs = []
        rev_index = dict()
        for i in range(len(nums)):
            subs.append([nums[i]])
            rev_index[nums[i]] = i
        
        while len(subs) > 0:
            cur = subs.pop(0)
            power.append(cur)
            for i in range(rev_index[cur[-1]]+1, len(nums)):
                nxt = cur.copy()
                nxt.append(nums[i])
                subs.append(nxt)
                
        return power
            
        
sol = Solution()

print(sol.subsets([1,2,3,4]))