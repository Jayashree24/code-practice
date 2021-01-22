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
	sum = m = nums[0] 
	for i in range(1, len(nums)):
		print (sum+nums[i], nums[i])	
		sum = max(sum+nums[i], nums[i])
		m = max(m, sum)
	return m
		
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#nums = [5,7,8,-1,-3,-3,1,2,4,-9,3,4]
#nums = [-100000]
print (maxSubArray(nums)) 
