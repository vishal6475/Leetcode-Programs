class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        # method: stack
        lastLocs = {}
        
        for i, c in enumerate(s):
            lastLocs[c] = i            
        
        res = [s[0]] 
        for i, c in enumerate(s[1:]):
            if c not in res:
                while len(res) > 0 and c < res[-1] and lastLocs[res[-1]] > i:
                    res.pop(-1)
                res.append(c)
                
        return "".join(res)
        """
            
        
         
        # method: greedy selection
        chars = sorted(list(set(s)))
        n = len(chars)
        lastLocs = {}
        locs = {}
        for c in chars:
            locs[c] = []
        
        for i, c in enumerate(s):
            lastLocs[c] = i
            locs[c].append(i)            
        
        inverse = sorted(list(lastLocs.values()))
        
        res = ""   
        cur = -1
        for i in range(n):
            for c in chars:
                #print(i, c, locs[c][0], lastLocs, inverse, locs)
                locs[c] = list(filter(lambda x: x>cur, locs[c]))
                if locs[c][0] <= inverse[0]:
                    cur = locs[c][0]
                    res += c
                    chars.remove(c)
                    inverse.remove(lastLocs[c])
                    del locs[c]
                    del lastLocs[c]
                    break
                
        return res
        
        
sol = Solution()

print(sol.removeDuplicateLetters('cbacdcbc'))