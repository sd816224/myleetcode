class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        nums.sort()
        lcs=0
        ans=1

        if nums:
            last = nums[0]
        else:
            return 0
        for i in nums:
            if i == last+1:
                ans+=1
            else:
                lcs=max(ans,lcs)
                ans=1
            last=i
        lcs=max(ans,lcs)
        return lcs
#%%
nums = [0,-1]

x=Solution
x.longestConsecutive(x,nums)


#%%
s = "A man, a plan, a canal: Panama"
s.lower()

