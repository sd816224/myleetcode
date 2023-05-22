class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        list=str(x)
        if list==list[::-1]:
            return True
        else:
            return False


#%%  test

x=Solution
x.isPalindrome(x,-121)

#%%
list=str(-122)
#%%
list[::-1]