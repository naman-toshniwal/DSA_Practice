"""
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.
"""

class Solution:
    def minimumPlatform(self,n,arr,dep):
        events = [(arr[i], 'arr') for i in range(n)] + [(dep[i], 'dep') for i in range(n)]
        events = sorted(events)
        platform_needed = 0
        current_platform = 0
        
        for time, event_type in events:
            if event_type == 'arr':
                current_platform += 1
            else:
                current_platform -= 1
            
            platform_needed = max(current_platform, platform_needed)
        return platform_needed

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
