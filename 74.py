class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top=0
        bottom= len(matrix)-1
        l=0
        r=len(matrix[0])-1

        while top <= bottom:
            mid=int((top+bottom)/2)
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                target_row=matrix[mid]
                while l<=r:
                    mid=int((l+r)/2)
                    if target ==target_row[mid]:
                        return True
                    elif target >target_row[mid]:
                        l=mid+1
                    elif target< target_row[mid]:
                        r=mid-1
                return False
            elif target >matrix[mid][-1]:
                top = mid+1
            elif target< matrix[mid][0]:
                bottom=mid-1
        return False

#%%
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
x=Solution
x.searchMatrix(x,matrix,target)

#%%
list=str(-122)
#%%
list[::-1]
#%%
a=['b','c','x','a']
a.sort()
#%%
d={a:'a'}
'a' in d
