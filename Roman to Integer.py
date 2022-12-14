class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sum = 0
        i = 0
        
        val ={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        
        while i < len(s)-1:
            if val[s[i]] >= val[s[i+1]]:
                sum += val[s[i]]
            else:
                sum += val[s[i+1]] - val[s[i]]
                i += 1                 
            
            i += 1            
            
        if i == len(s)-1:
            sum += val[s[i]]  
        
        return sum
        


sol = Solution()

print(sol.romanToInt("MCMXCIV"))
