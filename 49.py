class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans={}
        for string in strs:
            sorted_string=''.join(sorted(string))
            if sorted_string not in ans:
                ans[sorted_string]=[]
            ans[sorted_string].append(string)

        return list(ans.values())
#%%
strs =["eat","tea","tan","ate","nat","bat"]
x=Solution
x.groupAnagrams(x,strs)

#%%
a=["","",""]
for index,item in enumerate(a):
    print(index,item)
    #%%

list('asdfasdf')
#%%
a='asdfasdfadsfasdf'
b=sorted(a)
''.join(b)
#%%
dp=[[0]*6 for _ in range(5)]
dp
