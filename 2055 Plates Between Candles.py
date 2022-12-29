class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        candles = []
        answers = []
        
        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)
        print('candles', candles)
                
        if len(candles) < 2:
            return [0 for _ in range(len(queries))]
                
        for q in queries:
            print(q[0], q[1])
            
            if q[0] == q[1]:
                answers.append(0)
                continue
            
            first, last = -1, -1
            low, high = 0, len(candles) - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if candles[mid] == q[0]:
                    first = mid
                    break
                
                if mid == 0:
                    if candles[mid] > q[0] and candles[mid] <= q[1]:
                        first = mid
                        break
                
                if candles[mid] > q[0] and candles[mid] <= q[1] and candles[mid-1] < q[0]:
                    first = mid
                    break                
                
                if candles[mid] < q[0]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            if first != -1:
                low, high = 0, len(candles) - 1
                
                while low <= high:
                    mid = (low + high) // 2
                    
                    if candles[mid] == q[1]:
                        last = mid
                        break
                    
                    if mid == 0:
                        last = first
                        break
                    
                    if mid == len(candles) - 1:                        
                        if candles[mid] >= q[0] and candles[mid] < q[1]:
                            last = mid
                            break                                              
                    
                    if candles[mid] >= q[0] and candles[mid] < q[1] and candles[mid+1] > q[1]:
                        last = mid
                        break                    
                    
                    if candles[mid] > q[1]:
                        high = mid - 1
                    else:
                        low = mid + 1
                        
            print('First:', first, candles[first])
            print('Last:', last, candles[last])
            print(answers)
            
            if first == last:
                answers.append(0)
            else:
                count = candles[last] - candles[first] - (last - first)
                answers.append(count)
                
        print('Final:')
        return answers
        
        
sol = Solution()

print(sol.platesBetweenCandles("**|**|***|*", [[2,5],[5,9],[4,8],[0,1],[9,10]]))