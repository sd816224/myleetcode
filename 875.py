import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def cc(h):
            return sum(math.ceil(pile /h) for pile in piles)

        l,r=1,10**9
        piles.sort(reverse=True)
        while l<=r:
            mid=int((l+r)/2)
            # if cc(mid)==h:
            #     return mid
            if cc(mid)>h:
                l=mid+1
            else:
                r=mid-1
        return l
#%%

piles = [30,11,23,4,20]
h = 6
x=Solution
Solution.minEatingSpeed(x,piles,h)
#%%
a=[1,6,4,3,7,]
a.sort(reverse=True)

low, high = 1, 10 ** 9
while low <= high:
    k = (low + high) // 2
    if sum(math.ceil(1.0 * pile / k) for pile in piles) > h:
        low = k + 1
    else:
        high = k - 1
return low