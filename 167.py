class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j=0,len(numbers)-1
        while numbers[j-1]+numbers[0]>target:
            j-=1
        numbers = numbers[:j+1]
        # j=j+1
        while True:
            if numbers[i]+numbers[j]==target:
                if i<0:
                    i=i+len(numbers)
                if j <0:
                    j=j+len(numbers)
                return sorted([i+1,j+1])
            elif numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]>target:
                # i-=1
                j-=1


#%%
numbers = [-10,-8,-2,1,2,5,6]
target = 0

x=Solution
x.twoSum(x,numbers,target)

