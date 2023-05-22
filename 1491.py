class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.remove(max(salary))
        salary.remove(min(salary))
        avg=sum(salary)/float(len(salary))
        return avg

#%%
a=[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
x=Solution
Solution.average(x,a)
