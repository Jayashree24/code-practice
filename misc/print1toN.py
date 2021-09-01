"""
print all the numbers from 1 to N recursively

"""

# IBH - Method
# Base Condition - Hypothesis - Induction
def print_n(n):
	# Base Condition - smallest valid input
	if n == 1:
		print (n)
		return
	# Hypothesis - smaller input
	print_n(n-1)
	# Induction Step
	print (n)

print_n(7)
