def maxProfit(prices):
	buy = prices[0]
	dif = 0
	for i in range(len(prices)-1):
		if prices[i] <= buy:
			buy = prices[i]
			sell = max(prices[i+1:])
			if sell < buy:
				continue
			dif = max(dif, sell - buy)
	return dif 
			
		
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
#prices = [7,2,5,3,6,4, 8, 9, 1]
prices = [3,2,6,5,0,3]
print (maxProfit(prices))
