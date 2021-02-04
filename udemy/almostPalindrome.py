"""
https://leetcode.com/problems/valid-palindrome-ii/

Given a string, determine if its almost a palindrome.
A string is almost palindrome if it becomes palindrome
by removing 1 letter. Consider only alphanumeric characters and
ignore case sensitivity.

Example 1 -
race a car - becomes palindrome by removing a or e

Example 2 -
abccdba - becomes palindrome d

Example 3 -
abcdefdba - Not a almost palindrome.
"""

def validpal(s, l, r):
	while l <= r:
		print ("%s=%s %s=%s" % (l, s[l], r, s[r]))
		if not s[l] == s[r]:
			return False
		l += 1
		r -= 1
	return True 

def almostPalindrome(s):
	l, r = 0, len(s) - 1 
	removed = False
	print (s)
	while l <= r:
		print ("*.%s=%s %s=%s" % (l, s[l], r, s[r]))
		if not s[l] == s[r]:
			if s[l+1] == s[r] and s[l] == s[r-1]:
				ret = validpal(s, l+1, r)
				if ret:
					return ret
				return validpal(s, l, r-1)
			elif s[l+1] == s[r]:
				return validpal(s, l+1, r) 
			elif s[l] == s[r-1]:
				return validpal(s, l, r-1)
			else:
				return False
		else:
			l += 1
			r -= 1
	return True
				

s = 'raceacar'
s = 'abczzdba' # False
#s = 'abcczcdba' # False
#s = 'abczzcdba' # True
#s = 'daba'
#s = 'pabapd'
#s = 'raceacar'
#s = 'abccdba'
#s = 'abapqqaba'
s = "ebcbbececabbacecbbcbe"
#s = "eeccccbebaeeabebccceea"
#s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print (almostPalindrome(s))
	
	
