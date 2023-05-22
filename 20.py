class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        closeToOpen={")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
#%%  test
s = "(([]){})"
x=Solution
x.isValid(x,s)

#%%
a=[0,0,0,0]
a.count(0)
#%%
a.replace(0,1)
#%%
opcl = dict(('()', '[]', '{}'))
