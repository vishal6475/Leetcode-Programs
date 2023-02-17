class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        all = []
        
        def matchString(sub, sent):
            for word in wordDict:
                if len(word) <= len(sub):
                    if word == sub[:len(word)]:
                        if len(word) == len(sub): 
                            all.append((sent + ' ' + word).lstrip())
                        else:
                            matchString(sub[len(word):], sent + ' ' + word)
    
        matchString(s, "")
        
        return all
        
sol = Solution()

print(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))