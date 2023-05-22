class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        while True:
            if 'R' not in senate:
                return 'Dire'
            elif 'D' not in senate:
                return 'Radiant'
            else:
                checker = 0
                while checker<len(senate):
                    # if checker==len(senate)-1 and senate[checker]!=' ':
                    #     if senate[checker] == 'R':
                    #         senate =senate.replace('D', ' ', 1)
                    #     elif senate[checker] == 'D':
                    #         senate =senate.replace('R', ' ', 1)

                    if senate[checker]=='R':
                        if 'D' in senate[checker:]:
                            senate=senate[:checker]+senate[checker:].replace('D',' ',1)
                        else:
                            senate = senate.replace('D', ' ', 1)
                    elif senate[checker]=='D':
                        if 'R' in senate[checker:]:
                            senate=senate[:checker]+senate[checker:].replace('R',' ',1)
                        else:
                            senate = senate.replace('R', ' ', 1)

                    checker+=1



#%%

x=Solution
Solution.predictPartyVictory(x,'DRRDRDRDRDDRDRDR')

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