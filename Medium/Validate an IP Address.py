"""
You are given a string str in the form of an IPv4 Address. Your task is to validate an IPv4 Address, if it is valid return true otherwise return false.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1

A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)

Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.
"""

class Solution:
    def isValid(self, ip_address: str) -> bool:
        # Split the IP address by dots
        segments = ip_address.split(".")
       
        # An IP address should have exactly 4 segments
        if len(segments) != 4:
            return False
       
        if ip_address.count('..') >= 1:
            return False
       
        for segment in segments:
            # Convert the segment to an integer
            segment_int = int(segment)
            segment_str = str(segment_int)
           
            # Check if the integer is between 0 and 255 and matches the original segment string
            if not 0 <= segment_int < 256 or segment != segment_str:
                return False
       
        return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")
