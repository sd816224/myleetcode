# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         ss=list(s)
#         tt=list(t)
#         ss.sort()
#         tt.sort()
#         if ss==tt:
#             return True
#         else:
#             return False


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if ''.join(sorted(s)) == ''.join(sorted(t)):
            return True
        else:
            return False


#%%
s="anagram"
t="nagaram"
x=Solution
x.isAnagram(x,s,t)

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
