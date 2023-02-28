class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic1 = {}
        dic2 = {}
        n1 = len(nums1)
        n2 = len(nums2)
        for i, n in enumerate(nums1):
            if n in dic1:
                dic1[n].append(i)
            else:
                dic1[n] = [i]
        for i, n in enumerate(nums2):
            if n in dic2:
                dic2[n].append(i)
            else:
                dic2[n] = [i]
                
        print(dic1, dic2)
        
        res= []
        
        p1 = p2 = -1
        for i in k:
            for toAdd in range(9, -1, -1):
                while dic1[toAdd][0] <= p1:
                    dic1[toAdd].pop(0)
                while dic2[toAdd][0] <= p2:
                    dic2[toAdd].pop(0)
                    
                if (n2 - dic2[toAdd][0]) and dic2[toAdd]
        
        
sol = Solution()

print(sol.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5))