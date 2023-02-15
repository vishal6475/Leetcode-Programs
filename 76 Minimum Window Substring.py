class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = len(s)
        lt = len(t)
        if lt > ls: return ""
        minWindow = s
        winLength = ls+1
        sDic = dict()
        tDic = dict()
        tchars = set(t)
        
        for i in range(lt):
            sDic[s[i]] = 1 + sDic.get(s[i], 0)
            tDic[t[i]] = 1 + tDic.get(t[i], 0)
        if sDic == tDic: return s[:lt]
        
        left = 0
        
        def doesContains(bigDic, smallDic):
            for key in smallDic.keys():
                if smallDic[key] > bigDic.get(key, 0):
                    return False
            return True
        
        for i in range(lt, ls):
            sDic[s[i]] = 1 + sDic.get(s[i], 0)
            if s[i] in tchars or i == ls-1:
                if doesContains(sDic, tDic):            
                    if i-left+1 < winLength:
                        winLength = i-left+1
                        minWindow = s[left:i+1]
                        
                    moveLeft = True
                        
                    while moveLeft:
                        sDic[s[left]] -= 1
                        left += 1
                        
                        if s[left-1] in tchars:
                            moveLeft = doesContains(sDic, tDic)
                            if moveLeft:
                                if i-left+1 < winLength:
                                    winLength = i-left+1
                                    minWindow = s[left:i+1]
                        else:
                            if i-left+1 < winLength:
                                winLength = i-left+1
                                minWindow = s[left:i+1]
                            
                        
                        if left == i: moveLeft = False
                        

        return "" if winLength == ls+1 else minWindow

sol = Solution()

print(sol.minWindow("ADOBECODEBANC", "ABC"))