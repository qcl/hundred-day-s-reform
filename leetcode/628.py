class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        # [0, +, +, +]
        # [+ ,+, +, +]  => right most 3
        # [-, +, +, +]

        # [-, -, +, +]
        
        # [-, 0, +, +]
        # [-, -, 0, +, +]
        # [-, -, ..., 0, +, +]
        
        # [-, -, 0, +]
        # [-, -, ..., -, 0 , +]

        # [-, -, -, +]

        a = nums[0] * nums[1] * nums[-1]
        b = nums[-3] * nums[-2] * nums[-1]

        if a > b:
            return a
        else:
            return b
        
