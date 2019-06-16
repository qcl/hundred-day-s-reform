class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    c = stack.pop()
                    if c != mapping[char]:
                        return False
        if len(stack) != 0:
            return False
    
        return True
