class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        ans=[]
        if nums.count(0)>=3:
          ans.append([0,0,0])
          while nums.count(0)>1:
              nums.remove(0)

        for i in range(len(nums)-2):
            # if i>0 and nums[i]==nums[i-1]:
            #     continue
            l,r = i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]==-nums[i]:
                    arr=sorted([nums[i],nums[r],nums[l]])
                    if arr not in ans:
                        ans.append(arr)
                    # break
                    l+=1
                elif nums[l]+nums[r]>-nums[i]:
                    r-=1
                else:
                    l+=1
        return ans



#%%  test
nums = [-2,0,1,1,2]
x=Solution
x.threeSum(x,nums)

#%%
a=[0,0,0,0]
a.count(0)
#%%
a.replace(0,1)