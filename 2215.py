class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans1=[]
        ans2=[]
        for i in list(set(nums1)):
            if i not in nums2:
                ans1.append(i)
        for i in list(set(nums2)):
            if i not in nums1:
                ans2.append(i)
        return [ans1,ans2]

#%%
nums1 = [1,2,3]
nums2 = [2,4,6]
x=Solution
Solution.findDifference(x,nums1,nums2)
