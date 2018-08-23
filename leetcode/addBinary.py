class Solution(object):
    def addBinary(self, a, b):
        self.a = a
        self.b = b
        r = ""
        max = ""
        min = ""
        carry = 0

        if (len(a) - len(b)) >= 0:
            max = a
            min = b
        else:
            max = b
            min = a
        
        for j in range (len(max) - len(min)):
            min = "0" + min
            j += 1
            
        for i in range(len(max)):
            if int(min[-1-i]) + int(max[-1-i]) + carry >= 2:
                r = str(((int(min[-1-i]) + int(max[-1-i]))%2 + carry)%2) + r
                carry = 1
                if i == len(max) - 1:
                    r = "1" + r
            else:
                r = str(int(min[-1-i]) + int(max[-1-i]) + carry) + r
                carry = 0
                    
        return r
