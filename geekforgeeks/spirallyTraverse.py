"""
https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

https://leetcode.com/problems/spiral-matrix/

Given a matrix of size R*C. Traverse the matrix in spiral form.
Medium

Example 1:

Input:
R = 4, C = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Input:
R = 3, C = 4  
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12}}
Output: 
1 2 3 4 8 12 11 10 9 5 6 7
Explanation:
Applying same technique as shown above, 
output for the 2nd testcase will be 
1 2 3 4 8 12 11 10 9 5 6 7.
"""

def spirallyTraverse(matrix, c, r): 
	x = []
	j = 0
	cc = c
	rr = r
	cnt = i = 0
	while c > 0 and r > 0:
		print ("c=%s r=%s i = %s" % (c, r, i))
		while cnt < c:
			x.append(matrix[i])
			i += 1
			cnt += 1
		cnt = 0
		i -= 1
		print ('after 1st loop i=%s' % i)
		print ('after 1st loop x=%s' % x)
		print ('***********************')

		if r-1 <= 0:
                        break
		i = (i + cc) 
		while cnt < r-1:
			print (i)
			x.append(matrix[i])
			i += cc 
			cnt += 1
		cnt = 0
		i -= cc
		print ('after 2nd loop i=%s' % i)
		print ('after 2nd loop x=%s' % x)
		print ('***********************')

		i = i - 1
		while cnt < (c - 1):
			print (i)
			x.append(matrix[i])
			i -= 1
			cnt += 1
		cnt = 0
		i += 1
		print ('after 3rd loop i=%s' % i)
		print ('after 3rd loop x=%s' % x)
		print ('***********************')

		i -= cc
		while cnt < (r-2):
			print (i)
			x.append(matrix[i])
			i -= cc
			cnt += 1
		cnt = 0
		i += cc
		print ('after 4th loop i=%s' % i)
		print ('after 4th loop x=%s' % x)
		print ('***********************')
		r -= 2
		c -= 2
		i += 1
	return x



r, c = map(int, input().split())
matrix = list(map(int, input().split()))[:(r*c)]
#print(c,r)
#print (matrix)
print (spirallyTraverse(matrix, c, r))

