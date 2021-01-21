# Merge two sorted arrays
# x = [0,3,4,31], y = [4,6,30]
# [0,3,4,4,6,30,31]

def merge(x, y):
	print (x)
	print (y)
	len_x = len(x)
	len_y = len(y)
	arr = [0] * (len_x + len_y)
	i = j = k = 0
	while i < len_x or j < len_y:
		if j >= len_y:
			arr[k:] = x[i:] 
			break
		if i >= len_x:
			arr[k:] = y[j:]
			break
		print ("[%s] %s=%s, %s=%s" % (k, i, x[i], j, y[j]))
		if x[i] < y[j]:
			arr[k] = x[i]
			i += 1
		elif x[i] > y[j]:
			arr[k] = y[j]
			j += 1
		else:
			arr[k] = x[i]
			k += 1
			arr[k] = y[j]
			i += 1
			j += 1
		k += 1
		print (arr)
	return arr

x = [0,3,4,31,33,90]
y = [4,6,30,32]
print (merge(x, y))
			

