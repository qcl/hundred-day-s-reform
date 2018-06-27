class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        taskCount = {}
        for task in tasks:
            if not task in taskCount:
                taskCount[task] = 0
            taskCount[task] += 1
        taskCount = sorted(taskCount.values())

        time = 0
        while taskCount[-1] > 0:
            i = 0
            while i <= n:
                if taskCount[-1] == 0:
                    break;
                if i < len(taskCount) and taskCount[-1-i] > 0:
                    taskCount.insert(len(taskCount)-1-i, taskCount.pop(len(taskCount)-1-i) - 1)
                i+=1
                time+=1
            taskCount = sorted(taskCount)

        return time
        
