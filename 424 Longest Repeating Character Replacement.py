class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counts = dict()
        l = 0
        counts[s[l]] = 1
        maxx = 1
            
        for r in range(1, len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxx = max(maxx, counts[s[r]])
                    
            if ((r-l+1) - maxx) > k:
                counts[s[l]] -= 1
                l += 1
        
        return min(maxx+k, len(s))
        
sol = Solution()

print(sol.characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))