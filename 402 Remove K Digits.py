class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        
        stack = [num[0]]
        
        for n in num[1:]:
            while stack and n < stack[-1] and k:
                stack.pop(-1)
                k -= 1                
            stack.append(n)
            
        while k > 0:
            stack.pop(-1)
            k -= 1   

        while stack[0] == '0' and len(stack) > 1:
            stack.pop(0)
            k -= 1                     
            
        return "".join(stack)
            
        
sol = Solution()

print(sol.removeKdigits("10200", 1))