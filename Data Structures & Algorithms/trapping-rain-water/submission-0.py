class Solution:
    def trap(self, height: List[int]) -> int:
                # so let's try to find the boundary/bottle-neck which will
        # tell us the amount of water we can hold,
        # if idx = 3 and leftmax = 3 and rmax = 5 
        # it'd b min(lmax,rmax) - h[i] why h[i? because we're 
        # seperating the terrain height at idx i to get amout of water held at that
        # point
        n = len(height)
        # leftMax = [0]*n
        # rightMax = [0]*n
        # leftMax[0]=height[0]
        # for i in range(1, n):
        #     leftMax[i] = max(leftMax[i-1], height[i])
        # rightMax[n-1] = height[n-1]
        # for i in range(n-2, -1, -1):
        #     rightMax[i] = max(rightMax[i+1], height[i])
        # trappedWater = 0
        # for i in range(n):
        #     trappedWater+=min(leftMax[i], rightMax[i]) - height[i]
        # return trappedWater
        leftMax, rightMax, l, r = 0, 0, 0, n-1
        trappedWater = 0
        while l < r:
            if height[l] < height[r]:
                leftMax = max(leftMax, height[l])
                trappedWater += leftMax - height[l]
                l+=1
            else:
                rightMax = max(rightMax, height[r])
                trappedWater += rightMax - height[r]
                r-=1
        return trappedWater