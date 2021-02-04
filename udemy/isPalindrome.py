"""
https://leetcode.com/problems/valid-palindrome/
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

Constraints:

    s consists only of printable ASCII characters.
"""
"""
def isPalindrome(s):
	s = [i for i in s if i.isalnum()]
	s = ''.join(s).lower()
	return s == s[::-1]
"""

def isPalindrome(s):
	i, j = 0, len(s) - 1
	while i <= j:
		print ("%s=%s %s=%s" % (i, s[i], j, s[j]))
		while i <=j and not s[i].isalnum():
			i += 1
		while i <= j and not s[j].isalnum():
			j -= 1
		#print ("AFTER %s=%s %s=%s" % (i, s[i], j, s[j]))
		if i <= j and not s[i].lower() == s[j].lower():
			return False
		else:
			i += 1
			j -= 1
	return True

#s = "A man, a plan, a canal: Panama"
#s = "race a car"
s = "-"
print (isPalindrome(s))
