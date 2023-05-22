# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         s=s.lower()
#         ss=''
#         for letter in s:
#             if letter.isalnum():
#             # if (letter not in 'abcdefghijklmnopqrstuvwxyz') or ~letter.isdigit():
#                 ss+=letter
#         print(ss)
#
#         if ss==ss[::-1]:
#             return True
#         else:
#             return False

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()

        i,j=0,len(s)-1

        while i<j:
            while not s[i].isalnum() and i<j:
                i+=1
            while not s[j].isalnum() and i<j:
                j-=1
            print(i,j)
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1

        return True
#%%
s =".,"

x=Solution
x.isPalindrome(x,s)

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
#%%
'asdfasdf'[:4]
#%%
for i in range(10,-1,-1):
    print(i)