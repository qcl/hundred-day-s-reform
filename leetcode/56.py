# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 1:
            return intervals

        sortedIntervals = sorted(intervals, key=lambda x: x.start)
        results = []
        
        baseInterval = Interval(sortedIntervals[0].start, sortedIntervals[0].end)
        i = 1
        while i < len(sortedIntervals):
            comparedInterval = sortedIntervals[i]
            if comparedInterval.start >= baseInterval.start and comparedInterval.start <= baseInterval.end:
                baseInterval = Interval(min(comparedInterval.start, baseInterval.start), max(comparedInterval.end, baseInterval.end)) 
            else:
                results.append(baseInterval)
                baseInterval = comparedInterval
            i += 1
        results.append(baseInterval)
        
        return results
