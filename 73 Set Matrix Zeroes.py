
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        col_1 = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if j != 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    else:
                        col_1 = 0
                        matrix[i][0] = 0
                    
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0: matrix[i] = [0 for j in range(len(matrix[0]))]
            
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0: matrix[0] = [0 for j in range(len(matrix[0]))]
        
        if col_1 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

sol = Solution()

print(sol.setZeroes([[1,2,0,4],[5,0,7,8],[3,10,11,12],[13,14,15,0]]))