class Solution(object):
    def lengthOfLastWord(self, s):
        self.s = s
        
        if(len(s) == 0):
            return 0
 """delete space(s) in the end of String:"""      
        i = len(s) - 1       
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        if i == -1:
            return 0
        elif i == 0:
            return 1
        """find the index of the space before the last word (j)"""
        else:
            j = i - 1
            while j >= 0 and s[j] != ' ':
                j -= 1
                
            return i - j
            
