#import functools

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        #intervals = sorted(intervals, key=functools.cmp_to_key(lambda x, y: x[0]-y[0]))
        intervals = sorted(intervals, key= lambda x: x[0])
        
        output = [intervals[0]]
        for start, end in intervals:
            if end <= output[-1][1]:
                continue
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        
        return output
        
sol = Solution()

print(sol.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))