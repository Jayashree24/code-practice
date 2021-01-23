"""
def moveZeroes(nums):
	print (nums)
	orig_i = -1 
	d = 0
	for i in range(len(nums)):
		print ("%s=%s" % (i, nums[i]))
		if nums[i] != 0:
			d = i - orig_i
			nums[orig_i+1] = nums[i]
			print (d, nums[orig_i+2:i+1])
			nums[orig_i+2:i+1] = [0] * (d-1)
			orig_i = orig_i+1 
			print (nums)
"""
def moveZeroes(nums):
	j = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[j], nums[i] = nums[i], nums[j]
			j += 1
	print (nums)


#nums = [1, 0,0,1,0,0]
nums = [0, 0, 0, 0, 0, 1, 0, 3, 12, 0, 1, 0]
#nums = [1, 0, 1, 0, -1, 0, 3, 12, 0, 1, 0]
moveZeroes(nums)


