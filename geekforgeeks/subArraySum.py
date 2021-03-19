"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

Subarray with given sum
Easy 

Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

 

Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.

"""
def subArraySum(arr, n, s):
	i = j = slide_sum = 0
	for i in range(n):
		print ("i.%s=%s slide_sum=%s" % (i, arr[i], slide_sum))
		while slide_sum < s and j < n:
			slide_sum += arr[j]
			print ("%s=%s slide_sum=%s" % (j, arr[j], slide_sum))
			j += 1
		if slide_sum == s:
			print ('Sum is equal')
			print (i, j)
		slide_sum -= arr[i]

"""
This is done by hashing technique
d = {}
d[0] = -1

def subArraySum(arr, n, s):
	sm = 0
	for i in range(n):
		sm += arr[i]
		print (sm, sm-s)
		if (sm - s) in d:
			print ('I am returning for %s' % (sm-s))
			print (d[sm-s]+1, i)
			#return (d[sm-s]+1, i)
		d[sm] = i
		print (d)
"""

arr = list(map(int, input().split()))
s = int(input())
n = len(arr)
print (subArraySum(arr, n, s)) 
