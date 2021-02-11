"""
[1,2,-1,3,4,10,10,-10,-1]
sum = 29
"""

def large_sum_array(s):
	max_sum = final_sum = 0
	for i in s:
		max_sum += i
		#print ("i=%s max_sum=%s" % (i, max_sum))
		max_sum = max(max_sum, i)
		final_sum = max(final_sum, max_sum)
		#print ("AFTER max_sum=%s final_sum=%s" % (max_sum, final_sum))
	return final_sum


s = [1, 2, -1, 3, 4, 10, 10, -10, -1]
s = [1, 2, -2, 3, 4, 10, 10, -10, -1]
s = [1, 2, -3, 3, 4, 10, 10, -10, -1]
s = [1, 2, -4, 3, 4, 10, 10, -10, -1]
s = [-2, 6, -4, 2, -9]
s = [-2, -3, 4, -1, -2, 1, 5, -3]
print (large_sum_array(s))

