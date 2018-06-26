class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        char_count = {}
        m = 0
        mc = S[0]

        for i in range(0, len(S)):
            s = S[i]
            if not s in char_count:
                char_count[s] = 0
            char_count[s] = char_count[s] + 1
            if char_count[s] > (len(S)+1)/2:
                return ""
            if char_count[s] > m:
                m = char_count[s]
                mc = s

        ns = mc * char_count[mc]
        del char_count[mc]
        
        for s in char_count:
            ns = s * char_count[s] + ns

        a = ns[:len(ns)/2]
        b = ns[len(ns)/2:]

        r = ''
        for i in range(0, len(a)):
            r = r + b[i] + a[i]
        if len(b) > len(a):
            r = r + b[-1]
        return r
