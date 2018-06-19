class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''
        lcp = strs[0]
        for i in range(1, len(strs)):
            string = strs[i]
            if len(lcp) > len(string):
                lcp = lcp[:len(string)]
            for j in range(0, len(string)):
                if j < len(lcp):
                    if string[j] != lcp[j]:
                        lcp = lcp[:j]
                        break
            if len(lcp) == 0:
                return ''
        return lcp
