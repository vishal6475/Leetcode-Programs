class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        min_p, max_p = prices[0], prices[0]
        for p in prices[1:]:
            if p < min_p :
                min_p, max_p = p, p
            elif p > max_p:
                max_p = p
                max_profit = max_p - min_p
                
        return max_profit
        
sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4]))