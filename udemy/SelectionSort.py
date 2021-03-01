"""
Implement Selection Sort
"""

def selection_sort(arr):
	l = len(arr)
	print (arr)
	for i in range(l):
		#print ("******%s=%s*****" % (i, arr[i]))
		index = i
		for j in range(i+1, l):
			#print ("%s, %s" % (arr[j], arr[index]))
			if arr[j] < arr[index]:
				index = j

		#print ("indy %s=%s" % (arr[i], arr[index]))
		arr[i], arr[index] = arr[index], arr[i]
	print (arr)
				
arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selection_sort(arr)	
