class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=''
        res=[]
        l=0
        r=0
        def dfs(l,r,result,):
            if l==n and r==n:
                res.append(result)
                return
            if l<n:
                dfs(l+1,r,result+'(')
            if r<l:
                dfs(l,r+1,result+')')
        dfs(l,r,result)

        return res
#%%

x=Solution
Solution.generateParenthesis(x,3)
#%%
a=[1,2,3,4]
a.sum()