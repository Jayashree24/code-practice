# https://leetcode.com/problems/two-sum/description/

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

def twoSum(nums, target):
	print (nums)
	sum_map = {}
	for i in range(len(nums)):
		dif = target - nums[i]
		print ("[%s] %s=%s" % (i,nums[i], dif))
		comp_nums_i = sum_map.get(nums[i], None)
		print ('comp_nums_i=%s' % (comp_nums_i))
		if comp_nums_i is None:
			sum_map[dif] = i
			print (sum_map)
		else:
			return [comp_nums_i, i]
	return []

nums = [2,7,11,15]
nums = [3,2,4]
nums = [3,3]
target = 9
target = 6
print (twoSum(nums, target))
			
