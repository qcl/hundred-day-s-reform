#python2

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        roomsEndTime = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            startTime = interval[0]
            endTime = interval[1]
            foundRoom = False
            for i in range(0, len(roomsEndTime)):
                roomEndTime = roomsEndTime[i]
                if startTime >= roomEndTime:
                    roomsEndTime[i] = endTime
                    foundRoom = True
                    break
            if not foundRoom:
                roomsEndTime.append(endTime)

        return len(roomsEndTime)

