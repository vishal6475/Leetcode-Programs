
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n > 2:
            opt1, opt2 = 1, 2
            for i in range(3, n+1):
                opt2, opt1 = opt2 + opt1, opt2
            return opt2
            

sol = Solution()

print(sol.climbStairs(45))