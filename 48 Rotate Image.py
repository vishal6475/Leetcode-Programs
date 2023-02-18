class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)        
        m = int((n/2)) 
        
        def printMatrix(matrix):
            print()
            for a in range(len(matrix)):
                for b in range(len(matrix[0])):
                    print(matrix[a][b], end=' ')
                print()
        
        printMatrix(matrix)
        
        for i in range(m):
            for j in range(m):
                t = matrix[i][j]
                r = i
                c = j
                matrix[i][j] = matrix[n-1-c][r]
                matrix[n-1-c][r] = matrix[n-1-r][n-1-c]
                matrix[n-1-r][n-1-c] = matrix[c][n-1-r]
                matrix[c][n-1-r] = t
                
                printMatrix(matrix)
                
        if n%2 == 1:
            i = m
            for j in range(m):
                t = matrix[i][j]
                r = i
                c = j
                matrix[i][j] = matrix[n-1-c][r]
                matrix[n-1-c][r] = matrix[n-1-r][n-1-c]
                matrix[n-1-r][n-1-c] = matrix[c][n-1-r]
                matrix[c][n-1-r] = t
                
                printMatrix(matrix)
            
                
        return matrix
        
        
sol = Solution()

print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))
#print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))