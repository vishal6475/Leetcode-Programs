class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        cstr = '11'
        
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:        
            for _ in range(n-2):
                new_cstr = ''
                
                sum = 1
                
                for i in range(1, len(cstr)):
                    if cstr[i] != cstr[i-1]:
                        new_cstr += str(sum) + cstr[i-1]
                        sum = 1
                    else:
                        sum += 1                        
                
                new_cstr += str(sum) + cstr[len(cstr)-1]                
                cstr = new_cstr                
        
        return cstr

sol = Solution()

print(sol.countAndSay(5))