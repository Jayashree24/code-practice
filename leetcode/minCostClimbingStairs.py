"""
https://leetcode.com/problems/min-cost-climbing-stairs/

Example 1:

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:

    cost will have a length in the range [2, 1000].
    Every cost[i] will be an integer in the range [0, 999].

"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)
        
        if l == 2:
            return min(cost)
        elif l == 3:
            return min(cost[0] + min(cost[1], cost[2]), cost[1] + min(cost[2], 0))
        
        min_jump = float('inf')
        print (cost)
        for start in range(2):
            i = start
            jump = cost[start]
            while i < l-1:
                #print (i, cost[i])
                x = 0
                if (i+2) < l:
                    x = cost[i+2]
                print (cost[i], cost[i+1], x)
                k = 1
                if x <= cost[i+1]:
                    k = 2
                jump += min(cost[i+1], x)
                print ("jump = %s k=%s" % (jump, k))
                i += k
                print ('********************')
            min_jump = min(min_jump, jump)
        return min_jump
        
        
            
            
        
