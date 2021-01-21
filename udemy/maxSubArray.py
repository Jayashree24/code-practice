"""
https://leetcode.com/problems/maximum-subarray/description/

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [0]
Output: 0

Input: nums = [0]
Output: 0

Input: nums = [-100000]
Output: -100000
"""

def maxSubArray(nums):
	s = -100000000000001
	l = len(nums)
	for i in range(l):
		j = l
		while (j > i):
			x = sum(nums[i:j]) 
			print ("%s=%s sum=%s" % (i, nums[i:j], x))
			if x > s:
				s = x 
			j -= 1
	return s

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#nums = [5,7,8,-1,-3,-3,1,2,4,-9,3,4]
#nums = [-100000]
print (maxSubArray(nums)) 
