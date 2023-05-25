class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right)/2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
#%%
nums = [-1,0,2,5,9,12]
target = 2
# nums = [-1,0,3,5,9,12]
# target = 9
x=Solution
Solution.search(x,nums,target)

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
a='abcdeft'
len(a)
#%%
a[6]