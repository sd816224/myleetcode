class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        arr= [[0]*(len(nums1)+1) for _ in range(1+len(nums2))]

        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j]==nums2[i]:
                    arr[i+1][j+1]=arr[i][j]+1
                else:
                    arr[i+1][j+1]=max(arr[i+1][j],arr[i][j+1])
        return arr[-1][-1]



#%%
nums1 = [2,1]
nums2 = [1,2,1,3,3,2]
x=Solution


# x.canConstruct(x,ransomNote,magazine)
x.maxUncrossedLines(x,nums1,nums2)
#%%
