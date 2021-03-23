"""
Tail recursion for factorial calculation
Space Complexitiy - O(1)
"""

def fact(n, total_fact = 1):
	print ("n=%s total_fact=%s" % (n,total_fact))
	if n == 0:
		return total_fact
	return fact(n-1, n * total_fact)

print (fact(5))
