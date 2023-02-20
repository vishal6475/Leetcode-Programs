class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        out = dict()
        
        for st in strs:
            freq = [0] * 26
            for c in st:
                freq[ord(c) - ord('a')] += 1
                
            t = tuple(freq)
            
            if t in out:
                out[t].append(st)
            else:
                out[t] = [st]
                
        return out.values()
            
        
sol = Solution()

print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))