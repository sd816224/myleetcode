class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans=0
        left = 0
        right = len(nums) - 1
        while left<=right:
            if nums[left]+nums[right]>target:
                right-=1
            else:
                ans+=2**(right-left)
                left+=1

        return ans % (10 ** 9 + 7)
    """lee
                for index1, i in enumerate(nums):
            # if i *2<=target:
                # ans+=1
            # pailie_len=len(nums)-index1
            tail=nums[index1+1:]
            if i*2<=target:
                if not tail:
                    ans+=1
                    print(i,'single')
                    break
                for index2, j in enumerate(tail):
                    if (index2==len(tail)-1) and (i+j<=target):
                        pailie_len = len(tail)
                        ans += 2 ** pailie_len
                        print(i,j,2 ** pailie_len)
                    if i+j>target:
                        pailie_len=nums.index(j)-index1-1

                        print(i,j,'---',2**pailie_len)
                        ans+=2**pailie_len
                        break
        
        """






#%%
nums = [2,3,3,4,6,7]
target = 12
x=Solution
Solution.numSubseq(x,nums,target)
#%%
a=[1,2,3,4,5,1]
# a.index(1)
for index,a in enumerate(a):
    print(index,a)
    #%%
a=[3,2,4,5,1,0]
a.sort()