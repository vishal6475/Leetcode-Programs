class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        r = len(board)
        c = len(board[0])    
        
        to_check = []
        
        for i in range(r):
            if board[i][0] == 'O': 
                to_check.append([i, 0])
                board[i][0] = '1'
            if board[i][c-1] == 'O': 
                to_check.append([i, c-1])                
                board[i][c-1] = '1'
        
        for j in range(1, c-1):
            if board[0][j] == 'O': 
                to_check.append([0, j])                
                board[0][j] = '1'
            if board[r-1][j] == 'O': 
                to_check.append([r-1, j])            
                board[r-1][j] = '1'
        
        while(len(to_check) > 0):
            item = to_check.pop()
            board[item[0]][item[1]] = '1'
            
            if item[1] - 1 >= 0:
                if board[item[0]][item[1] - 1] == 'O':
                    to_check.append([item[0], item[1] - 1]) 
                    board[item[0]][item[1]-1] = '1'
            
            if item[1] + 1 < c:
                if board[item[0]][item[1] + 1] == 'O':
                    to_check.append([item[0], item[1] + 1]) 
                    board[item[0]][item[1]+1] = '1'
            
            if item[0] - 1 >= 0:
                if board[item[0] - 1][item[1]] == 'O':
                    to_check.append([item[0] - 1, item[1]]) 
                    board[item[0]-1][item[1]] = '1'
            
            if item[0] + 1 < r:
                if board[item[0] + 1][item[1]] == 'O':
                    to_check.append([item[0] + 1, item[1]]) 
                    board[item[0]+1][item[1]] = '1'                   
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'               
                    
        return board
        
sol = Solution()

print(sol.solve([["O","O","O"],["O","O","O"],["O","O","O"]]))