"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""
def maxProfit(prices):
	print (prices)
	l = len(prices)
	sell = 0
	buy = prices[0]
	for i in range(l):
		#if buy > prices[i]:
		#	buy = prices[i]
		buy = min(buy, prices[i])
		t = prices[i] - buy
		#if sell < t:
		#	sell = t
		sell = max(sell, prices[i] - buy)
		print ("[%s] buy=%s t=%s sell=%s" % (prices[i], buy, t, sell))
	return sell

#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
#prices = [7,2,5,3,6,4, 8, 1, 9]
#prices = [3,2,6,5,0,1]
prices = [2,1,2,1,0,1,2]
print (maxProfit(prices))
