"""
https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/

"""

def revstack(arr):
	print ('arr=%s' % arr)
	if len(arr) == 1:
		return
	x = arr.pop()
	print ('x=%s' % x)
	revstack(arr)
	print ('after arr=%s' % arr)
	insert(arr, x)

def insert(arr, x):
	print ('ar=%s x=%s'% (arr, x))
	if len(arr) == 0:
		arr.append(x)
		return
	y = arr.pop()
	insert(arr, x)
	arr.append(y)

arr = [1,8,2,6,9]
revstack(arr)
print (arr)
