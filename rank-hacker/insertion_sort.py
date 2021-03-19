# Complexity of Insertion sort is O(n2)
#

def insertion_sort(arr):
	n = len(arr)
	for i in range(n):
		key = arr[i]
		print ('*i* %s=%s' % (i, arr[i]))
		j = i - 1
		print ('*j* %s=%s' % (j, arr[j]))
		prev = i
		while j >=0 and key < arr[j]:
			print ('%s <---> %s' % (arr[prev], arr[j]))
			arr[prev], arr[j] = arr[j], arr[prev]
			prev = j
			key = arr[j]
			j -= 1
			print (arr)

arr = [7, 4, 5, 2]		
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
	
