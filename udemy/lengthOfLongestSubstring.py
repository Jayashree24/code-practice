"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
	hmap = {}
	j = 0
	l = 0 
	ll = 0 
	print (s)
	for i in range(len(s)):
		print ("%s=%s max=%s" % (i, s[i], ll))	
		x = hmap.get(s[i], None)
		if x is None:
			hmap[s[i]] = i
			l += 1
		else:
			j = max(j, x + 1)
			l = i - j + 1
			ll = max(ll, l)
			print ('len=%s j=%s' % (l, j))
			hmap[s[i]] = i
		ll = max(ll, l)
		#print (hmap)
		print (s[j:i+1])
	return ll 
		
			

s = 'abcabcbb'
#s = 'bbbbb'
#s = 'pwwkew'
#s = 'pwwkewabcdeabaghiabcdefgh'
#s = 'pwwkewabcdpqrstuvwxyzeabaghiabcdefgh'
print (lengthOfLongestSubstring(s))


