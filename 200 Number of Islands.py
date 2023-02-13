class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])        
        count = 1        
        
        def formIsland(i, j):
            grid[i][j] = str(count)
            if i>0:
                if grid[i-1][j] == '1':
                    formIsland(i-1, j)                    
                
            if j>0:
                if grid[i][j-1] == '1':
                    formIsland(i, j-1)
                
            if i<m-1:
                if grid[i+1][j] == '1':
                    formIsland(i+1, j)
                
            if j<n-1:
                if grid[i][j+1] == '1':
                    formIsland(i, j+1)                
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    formIsland(i, j)
                    
        return count-1
                    

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()

print(sol.numIslands(grid))