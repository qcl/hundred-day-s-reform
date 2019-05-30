class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        l = 0
        i = 0
        ss = s[0:1]
        for j in range(1, len(s)):
            if not s[j] in ss:
                ss = s[i:j+1]
            else:
                i = i + ss.index(s[j]) + 1
                ss = s[i:j+1]
            
            #print j,s[j],ss
            l = max(len(ss), l)
        return l
