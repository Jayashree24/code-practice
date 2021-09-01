"""
https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

"""
def solve(n, src, dest, helper):
	print (n, src, dest, helper)
	if n == 1:
		print ('1. Moving from %s to %s' % (src, dest))
		return
	solve(n-1, src, helper, dest)
	print ('2. Moving from %s to %s' % (src, dest))
	solve(n-1, helper, dest, src)
	print ('*********')

n = 2 
solve(n, 'A', 'C', 'B') 
	
