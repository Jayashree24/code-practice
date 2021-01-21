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
	while i < len_x and j < len_y:
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
	arr[k:] = x[i:] + y[j:]
	return arr

x = [0,3,4,31,32]
y = [4,6,30,90,101]
print (merge(x, y))

