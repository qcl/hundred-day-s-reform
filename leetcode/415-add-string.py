class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        table = {
                '0':0,
                '1':1,
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                1:'1',
                2:'2',
                3:'3',
                4:'4',
                5:'5',
                6:'6',
                7:'7',
                8:'8',
                9:'9',
                0:'0'
            }

        maxDig = max(len(num1), len(num2))
        result = ""
        
        carry = 0
        
        for i in range(0, maxDig):
            n1 = 0
            n2 = 0
            if i < len(num1):
                n1 = table[num1[len(num1) - i - 1]]
            if i < len(num2):
                n2 = table[num2[len(num2) - i - 1]]
            
            n = n1 + n2 + carry
            if n >= 10:
                carry = 1
            else:
                carry = 0
            
            result = table[n%10] + result
        
        if carry:
            result = '1' + result
        
        return result
        
        
