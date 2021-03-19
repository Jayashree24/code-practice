"""
https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0

https://leetcode.com/problems/largest-number/

Largest Number formed from an Array
Medium

Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.The result is going to be very large, hence return the result in the form of a string.

Example 1:

Input: 
N = 5
Arr[] = {3, 30, 34, 5, 9}
Output: 9534330
Explanation: Given numbers are {3, 30, 34,
5, 9}, the arrangement 9534330 gives the
largest value.

Example 2:

Input: 
N = 4
Arr[] = {54, 546, 548, 60}
Output: 6054854654
Explanation: Given numbers are {54, 546,
548, 60}, the arrangement 6054854654 
gives the largest value.
"""
from functools import cmp_to_key 

def cmp_chr(x, y):
	print (x, y, x+y, y+x)
	if x + y > y + x:
		return -1
	elif x + y < y + x:
		return 1
	else:
		return 0

def printLargest(arr):
	#cmp_chr1 = lambda x,y: -1 if x+y > y+x else (1 if x+y < y+x else 0)
	arr.sort(key=cmp_to_key(cmp_chr))
	print (arr)
	return ''.join(arr)

def compare(a, b):
	print (a+b, b+a)
	print ('*********')
	return a + b < b + a

"""
Bubble Sort - O(n^2)
"""
def bubble_sort(arr):
	l = len(arr)
	for i in range(l):
		for j in range(l-1):
			#if arr[j] < arr[j+1]:
			if compare(arr[j], arr[j+1]):
				print (arr[j], arr[j+1])
				arr[j], arr[j+1] = arr[j+1], arr[j]
			#print (arr)
	return ''.join(arr)

"""
Selection Sort - O(n^2)
"""
def selection_sort(arr):
	l = len(arr)
	for i in range(l):
		index = i
		for j in range(i+1, l):
			#if arr[j] > arr[index]:
			if not compare(arr[j], arr[index]):
				index = j
		arr[i], arr[index] = arr[index], arr[i] 
		#print (arr)
	return ''.join(arr)

"""
Insertion Sort - O(n^2)
"""		
def insertion_sort(arr):
	l = len(arr)
	for i in range(l):
		print ("i.%s=%s" % (i, arr[i]))
		for j in range(i, 0, -1):
			print ("j.%s=%s<->%s" % (j, arr[j], arr[j-1]))
			#if arr[j-1] < arr[j]:
			if compare(arr[j-1], arr[j]):
				arr[j-1], arr[j] = arr[j], arr[j-1]
			print (arr)	
		print ('*******')

"""
Merge Sort - O(nlogn)
"""

def merge(l, r):
	i = j = 0
	x = []
	print (l, r)
	while i < len(l) and j < len(r):
		#print (l[i], r[j])
		#if l[i] > r[j]:
		if not compare(l[i], r[j]):
			x.append(l[i])
			i += 1
		else:
			x.append(r[j])
			j += 1
		#print (x, i, j)
	print (l[:i], l[i:], r[:j], r[j:])
	return x + l[i:] + r[j:]

def merge_sort(arr):
	l = len(arr)
	if l == 1:
		return arr
	mid = int(l/2)
	l = arr[:mid]
	r = arr[mid:]
	print ("l=%s r=%s"% (l, r))

	left = merge_sort(l)
	right = merge_sort(r)
	print ("left=%s right=%s" % (left, right))
	x = merge(left, right)
	print ("x = %s" % x)
	return x

"""
Quick Sort - O(nlogn) - TODO
"""			

arr = input().split()
print (arr)
#print (printLargest(arr))
#print (bubble_sort(arr))
#print (selection_sort(arr))
#print (insertion_sort(arr))
print (merge_sort(arr))

