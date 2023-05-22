class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def convert_letter(letter):
            if letter == 'I':
                print(1)
                return 1
            elif letter == 'V':
                print(5)
                return 5
            elif letter == 'X':
                print(10)
                return 10
            elif letter == 'L':
                print(50)
                return 50
            elif letter == 'C':
                print(100)
                return 100
            elif letter == 'D':
                print(500)
                return 500
            elif letter == 'M':
                print(1000)
                return 1000

        number =0

        if 'CM' in s:
            number +=900
            s=s.replace('CM','')
        if 'CD' in s:
            number +=400
            s=s.replace('CD','')
        if 'XC' in s:
            number +=90
            s=s.replace('XC','')
        if 'XL' in s:
            number +=40
            s=s.replace('XL','')
        if 'IX' in s:
            number +=9
            s=s.replace('IX','')
        if 'IV' in s:
            number +=4
            s=s.replace('IV','')

        for letter in s:
            print(letter)
            number+=convert_letter(letter)
        return number





#%%  test
x=Solution
x.romanToInt(x,'MCMXCIV')


#%%
a='ABCDEBC'
'BC' in a
#%%
a.replace('BC','')