class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
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
            
        #print(chars, lastLocs, inverse, locs)
        
        res = ""   
        cur = -1
        for i in range(n):
            for c in chars:
                #print(i, c, locs[c][0], lastLocs, inverse, locs)
                while locs[c][0] <= cur:
                    locs[c].pop(0)
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