class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans=0

        for index,i in enumerate(mat):
            ans+=i[index]

        for i in mat:
            i.reverse()

        for index,i in enumerate(mat):
            ans+=i[index]

        if len(mat)%2==1:
            ans=ans-mat[int(len(mat)/2)][int(len(mat)/2)]

        return ans

#%%  test
mat = [[5]]
x=Solution
x.diagonalSum(x,mat)

#%%
list=str(-122)
#%%
list[::-1]