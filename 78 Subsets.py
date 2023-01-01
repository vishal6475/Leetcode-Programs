class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """ Method 1
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
        """
        
        power = [[]]
        rev_index = dict()
        for i in range(len(nums)):
            power.append([nums[i]])
            rev_index[nums[i]] = i
        
        n = len(nums)
        start = 1
        end = n
        count = 1
        
        while count > 0:
            count = 0
            for sub in range(start, end+1):            
                cur = power[sub]
                for i in range(rev_index[cur[-1]]+1, n):
                    nxt = cur.copy()
                    nxt.append(nums[i])
                    power.append(nxt)
                    count += 1
            start, end = end + 1, end + count                
                
        return power
            
        
sol = Solution()

print(sol.subsets([1,2,3,4]))