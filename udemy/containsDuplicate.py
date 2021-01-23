"""
https://leetcode.com/problems/contains-duplicate/

Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

"""
def containsDuplicate(nums):
	count_elem = {}
	for i in nums:
		count_elem[i] = count_elem.get(i, 0) + 1
		if count_elem[i] > 1:
			print (count_elem)
			return True
	print (count_elem)
	return False

nums = [1,2,3,1]
nums = [3,1]
nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,4]
print (containsDuplicate(nums))

