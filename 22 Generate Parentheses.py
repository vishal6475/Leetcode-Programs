class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        allCombs = {"(": [1, 1]} # 1st: opening parenthesis, 2nd: closed parenthesis allowed
        
        for i in range((n*2)-1):
            newAllComb = {}
            for comb in allCombs:
                if allCombs[comb][1] >= 0 and allCombs[comb][0] < n:
                    newAllComb[comb+'('] = [allCombs[comb][0]+1, allCombs[comb][1]+1]
                    
                if allCombs[comb][1] > 0:
                    newAllComb[comb+')'] = [allCombs[comb][0], allCombs[comb][1]-1]                
                
            allCombs = newAllComb
                
            
        return list(allCombs.keys())


sol = Solution()

print(sol.generateParenthesis(4))