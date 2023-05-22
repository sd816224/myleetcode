class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ans = []
        l, r = 0, len(height) - 1
        water = (r - l) * min(height[r], height[l])
        # def find_next_right(height, l, r,last_top):
        #     while height[r] < last_top and r < l:
        #         r -= 1
        #     return r
        # water=(r-l)*min(height[r],height[l])
        while l+1<r:
            if height[l]>height[r]:
                while height[r-1]<height[r]:
                    if l < r:
                        r-=1
                    else:
                        return water
                r-=1
            else:
                while height[l+1]<height[l]:
                    if l<r:
                        l+=1
                    else:
                        return water
                l+=1

            water=max((r-l)*min(height[r],height[l]),water)

        return water

    def find_next_right(self,height,l,last_top,r):
        while height[r]<last_top and r<l:
            r-=1
        return r



#%%
height = [1,1]
x=Solution
Solution.maxArea(x,height)

#%%
# a='sdafewraaaaa'
# i=0
# while i < len(a):
#
#     b=a[i]
#     print(b)
#     a=a.replace('a','',1)
#     i += 1

#%%
a='abcdeft'
len(a)
#%%
a[6]