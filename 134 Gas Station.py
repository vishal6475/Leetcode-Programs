

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        start = -1
        i = 0
        total = 0
        looped = 0
        while True:
            if i == start: return start
            
            if total + gas[i] >= cost[i]:
                if start == -1: start = i
                total += gas[i] - cost[i]
            else:
                start = -1
                total = 0
                
                
            i += 1
            if i == len(gas):
                i = 0
                looped += 1
                if looped == 2:
                    return -1
                
            
        
sol = Solution()

print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))