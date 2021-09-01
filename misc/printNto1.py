"""
https://www.geeksforgeeks.org/program-to-print-numbers-from-n-to-1-in-reverse-order/

"""

def recur(n):
	if n == 1:
		print (n)
		return
	print (n)
	recur(n-1)

recur(5)
