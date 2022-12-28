
class KnightVsKing(object):

    def __init__(self):
        """
        :type capacity: int
        """        
        self.checked = [[0 for _ in range(8)] for _ in range(8)]
        self.DFS = list()
                
        
    def printCheck(self):
        for i in range(len(self.checked)):
            print(self.checked[i])
            print()
        
        
    def updateBishopCells(self, x, y):
        self.checked[x][y] = 5
                
        for d in range(1, 8):
            if x - d >=0 and y - d >=0:
                self.checked[x-d][y-d] = 5
            if x + d <=7 and y - d >=0:
                self.checked[x+d][y-d] = 5
            if x - d >=0 and y + d <=7:
                self.checked[x-d][y+d] = 5
            if x + d <=7 and y + d <=7:
                self.checked[x+d][y+d] = 5
        
        
    def getPossibleMoves(self, x, y, turn):
        
        moves = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, -1), (2, 1)]
        
        for (dx, dy) in moves:
            if x + dx >=0 and x + dx < 8 and y + dy >=0 and y + dy < 8 and self.checked[x+dx][y+dy] == 0:
                self.DFS.append([(x+dx, y+dy), turn])
                self.checked[x+dx][y+dy] = 1
        

    def minMoveCheckmate(self, king, bishop, knight):        
        
        self.updateBishopCells(bishop[0], bishop[1])
        self.checked[knight[0]][knight[1]] = 2        
        
        self.printCheck()
        
        turn = 0
        self.DFS.append([(knight[0], knight[1]), turn])
        
        while(True):
            if len(self.DFS) == 0: return 'Not Possible'
            
            cur = self.DFS.pop(0)
            if cur[0][0] == king[0] and cur[0][1] == king[1]:
                return cur[1]          
        
            self.getPossibleMoves(cur[0][0], cur[0][1], cur[1]+1)            
        

obj = KnightVsKing()

print('Minimum moves is-', obj.minMoveCheckmate((1, 2), (4, 4), (7, 4)))

