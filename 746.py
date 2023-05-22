class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.reverse()

        cost_each_step_reverse=cost[:2]
        for i in cost[2:]:
            cost_each_step_reverse.append(i+min(cost_each_step_reverse[-2:]))

        cost_each_step_reverse.reverse()
        cost.reverse()

        i = 0
        ans = 0
        while True:
            if cost_each_step_reverse[i] >= cost_each_step_reverse[i + 1]:
                # inspect=cost[i:i+2]
                ans += cost[i + 1]
                i += 2
            else:
                ans += cost[i]
                i += 1

            if i >= len(cost) - 1:
                return ans

        return cost_each_step_reverse


#%%  test
cost = [10,15,20]
x=Solution
x.minCostClimbingStairs(x,cost)

#%%
list=str(-122)
#%%
list[::-1]