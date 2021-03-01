"""
Implementing Bubble Sort Algorithm
"""

def bubble_sort(arr):
	print (arr)
	loop = len(arr)
	while loop:
		print ("loop = %s" % (loop))
		for i in range(0, loop-1): 	
			print (arr[i], arr[i+1])
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]

		loop -= 1

		print (arr)

arr = [12,8,9,1,4,3,0,10,9]
arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubble_sort(arr)
