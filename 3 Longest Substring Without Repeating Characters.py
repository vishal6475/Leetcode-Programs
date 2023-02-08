class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        sub = dict()
        sub[s[0]] = 0
        
        i, j, length = 0, 1, 1
        
        for j in range(1, len(s)):
            if s[j] in sub and sub[s[j]] >= i:
                length = max(length, j-i)                   
                i = sub[s[j]]+1
                #print(i, j, sub)
                
            sub[s[j]] = j    
            
        length = max(length, j-i+1)        
        
        return length
        """
        if len(s) == 0:
            return 0
        
        sub = set(s[0])
        
        i, j, length = 0, 1, 1
        
        while j < len(s):
            if s[j] in sub:
                length = max(length, j-i)
                while s[i] != s[j]:
                    sub.remove(s[i])
                    i += 1
                sub.remove(s[i])
                i += 1
                #print(i, j, sub)
                
            sub.add(s[j])  
            j+=1
            
        length = max(length, j-i)        
        
        return length
        """
        
sol = Solution()

print(sol.lengthOfLongestSubstring("aab"))