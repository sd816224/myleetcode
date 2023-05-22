class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        list=[0,1]
        for i in range(n-1):
            list.append(list[-1]+list[-2])

        return list[n]




#%%  test
n=4
x=Solution
x.fib(x,n)

#%%
list=str(-122)
#%%
list[::-1]