class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volumn = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not len(stack):
                    break
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volumn += distance * waters
            stack.append(i)
        return volumn
    
#너무 어려움... 이해 X 180pg
#https://leetcode.com/problems/trapping-rain-water/
