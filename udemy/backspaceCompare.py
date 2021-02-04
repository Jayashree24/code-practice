"""
https://leetcode.com/problems/backspace-string-compare/

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.
"""

"""
def backspaceCompare(s, t):
	s_stack = []
	t_stack = []
	for i in s:
		if i != '#':
			s_stack.append(i)
		else:
			if s_stack:
				s_stack.pop()
	for i in t:
		if i != '#':
			t_stack.append(i)
		else:
			if t_stack:
				t_stack.pop()
	print (''.join(s_stack), ''.join(t_stack))
	return ''.join(s_stack) == ''.join(t_stack)
"""

def backspaceCompare(S, T):
    i = len(S) - 1
    j = len(T) - 1
    sh,th = 0,0
    print (S, T)
    while i >=0 or j >= 0:
        print ("%s=%s %s=%s sh=%s th=%s" % (i, S[i], j, T[j], sh, th))
        if (i >=0 and S[i] == '#') or (j >=0 and T[j] == '#'):
            if i >=0 and S[i] == '#':
                i = i - 1
                sh = sh + 1
            if j >=0 and T[j] == '#':
                j = j - 1
                th = th + 1
        else:
            if th > 0 or sh > 0:
                if sh > 0:
                    sh = sh - 1
                    i = i - 1
                if th > 0:
                    th = th - 1
                    j = j - 1
            else:
                if i >= 0 and j >= 0 and S[i] == T[j]:
                    i = i - 1
                    j = j - 1
                else:
                    return False
    return True

s = 'a##c'
s = 'ab#c'
s = 'ab##'
S = "ab#c"
T = "ad#c"
S = "ab##"
T = "c#d#"
S = "a##c"
T = "#a#c"
S, T = "a########c", "ccb#b##c#"
#S,T = "abc#d", "abzz##d"
print (backspaceCompare(S,T))
