import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def normal_cal(a,b,i):
            if i=='+':
                return a+b
            elif i=='-':
                return a-b
            elif i=='*':
                return a*b
            elif i=='/':
                return math.trunc(a/b)

        stack=[]
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                b=stack.pop(-1)
                a=stack.pop(-1)
                stack.append(normal_cal(a,b,i))

        return stack[0]

#%%
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
x=Solution
Solution.evalRPN(x,tokens)
#%%
a='+'
int(a)
#%%
a.isnumeric()
