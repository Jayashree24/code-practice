"""
https://www.geeksforgeeks.org/maximize-pair-decrements-required-to-reduce-all-array-elements-except-one-to-0/

Maximize pair decrements required to reduce all array elements except one to 0

Given an array arr[] consisting of N distinct elements, the task is to find the maximum number of pairs required to be decreased by 1 in each step, such that N – 1 array elements are reduced to 0 and the remaining array element is a non-negative integer.

Examples:

    Input: arr[] = {1, 2, 3}
    Output: 3
    Explanation: 
    Decrease arr[1] and arr[2] by 1 modifies arr[] = {1, 1, 2} 
    Decrease arr[1] and arr[2] by 1 modifies arr[] = {1, 0, 1} 
    Decrease arr[0] and arr[2] by 1 modifies arr[] = {0, 0, 0} 
    Therefore, the maximum number of decrements required is 3.
     

    Input: arr[] = {1, 2, 3, 4, 5}
    Output: 7
"""

def cntMaxOperationToMakeN_1_0(arr):
	cnt = 0
	arr = sorted(arr)
	while len(arr) > 1 :
		print ('********')
		print (arr)
		x = arr[-1]
		y = arr[-2]
		print (y, x)
		arr.pop()
		arr.pop()
		if y - 1 > 0:
			arr.append(y-1)
		if x - 1 > 0:
			arr.append(x-1)
		cnt += 1
		arr = sorted(arr)
	return cnt

arr = [1,2,3]
arr = [1,2,3,4,5]
arr = [5,4,3,2,1]
arr = [5,1,4,2,3]
arr = [1,1]
print (cntMaxOperationToMakeN_1_0(arr))
