class Solution(object):
    def commonPrefixTwoArrays(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        i = 0
        j = 0
        res = ''
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j] :
                res += s1[i]
                i += 1
                j += 1
            else:
                break
        return res
    
    def longestCommonPrefix(self, strs):
        self.strs = strs
        
        if len(strs)== 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        res = self.commonPrefixTwoArrays(strs[0], strs[1])
        
        for i in range(2,len(strs)):
            res = self.commonPrefixTwoArrays(res, strs[i])
        
        return res
