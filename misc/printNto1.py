def recur(n):
	if n == 1:
		print (n)
		return
	print (n)
	recur(n-1)

recur(5)
