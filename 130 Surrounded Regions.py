class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        r = len(board)
        c = len(board[0])
        print(r, c)
        print(board)
        
        for i in range(r):
            for j in range(c):
                print(board[i][j])
        
sol = Solution()

print(sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))