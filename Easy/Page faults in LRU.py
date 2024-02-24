"""
In operating systems that use paging for memory management, page replacement algorithm is needed to decide which page needs to be replaced when the new page comes in. Whenever a new page is referred and is not present in memory, the page fault occurs and Operating System replaces one of the existing pages with a newly needed page.

Given a sequence of pages in an array pages[] of length N and memory capacity C, find the number of page faults using Least Recently Used (LRU) Algorithm. 

Note:- Before solving this example revising the OS LRU cache mechanism is recommended.
"""

class Solution:
    def pageFaults(self, N, C, pages):
        queue = []
        fault = 0
        
        for i in pages:
            if i not in queue:
                if len(queue) > 0 and len(queue) >= C:
                    queue.pop(0)
                queue.append(i)
                fault += 1
            else:
                queue.remove(i)
                queue.append(i)
                
        return fault

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        pages = input().split()
        for itr in range(N):
            pages[itr] = int(pages[itr])
        C = int(input())

        ob = Solution()
        print(ob.pageFaults(N, C, pages))
