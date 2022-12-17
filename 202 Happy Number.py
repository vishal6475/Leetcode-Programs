

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        checked = dict()
        
        while True:
            ints = []
            while n > 0:
                ints.append(n % 10)
                n = n//10
                
            for ele in ints:
                n += ele*ele
                
            if n == 1: return True
            
            if n in checked: return False
            else: checked[n] = 0
        
sol = Solution()

print(sol.isHappy(243))