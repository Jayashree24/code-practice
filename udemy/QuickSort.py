"""
Implement Quick Sorting Algorithm
# Divide and Conquer Algorithm
1st loop
========
[5,3,1,6,4,2] pivot = 2
 i,j
[5,3,1,6,4,2]
 i,j
[5,3,1,6,4,2]
 i,  j
[1,3,5,6,4,2]
   i   j
[1,3,5,6,4,2]
   i     j
[1,3,5,6,4,2]
   i       j
# Exchange i and j
[1,2,5,6,4,3]
2nd loop
========
[1] & [5,6,4,3] pivot = 3
       i,j
[3,6,4,5] 

3rd loop
========
[6,4,5] pivot = 5
 i,j
[4,6,5]
   i,j
[4,5,6]
"""

def partition(arr, start, end):
	print ("arr=%s" % arr)
	pivot = end
	print ("start: arr[%s]=%s end: arr[%s]=%s pivot=%s" % (start, arr[start], end, arr[end], arr[pivot]))
	i = start 
	for j in range(start, end+1):
		if arr[j] < arr[pivot]:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
		print (arr)
	print (i, pivot)
	arr[i], arr[pivot] = arr[pivot], arr[i]
	print (arr)
	return i

def quick_sort(arr, start, end):
	if end <= start:
		print ('I am returning for %s' % arr)
		print ("return start=%s end=%s" % (start, end))
		return
	print ('quick_sort start: arr[%s]=%s end: arr[%s]=%s' % (start, arr[start], end, arr[end]))
	pos = partition(arr, start, end)
	print ('quick_sort pos=%s' % (pos))
	quick_sort(arr, start, pos-1)
	quick_sort(arr, pos+1, end)

arr = [99, 44, 6, 2, 1, 5, 2, 63, 87, 283, 4, 0]
arr = [7,-2,4,1,6,5,0,-4,2]
quick_sort(arr, 0, len(arr)-1)


	
	
