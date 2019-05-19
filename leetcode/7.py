class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = int(`abs(x)`[::-1])
        if x < 0:
            rev = -1 * rev
        if rev > 2**31 -1 or rev < -1 * 2**31:
            return 0
        return rev
