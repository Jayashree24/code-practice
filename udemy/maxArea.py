"""
https://leetcode.com/problems/container-with-most-water/

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Input: height = [4,3,2,1,4]
Output: 16

Input: height = [1,2,1]
Output: 2

Constraints:

    n == height.length
    2 <= n <= 3 * 104
    0 <= height[i] <= 3 * 104
"""

# O(n^2)
# O(1)
# Increase space complexity to get the time complexity down.

"""
def maxArea(height):
	print (height)
	l = len(height)
	area = 0
	for i in range(l):
		for j in range(i+1, l):
			a = min(height[i], height[j]) * (j - i)
			print ("%s=%s %s=%s a=%s" % (i, height[i], j, height[j], a))
			area = max(area, a)
	print ('Area : %s' % area)
"""
def maxArea(height):
	print (height)
	l = len(height) - 1
	area = 0
	i = 0
	j = l 
	while i < j:
		print ("%s=%s %s=%s" % (i, height[i], j, height[j]))
		length = min(height[i], height[j])
		width = j - i
		print ("length=%s width=%s AREA=%s" % (length, width, length * width))
		area = max(area, length * width)
		if height[i] < height[j]:
			i += 1
		else:
			j -= 1
	return area

#x = [1,8,6,2,5,4,8,3,7]
x = [1,8,6,2,5,4,8,3]
x = [1,1]
x = [4,3,2,1,4]
x = [1,2,1]
x = [1,8,6,2,10,4,8,3,7]
#x = [4,10,1]
#x = [4,10,12]
#x = [1,2,4,3]
#x = [1,2,6,8,4,9]
#x = [1,2,6,8,9,4]
print (maxArea(x))        
