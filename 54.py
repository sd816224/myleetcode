class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        def rotate(matrix):
            ratate = []
            n = len(matrix[0])
            for i in range(n):
                ratate.append([])
                for item in matrix:
                    ratate[i].append(item[n - i - 1])
            return ratate

        while len(matrix)>0:
            ans+=matrix.pop(0)
            if matrix:
                matrix=rotate(matrix)
            else:
                return ans



    def rotate(self,matrix):
        ratate=[]
        n=len(matrix[0])
        for i in range(n):
            ratate.append([])
            for item in matrix:
                ratate[i].append(item[n-i-1])
        return ratate

#%%  test
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
x=Solution
x.spiralOrder(x,matrix)

#%%
list=str(-122)
#%%
list[::-1]
#%%
x = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
x.pop(0)
