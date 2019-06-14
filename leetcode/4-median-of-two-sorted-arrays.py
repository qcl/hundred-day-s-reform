class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        mergedSortedArray = []
        indexOne = 0
        indexTwo = 0
        while indexOne != len(nums1) or indexTwo != len(nums2):
            if indexOne == len(nums1):
                mergedSortedArray.append(nums2[indexTwo])
                indexTwo += 1
                continue
            
            if indexTwo == len(nums2):
                mergedSortedArray.append(nums1[indexOne])
                indexOne += 1
                continue
            
            if nums1[indexOne] > nums2[indexTwo]:
                mergedSortedArray.append(nums2[indexTwo])
                indexTwo += 1
            else:
                mergedSortedArray.append(nums1[indexOne])
                indexOne += 1

        resultLen = len(mergedSortedArray)
        if resultLen % 2 == 1:
            return mergedSortedArray[resultLen/2]
        else:
            return (mergedSortedArray[resultLen/2] + mergedSortedArray[resultLen/2 - 1]) / 2.0
