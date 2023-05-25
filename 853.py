
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time_needed_of_each_position=[]
        for i in position:
            time_needed_of_each_position.append([i])

        for index,(i, j) in enumerate(zip(position,speed)):
            time_needed_of_each_position[index].append((target-i)/j)

        time_needed_of_each_position.sort(key=lambda x:x[0],reverse=True)

        max_stack=[time_needed_of_each_position[0][1]]
        for i in time_needed_of_each_position[1:]:
            max_stack.append(max(max_stack[-1],i[1]))
        # print('a')

        return len(set(max_stack))

        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            if not stack:
                stack.append(dist / vel)
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)
#%%
target = 10
position = [6,8]
speed = [3,2]
x=Solution
Solution.carFleet(x,target, position, speed)
#%%
target=12
speed = [2,4,1,1,3]
time_needed_of_each_position=[]
position = [10,8,0,5,3]
for i in position:
    time_needed_of_each_position.append([i])
for index, (i, j) in enumerate(zip(position, speed)):
    time_needed_of_each_position[index].append((target - i) / j)
#%%
time_needed_of_each_position.sort(key=lambda x:x[0],reverse=True)