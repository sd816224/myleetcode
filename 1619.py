class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        x=int(len(arr)*0.05)
        new_arr=arr[x:-x]
        ans=round(sum(new_arr)/len(new_arr),5)
        return ans

#%%
arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
x=Solution
Solution.trimMean(x,arr)

#%%
# a='sdafewraaaaa'
# i=0
# while i < len(a):
#
#     b=a[i]
#     print(b)
#     a=a.replace('a','',1)
#     i += 1

#%%
arr = [6,0,3,4]
arr.sort()
#%%
arr=arr[1:-1]

#%%
len(arr)*0.05
#%%
arr.remove(0)
arr.remove(0)
arr.remove(10)
arr.remove(10)
#%%
sum(arr)/len(arr)
#%%
a=0.123128123
round(a,5)