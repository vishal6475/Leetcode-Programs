class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # Knuth Morris Pratt Algorithm        
        def getPrefix(P, m):
            f = [0] * m
            
            j, ln = 1, 0
            
            while j < m:
                if P[j] == P[ln]:
                    ln += 1
                    f[j] = ln
                    j += 1
                elif ln > 0:
                    ln = f[ln-1]
                else:
                    f[j] = 0
                    j += 1            
            return f
        
        
        n, m = len(haystack), len(needle)
        f = getPrefix(needle, m)
        
        i, j = 0, 0
        while i < n:
            if haystack[i] == needle[j]:
                if j == m-1:
                    return i-j
                else:
                    i += 1
                    j += 1
            else:
                if j>0:
                    j = f[j-1]
                else:
                    i += 1
                    
        return -1
        
        
        """
        # Boyer Moore Algorithm- method 1
        last = {}
        
        for i, c in enumerate(needle):
            last[c] = i
            
        l = len(needle)
        
        i, j = l - 1, l - 1
        
        while i < len(haystack):
            print('Start', i, j, haystack[i], needle[j])
            if haystack[i] == needle[j]:
                if j == 0: return i
                i -= 1
                j -= 1
            else:
                i += l - min(j, 1 + last.get(haystack[i], -1))
                j = l-1
                
        return -1
        """
        
        
        """
        # Boyer Moore Algorithm- method 2
        last = {}
        
        for i, c in enumerate(needle):
            last[c] = i
        
        i, j = len(needle) - 1, len(needle) - 1
        
        while i < len(haystack):
            print('Start', i, j, haystack[i], needle[j])
            if haystack[i] == needle[j]:
                org = i
                if j == 0: return i
                i -= 1
                j -= 1
                print(i, j, haystack[i], needle[j])
                while haystack[i] == needle[j]:
                    if j == 0: return i
                    i -= 1
                    j -= 1
                j = len(needle) - 1
                i = org + len(needle) - last.get(haystack[org], -1) - 1
                if i == org: i+=1
            else:
                i += len(needle) - last.get(haystack[i], -1) - 1
                
        return -1
        """
        
sol = Solution()

print(sol.strStr("ababbbbaaabbbaaa", "bbbb"))