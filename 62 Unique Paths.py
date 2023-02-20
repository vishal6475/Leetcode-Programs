class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        """
        # Recursive method        
        def countPath(i, j):            
            if i==m-1 or j==n-1:
                return 1
            
            return countPath(i+1, j) + countPath(i, j+1)            
            
        return countPath(0,0)
        """
        
        
        # DP method
        dp = [[1] * n for _ in range(m)]
        
        for j in range(n-2, -1, -1):
            for i in range(m-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]              
        
        return dp[0][0]    
        
sol = Solution()
        
print(sol.uniquePaths(23, 12))