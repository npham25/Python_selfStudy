class Solution(object):
    def lengthOfLastWord(self, s):
        self.s = s
        
        if(len(s) == 0):
            return 0
 """delete space(s) in the end of String:"""      
        i = len(s) - 1       
        while s[i] == ' ' and i >= 0:
            i -= 1
            
        if i == -1:
            return 0
        elif i == 0:
            return 1
        else:
            s = s[0:i]
            
"""find the index of the space before the last word (j)"""
            j = len(s) - 1
            while s[j] != ' ' and j >= 0:
                j -= 1
                
            return i - j
            
