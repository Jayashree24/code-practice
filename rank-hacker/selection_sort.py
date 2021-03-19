# Complexity - O(n2)

def sel_sort(m):
	n = len(m)
	print (m)
	for i in range(n):
		min = i
		# First element will be the smallest one
		for j in range(i+1, n):
			if m[j] < m[min]:
				min = j
		print ('min : %s (%s %s)' % (min, m[i], m[min]))
		if min != i:
			m[i], m[min] = m[min], m[i]
			print (m)
 
arr = [7, 5, 4, 2]
arr = [64, 25, 12, 22, 11]
sel_sort(arr)
