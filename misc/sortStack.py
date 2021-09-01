"""
https://www.geeksforgeeks.org/sort-a-stack-using-recursion/

"""

def insert(x, n):
	print ('x=%s n=%s' % (x, n))
	if not x or (x and n >= x[-1]):
		print ('** x=%s n=%s **' % (x,n))
		x.append(n)
		return
	y = x.pop()
	print ('y=%s' % y)
	insert(x, n)
	x.append(y)
	print ('after x=%s' % x)

def sortstack(arr):
	x = []
	while arr:
		n = arr.pop()
		insert(x, n)
	print(x)

arr = [10,4,2,1,9,5,3]
sortstack(arr)
