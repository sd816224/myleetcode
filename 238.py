class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        zeros=nums.count(0)
        if zeros==0:
            all=1
            for i in nums:
                all=all*i
            ans = []
            for i in nums:
                ans.append(all/i)

        elif zeros==1:
            location=nums.index(0)
            ans = ans = [0] * len(nums)
            nums.pop(location)
            all = 1
            for i in nums:
                all = all * i
            ans[location]=all
        elif zeros>1:
            ans=[0]*len(nums)


        return ans
#%%
nums = [-1,1,0,-3,3]
x=Solution
Solution.productExceptSelf(x,nums)
#%%
7%3
#%%
nums = [1,2,3,4]
nums.index(2)