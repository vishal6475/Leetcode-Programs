
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]
        
        maxx, minn = 1, 1
        max_p = 0
        
        for n in nums:
            if n == 0:
                maxx, minn = 1, 1
            else:
                maxx, minn = max(n, n*maxx, n*minn), min(n, n*maxx, n*minn)
                max_p = max(max_p, maxx)
                
            print(n, minn, maxx, max_p)
                
        return max_p
                
        
        """ First approach (not good)
        if len(nums) == 1: return nums[0]
        
        max_product = 0
        product = 0
        i = 0
        prod = [0, 0, 0]
        first_n = 0
        last_n = 0
        negs = 0
        
        for ele in nums:
            if ele == 0:                
                if prod[1] == 0: prod[1] = 1
                if negs == 0: 
                    max_product = max(prod[0], max_product)
                if negs == 1:
                    max_product = max(prod[0], prod[2], max_product)
                elif negs % 2 == 0:
                    product = max(1, prod[0]) * first_n * prod[1] * last_n * max(1, prod[2])
                else:
                    product = max(max(1, prod[0]) * first_n * prod[1], prod[1] * last_n * max(1, prod[2]))                          
                    
                max_product = max(product, max_product)
                i = 0
                prod = [0, 0, 0]
                first_n = 0
                last_n = 0
                negs = 0
            elif ele < 0:          
                negs += 1
                if negs == 1: 
                    first_n = ele
                    i = 2
                elif negs == 2:        
                    prod[1] = prod[2]                    
                    prod[2] = 0
                else:    
                    if prod[1] == 0: prod[1] = 1
                    prod[1] = prod[1] * last_n * max(1, prod[2])
                    prod[2] = 0
                    
                last_n = ele
            else:
                if prod[i] == 0: prod[i] = 1
                prod[i] *= ele
                
            
        if negs == 0: 
            return max(prod[0], max_product)
        if negs == 1:
            return max(prod[0], prod[2], max_product)
        else:       
        
            if negs % 2 == 0:
                if prod[1] == 0: prod[1] = 1
                product = max(1, prod[0]) * first_n * prod[1] * last_n * max(1, prod[2])
            else:
                if prod[1] == 0: prod[1] = 1
                product = max(max(1, prod[0]) * first_n * prod[1], prod[1] * last_n * max(1, prod[2]))                          
                    
            return max(product, max_product)
        """
        


sol = Solution()

print(sol.maxProduct([3, -1, 4]))
