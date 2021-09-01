"""
Count all possible paths from top left to bottom right

The task is to count all the possible paths from top left to bottom right of a m X n matrix with the constraints that from each cell you can either move only to right or down.

Example 1:

Input: m = 2, n = 2
Output: 2 
Explanation: Two possible ways are
RD and DR.  


Example 2:

Input: m = 3, R = 3
Output: 6
Explanation: Six possible ways are
RRDD, DDRR, RDDR, DRRD, RDRD, DRDR. 

https://leetcode.com/problems/unique-paths/

"""

"""
def numberOfPaths(self, m, n, d={}):
	# code here
	#print (m,n,d)
	if m == 1 or n == 1:
		d[m,n] = 1
		return 1
	x = d.get((m,n-1), None)
	y = d.get((m-1,n), None)
	if not x:
		d[m,n-1] = self.numberOfPaths(m, n-1, d)
	if not y:
		d[m-1,n] = self.numberOfPaths(m-1, n, d)
	return d[m,n-1] + d[m-1,n]

def numberOfPaths(n, m):
	count = [[0 for x in range(n)] for y in range(m)]
	print (count)

	for i in range(m):
		count[i][0] = 1;

	for j in range(n):
		count[0][j] = 1;

	for i in range(1, m):
		for j in range(1, n):			
			count[i][j] = count[i-1][j] + count[i][j-1]
	return count[m-1][n-1]
"""

def numberOfPaths(p, q):
     
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]
print (numberOfPaths(14,23))


