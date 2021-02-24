"""
Implement a function that reverses a string using iteration
and then recursion!
"""

def reverseString(s):
	t = ''
	for i in range(len(s)-1, -1, -1):
		t += s[i]
	return t

print (reverseString('apple pie'))


def reverse_recursion(s):
	if len(s) == 0:
		#print ('returns %s' % s)
		return s
	#print (s[1:], s[0])
	return reverse_recursion(s[1:]) + s[0]

print (reverse_recursion('apple pie'))
	
