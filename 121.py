class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r=0,1
        max_profit=0
        while r < len(prices):
            if prices[l]>prices[r]:
                l=r
                r+=1
            # elif prices[r]>prices[r-1]:
            #     max_profit=max(max_profit,prices[])
            else:
                max_profit=max(max_profit,prices[r]-prices[l])
                r+=1
        return max_profit
#%%
prices =[2,1,4]
x=Solution
Solution.maxProfit(x,prices)
#%%

a=[1,2,3,4]
len(a)