class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        max_length = 0
        length = 1
        for i in range(1, len(nums)):
            number = nums[i]
            if number > nums[i-1]:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                length = 1
        if length > max_length:
            return length
        return max_length
