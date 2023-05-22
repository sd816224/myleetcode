class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        dp={}
        for index in range(len(questions)-1,-1,-1):
            dp[index] =0
            pointer=questions[index][1]+1+index

            dp[index]=max(
                questions[index][0]+dp.get(pointer,0),
                dp.get(index+1,0)
            )
        return dp[0]




#%%  test
questions =[[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
x=Solution
x.mostPoints(x,questions)

#%%
list=str(-122)
#%%
a={1:100,2:200}
a.get(2,0)
#%%
for index in range(5,0,-1):
    print(index)