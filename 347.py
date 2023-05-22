class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seet=list(set(nums))
        count_dict={}
        for item in nums:
            if item not in count_dict:
                count_dict[item]=1
            else:
                count_dict[item]+=1

        return list(dict(sorted(count_dict.items(),key=lambda x:x[1],reverse=True)[:k]).keys())


#%%
nums = [3,0,1,0]
k = 1
x=Solution
Solution.topKFrequent(x,nums,k)
#%%
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
dict(sorted(footballers_goals.items(),key=lambda x:x[1])[:2]).keys()


