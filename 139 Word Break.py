class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        opt = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if len(word) <= i+1:
                    if word == s[i+1-len(word):i+1]:
                        if i+1 == len(word):
                            opt[i] = True
                            break
                        elif opt[i-len(word)] == True:
                            opt[i] = True
                            break
        
        return opt[len(s)-1]
            
        
        """ Time Limit exceeded
        def matchString(sub):
            for word in wordDict:
                if len(word) <= len(sub):
                    if word == sub[:len(word)]:
                        if len(word) == len(sub): return True
                        
                        if matchString(sub[len(word):]) == True: return True
    
        
        if matchString(s) == True: return True
        else: return False
        """
        
sol = Solution()

print(sol.wordBreak("leetcode", ["leet","code"]))