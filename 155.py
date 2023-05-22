class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min=[]
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min:
            self.min.append(min(self.min[-1],val))
        else:
            self.min.append(val)
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)
        self.min.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        print(self.min[-1])
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#%%
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
#%%
obj.getMin()
obj.pop()
obj.top()
obj.getMin()

#%%
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
dict(sorted(footballers_goals.items(),key=lambda x:x[1])[:2]).keys()


#%%
stack=[]
#%%
stack=stack+[2]

#%%
stack.pop(-1)