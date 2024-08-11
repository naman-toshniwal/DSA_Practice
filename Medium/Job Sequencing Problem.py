"""
Given a set of n jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with a job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job. Deadline of the job is the time on or before which job needs to be completed to earn the profit.
"""

'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    def JobScheduling(self, Jobs, n):
        
        # Sorting jobs by decreasing order of profit
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Finding the maximum deadline to create a timeline
        max_deadline = max(job.deadline for job in Jobs)
        
        # Timeline to keep track of free slots (initialized to None)
        timeline = [None] * (max_deadline + 1)
        
        job_count = 0
        max_profit = 0
        
        # Iterating over each job
        for job in Jobs:
            # Try to find a slot from job.deadline to 1
            for t in range(job.deadline, 0, -1):
                if timeline[t] is None:
                    # Slot found, schedule the job
                    timeline[t] = job.id
                    job_count += 1
                    max_profit += job.profit
                    break
        
        return job_count, max_profit

import atexit
import io
import sys

class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])
