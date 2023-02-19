class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        minLen = 200
        prefix = ""
        for st in strs:
            if len(st) < minLen:
                minLen = len(st)
                prefix = st
                
        for st in strs:
            for i in range(len(prefix)):
                if st[i] != prefix[i]:
                    if i == 0: return ""
                    prefix = prefix[:i]
                    break
                
        
        return prefix
                
        print(prefix, minLen)
        
sol = Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))