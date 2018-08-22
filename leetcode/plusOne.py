class Solution(object):         
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.digits = digits
        """in special case: no item in list, or only one item in list"""
        if len(digits) == 0:
            return 0
        if len(digits) == 1:
            if digits[0] == 9:
                return [1, 0]
            else:
                digits[0] += 1
                return digits
            
        """List has 2 or more items"""    
        if digits[- 1] != 9:
            digits[- 1] += 1
        else:
            digits[-1] = 0
            for i in range (1,len(digits)):
                if digits[-1-i] == 9:
                    digits[-1-i] = 0
                    if i == len(digits) - 1:
                        digits.insert(0, 1)
                else:
                    digits[-1-i] += 1
                    break
                
        return digits
