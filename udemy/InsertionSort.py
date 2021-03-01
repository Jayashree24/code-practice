"""
Implement Insertion Sorting Algorithm
"""

def insertion_sort(a):
	l = len(a)
	print (a)
	for i in range(l-1):
		#print ('********%s********' % i)
		for j in range(i, -1, -1):
			#print (a[j], a[j+1])
			if a[j+1] < a[j]:
				a[j], a[j+1] = a[j+1], a[j]
			else:
				break
			#print (a)
	print (a)

a = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
a = [1,2,3,4,10,8]
insertion_sort(a)
