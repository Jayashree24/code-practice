"""
https://www.geeksforgeeks.org/count-permutations-possible-by-replacing-characters-in-a-binary-string/

Count permutations possible by replacing ‘?’ characters in a Binary String

Given a string S consisting of characters 0, 1, and ‘?’, the task is to count all possible combinations of the binary string formed by replacing ‘?’ by 0 or 1.

Examples:

    Input: S = “0100?110”
    Output: 2
    Explanation: Replacing each ‘?’s with ‘1’ and ‘0’, the count of such strings formed will be equal to “01001110” and “01000110”. Therefore, the total count of such strings formed is 2.

    Input: S = “00?0?111”
    Output: 4
"""

def countPermutations(s):
	cnt = s.count('?')
	if cnt:
		#return pow(2, cnt)
		return 2 ** cnt
	return cnt


s = input()
print (countPermutations(s))
