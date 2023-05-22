class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        list=[0,1,1]
        for i in range(n-1):
            list.append(list[-1]+list[-2]+list[-3])

        return list[n]




#%%  test
n=5
x=Solution
x.tribonacci(x,n)

#%%
list=str(-122)
#%%
list[::-1]