"""
https://www.geeksforgeeks.org/delete-middle-element-stack/

"""

def delstack(arr, k):
	print ('arr=%s k=%s' % (arr, k))
	if k == 1:
		arr.pop()
		return
	x = arr.pop()
	print ('x = %s' % x)
	delstack(arr, k-1)
	print ('after arr = %s' % arr)
	arr.append(x)

arr = [1,4,5,6,7,8]
k = int(len(arr)/2)
delstack(arr, k)
print ('FINAL = %s' % arr)
	
	
