"""
https://www.geeksforgeeks.org/merge-transactions-in-bank-sheets-in-the-order-of-their-occurrence-such-that-their-sum-remains-positive/

Merge transactions in bank sheets in the order of their occurrence such that their sum remains positive

Given an array arr[] consisting of N integers representing N transactions, the task is to merge the given lists of transactions in the order of their occurrences, such that at any point of time, the sum of already performed transactions is non-negative. If found to negative, then print “-1”. Otherwise, print the merged list of transactions.



Input: arr[][] = {{100 → 400 → -1000 → -500}, {-300 → 2000 → -500}}
Output: 100 → 400 → -300 → 2000 → -500 → -1000 → -500
Explanation: The sum at every instant of the above list of transactions is given by {100, 500, 200, 2200, 1700, 700, 200}, which has no negative values.

Input: arr[][] = [[100 → 400]]
Output: 100 400
"""

def MergeBankSheets():
	m = list(map(int, input().split()))
	n = list(map(int, input().split()))
	print (m, n)
	i = j = 0
	sum_m = 0
	sum_n = 0
	x = []
	while i < len(m) and j < len(n):
		print (sum_m, m[i], sum_n, n[j])
		if sum_m + m[i] > sum_n + n[j]:
			sum_m += m[i]
			x += [m[i]]
			i += 1
		elif sum_m + m[i] < sum_n + n[j]:
			sum_n += n[j]
			x += [n[j]]
			j += 1
		else:
			sum_m += m[i]
			sum_n += n[j]
			x += [m[i], n[j]]
			x += 1
			j += 1
	x += (m[i:] + n[j:])
	return x


			
		

print (MergeBankSheets())


