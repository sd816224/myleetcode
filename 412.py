class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        set=[]
        for i in range(1,10001):
            if i%3==0 and i %5 ==0:
                set.append('FizzBuzz')
            elif i%3==0:
                set.append('Fizz')
            elif i%5==0:
                set.append('Buzz')
            else:
                set.append(str(i))
        return set[:n]
#%%
x=Solution
Solution.fizzBuzz(x,5)
#%%
7%3
