# This algorithm is based on the idea of repeatedly comparing pairs of adjacent elements and then switching their positions if they exist in the wrong order
# Complexity - O(n2)

def bubble(arr):
	n = len(arr)
	print ('n : %s' % n)
	for j in range(n-1):
		print ('j : %s' % (j))
		# Last element always be the greatest number. 
		for i in range(n-1-j):
			print ('%s= (%s %s)' % (i, arr[i], arr[i+1]))  
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
			print (arr)
		print ('**********')

arr = [64, 34, 25, 12, 22, 11, 90]
arr = [7, 4, 5, 2]
bubble(arr)
