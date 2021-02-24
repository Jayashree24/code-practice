"""
Find factorial of a number usign recursion.
"""

# Identify a base case
# Identify a recursive case
# 2 returns - for base and recursive case

def factorial_recursion(n):
	if n == 0 or n == 1:
		return 1
	return (n * factorial_recursion(n-1))

print (factorial_recursion(5))


def factorial_iterative(n):
	fact = 1
	while n:
		fact *= n
		n -= 1 
	print (fact)

factorial_iterative(3)
	
