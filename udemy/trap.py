"""
https://leetcode.com/problems/trapping-rain-water/

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

    n == height.length
    0 <= n <= 3 * 104
    0 <= height[i] <= 105
"""

def trap(height):
	print (height)
	total = 0
	left_max = right_max = 0
	left = 0
	right = len(height)-1
	while left < right:
		print ("%s=%s %s=%s" % (left, height[left], right, height[right]))
		if height[left] <= height[right]:
			if height[left] >= left_max:
				left_max = height[left]
			else:
				total += (left_max - height[left])
			left += 1
			print ("left=%s left_max=%s total=%s" % (left, left_max, total))
		else:
			if height[right] >= right_max:
				right_max = height[right]
			else:
				total += (right_max - height[right])
			right -= 1
			print ("right=%s right_max=%s total=%s" % (right, right_max, total))
	return total

"""
# Brute Solution - O(n^2)

def trap(self, height):
        total = 0
        max_r = max_l = 0
        for i in range(1, len(height)-1):
                max_l = max(max_l, height[i-1])
                max_r = max(height[i+1:])
                water = min(max_l, max_r) - height[i]
                if water > 0:
                        total += min(max_l, max_r) - height[i]
        return total
"""
		

#x = [4,2,0,3,2,5]
#x = [4,4,1,2,0,3,2,5]
x = [0,1,0,2,1,0,1,3,2,1,2,1]
print (trap(x))
