class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(nums)!=len(set(nums)) else False

#%%
nums =[2,14,18,22,22]
x=Solution
x.containsDuplicate(x,nums)

#%%
list=str(-122)
#%%
list[::-1]
#%%
a=[1,2,3,4,1]
1 in a
