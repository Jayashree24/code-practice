"""
square root of a number without using sqrt library
"""
import math

def sqrt_num(n):
	x = 1 
	while x:
		y = n/x
		#print (x, y)
		if abs(x-y) <= 0.0000001:
			x = float("{:.10f}".format(x))
			return x
		elif x > y:
			x = (x + y) / 2
		elif x < y:
			x += 1

print (sqrt_num(1234))


def sqrt_n(n):
	#return n ** 0.5
	return pow(n, 0.5)

print (sqrt_n(1234))


