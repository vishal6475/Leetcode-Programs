
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        
        area = (right-left) * min(height[left], height[right])
        
        while left < right:
            if height[left] <= height[right]:
                left += 1
                area = max(area, ((right-left) * min(height[left], height[right])))
            
            elif height[left] > height[right]:
                right -= 1
                area = max(area, ((right-left) * min(height[left], height[right])))
                
        
        return area

sol = Solution()

print(sol.maxArea([2,3,4,5,18,17,6]))
