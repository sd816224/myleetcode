class Solution(object):

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        def distance_square(p1, p2):
            return (p1[1] - p2[1]) ** 2 + (p1[0] - p2[0]) **2
        # q=self.distance_square(p1,p2)
        tri=[]
        tri.append(distance_square(p1,p2))
        tri.append(distance_square(p1,p3))
        tri.append(distance_square(p1,p4))
        tri.append(distance_square(p2,p3))
        tri.append(distance_square(p2,p4))
        tri.append(distance_square(p3,p4))

        tri.sort()

        if p1==p2 or p1==p3 or p1==p4:
            return False

        if tri[0]==tri[1]==tri[2]==tri[3] and tri[3]*2==tri[4]==tri[5]:

        # if tri[0]+tri[1]==tri[2] and tri[0]==tri[1] and distance_square(p1,p2)==distance_square(p3,p4) and distance_square(p1,p3)==distance_square(p2,p4) and distance_square(p1,p4)==distance_square(p3,p2):
            return True
        else:
            return False

        # if distance_square(p1,p2)==distance_square(p3,p4) and distance_square(p1,p3)==distance_square(p2,p4) and distance_square(p1,p4)==distance_square(p3,p2) :
        #     return True
        # else:
        #     return False


#%%
# p1 = [0,0]
# p2 = [1,1]
# p3 = [1,0]
# p4 = [0,1]

# p1 = [0,0]
# p2 = [1,1]
# p3 = [1,0]
# p4 = [0,12]
#
# p1 = [1,0]
# p2 = [-1,0]
# p3 = [0,1]
# p4 = [0,-1]

p1 = [0,1]
p2 = [1,2]
p3 = [0,2]
p4 = [0,0]

x=Solution
Solution.validSquare(x,p1,p2,p3,p4)
#%%
7%3
#%%
(-1)**2
#%%
a=[1,3,2]
b=[1,3,2]
a==b
#%%
1==1==1==1
