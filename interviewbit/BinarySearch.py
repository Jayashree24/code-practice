"""
Implement Binary Search

https://www.interviewbit.com/courses/programming/topics/binary-search/

"""

def binary_search(arr, target):
	start = 0
	end = len(arr) - 1 
	l = len(arr)
	mid = int(l/2) + start
	#while l >= 1:
	while start <= end:
		#mid = int(l/2) + start
		mid = int((start+end)/2)
		#print ("MID len=%s arr[%s]=%s" % (l, mid, arr[mid])) 
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			end = mid-1
			#l = (end - start) + 1
			#mid = int(l/2) + start
			#print ('BIG start=%s end=%s' % (start, end))
			#print ('arr=%s len=%s' % (arr[start:end+1], l))
		elif arr[mid] < target:
			start = mid+1
			#l = (end - start) + 1
			#mid = int(l/2) + start
			#print ('SMALL start=%s end=%s' % (start, end))
			#print ('arr=%s len=%s' % (arr[start:end+1], l))
	return -1

arr = list(map(int, input().split()))
target = int(input())
print (binary_search(arr, target))
		
