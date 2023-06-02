class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hm={}
        for i in s1:
            hm[i]=1+hm.get(i,0)
        letters=hm.copy()

        l=0
        r=0
        while r < len(s2):
            if s2[r] not in letters:
                r+=1
                l=r
                letters = hm.copy()
                continue

            elif letters[s2[r]]>0:
                letters[s2[r]]-=1
                if max(letters.values())==0:
                    return True
                r+=1
            else:
                letters[s2[l]]+=1
                l+=1

        return False


#%%  test
s1 = "adc"
s2 = "dcda"
x=Solution
x.checkInclusion(x,s1,s2)

#%%
a='asdfasdf'
b=list(a)
#%%
b.pop(a.index('f'))
#%%
for i in range(10):
    i-=1
    print(i)