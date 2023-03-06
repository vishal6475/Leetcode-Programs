class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        m = len(s)
        f = [0] * m
            
        j, ln = 1, 0
            
        while j < m:
            if s[j] == s[ln]:
                ln += 1
                f[j] = ln
                j += 1
            elif ln > 0:
                ln = f[ln-1]
            else:
                f[j] = 0
                j += 1            
        return s[:f[-1]]
        
sol = Solution()

print(sol.longestPrefix("level"))