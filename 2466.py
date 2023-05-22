class Solution(object):
    def countGoodStrings(self, l, h, z, o):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        global low
        global high
        global zero
        global one
        global dp
        global xxx
        low=l
        high=h
        zero=z
        one=o
        dp={}

        def next_state(index):
            if index>=low and index not in dp:
                dp[index]=1
            elif index>=low:
                dp[index]+=1

            for i in [zero,one]:
                if index+i<=high:
                    next_state(index+i)
            print(index)
        next_state(0)
        #
        # for i in list(dp.keys()):
        #     if i <low:
        #         dp.pop(i)

        return sum(list(dp.values()))


#%%
low = 200
high = 200
zero = 10
one = 1

x=Solution
x.countGoodStrings(x,low,high,zero,one)

#%%

a=0
def x():
    global a
    a=a+1
x()
a
#%%
a=1
list=[1,2]
sum(list)