class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        hm={}
        # hm[s[0]]=1
        ans=0
        for r in range(len(s)):
            hm[s[r]]=1+hm.get(s[r],0)
            while sum(hm.values())-max(hm.values())>k:
                hm[s[l]]-=1
                l+=1
            ans=max(ans,sum(hm.values()))
        return ans

#%%
s = "AABABBA"
k = 1
x=Solution
x.characterReplacement(x,s,k)

#%%
a = "abcabcbb"
a.index('b')
#%%
l=r=0
#%%
a={'a':1,"b":2,'c':5}
#%%
sum(a.values())
