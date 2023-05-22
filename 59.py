class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def direction_appoint(i, j, direction, arr, n):
            if direction == 'right':
                while j < n - 1:
                    j += 1
                    if arr[i][j] == 0:
                        arr[i][j] = aa.pop(0)
                    else:
                        j -= 1
                        return i, j, arr
                return i, j, arr

            elif direction == 'down':
                while i < n - 1:
                    i += 1
                    if arr[i][j] == 0:
                        arr[i][j] = aa.pop(0)
                    else:
                        i -= 1
                        return i, j, arr
                return i, j, arr

            elif direction == 'left':
                while j > 0:
                    j -= 1
                    if arr[i][j] == 0:
                        arr[i][j] = aa.pop(0)
                    else:
                        j += 1
                        return i, j, arr
                return i, j, arr

            elif direction == 'up':
                while i > 0:
                    i -= 1
                    if arr[i][j] == 0:
                        arr[i][j] = aa.pop(0)
                    else:
                        i += 1
                        return i, j, arr
                return i, j, arr

        arr = []
        for i in range(n):
            arr.append([])
            for j in range(n):
                arr[i].append(0)
        aa = list(range(1, n ** 2 + 1))
        i = 0
        j = 0
        arr[0][0] = aa.pop(0)
        for direction in (n - 1) * ['right', 'down', 'left', 'up']:
            i, j, arr = direction_appoint(i, j, direction, arr, n)
            if len(aa) == 0:
                break

        return arr

# %%
n=4
x=Solution
x.generateMatrix(x,n)


#%%


def direction_appoint(i,j,direction, arr,n):
    if direction == 'right':
        while j <n-1:
            j += 1
            if arr[i][j]==0:
                arr[i][j] = aa.pop(0)
            else:
                j-=1
                return i,j,arr
        return i, j, arr

    elif direction == 'down':
        while i < n - 1:
            i += 1
            if arr[i][j] == 0:
                arr[i][j] = aa.pop(0)
            else:
                i -= 1
                return i, j, arr
        return i, j, arr

    elif direction == 'left':
        while j>0:
            j -= 1
            if arr[i][j] == 0:
                arr[i][j] = aa.pop(0)
            else:
                j += 1
                return i, j, arr
        return i, j, arr

    elif direction == 'up':
        while i>0:
            i -= 1
            if arr[i][j] == 0:
                arr[i][j] = aa.pop(0)
            else:
                i += 1
                return i, j, arr
        return i, j, arr

#%%
n=5
arr=[]
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(0)
aa=list(range(1,n**2+1))
#%%
# aa=[1,2,3,4,5,6,7,8,9]
i=0
j=0
arr[0][0]=aa.pop(0)
for direction in (n-1)*['right','down','left','up']:
    i, j, arr = direction_appoint(i, j, direction, arr, n)
    if len(aa)==0:
        break


#%%

i,j,arr=direction_appoint(i,j,'right',arr,n)
#%%
i,j,arr=direction_appoint(i,j,'down',arr,n)
#%%
i,j,arr=direction_appoint(i,j,'left',arr,n)
#%%
i,j,arr=direction_appoint(i,j,'up',arr,n)


#%%
direction='right'
i=0
j=0
step=3
arr[i][j]=aa.pop(0)
if direction=='right':
    for astep in range(step-1):
        j+=1
        arr[i][j]=aa.pop(0)
        print(i,j)
#%%
direction='down'
if direction=='down':
    for astep in range(2):
        i+=1
        arr[i][j]=aa.pop(0)
        print(i, j)
#%%
direction='left'
if direction=='left':
    for astep in range(2):
        j-=1
        arr[i][j]=aa.pop(0)
        print(i, j)
#%%
direction='up'
if direction=='up':
    for astep in range(1):
        i-=1
        arr[i][j]=aa.pop(0)
        print(i, j)

#%%
a=[1,2,3,4]
a*2
