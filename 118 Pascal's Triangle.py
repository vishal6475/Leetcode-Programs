
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        output = [[1]]
        
        if numRows > 1:
            for _ in range(numRows - 1):
                last = output[-1]
                
                to_add = []
                to_add.append(1)
                
                for i in range(len(last) - 1):
                    to_add.append(last[i]+last[i+1])
                    
                to_add.append(1)
                
                output.append(to_add)            
        
        return output        
        
        
sol = Solution()

print(sol.generate(5))