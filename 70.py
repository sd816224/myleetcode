class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 2
        elif n==1:
            return 1

        choose_array=[1,2]
        for i in range(n-3):
            choose_array.append(sum(choose_array[-2:]))


        return sum(choose_array[-2:])




#%%  test
n=3
x=Solution
x.climbStairs(x,n)

#%%
list=str(-122)
#%%
list[::-1]