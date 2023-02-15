class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        topK = [[] for _ in range(len(nums)+1)]
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key in count:
            topK[count[key]].append(key)
        
        out = []
        found = 0
        for i in range(len(nums), -1, -1):
            if len(topK[i]) > 0:
                out.extend(topK[i])
                found += len(topK[i])
                if found >= k:
                    return out
            
        
sol = Solution()

print(sol.topKFrequent([1], 1))