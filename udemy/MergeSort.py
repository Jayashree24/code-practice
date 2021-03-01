"""
Implement Merge Sort Algorithm
"""

def merge(left, right):
	#print ("merged left=%s right=%s" % (left, right))
	#print ("len of left=%s len of right=%s" % (len(left), len(right)))
	x = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			x += [left[i]]
			i += 1
		elif left[i] > right[j]:
			x += [right[j]]
			j += 1
		else:
			#print ('JAI')
			x += [left[i], right[j]]
			i += 1
			j += 1
	#print (left[i:],  right[j:])
	x += (left[i:] + right[j:]) 
	#print ("merged returns = %s" % x)
	return x
	
def merge_sort(arr):
	#print (arr)
	if len(arr) == 1:
		return arr
	mid = int(len(arr)/2)
	left = arr[:mid]
	right = arr[mid:]
	left_sort = merge_sort(left)
	right_sort = merge_sort(right)
	merged = merge(left_sort, right_sort)
	#print ("after merged = %s" % merged)
	#print ("left=%s right=%s merged=%s" % (left_sort, right_sort, merged))
	return merged


arr = [99, 44, 6, 2, 1, 5, 2, 63, 87, 283, 4, 0]
print (arr)
print (merge_sort(arr))
