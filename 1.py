class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1,i in enumerate(nums):
            for index2,j in enumerate(nums[index1+1:]):
                # a=nums[index1]
                # b=nums[index1+1:][index2]
                if i+j==target:
                    return[index1,index1+index2+1]


#%%  test
nums=[2,7,11,15]
target=9
x=Solution
x.twoSum(x,nums,target)

