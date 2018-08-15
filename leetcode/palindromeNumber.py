class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        d = 1
        while x / d >= 10:
            d = d * 10
        
        while x != 0:
            if x/d != x%10:
                return False
            x = (x % d) / 10
            d = d / 100
        
        return True
        
    
