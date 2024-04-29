"""
Given a string S, implement Huffman Encoding and Decoding.
"""

class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other): 
        return self.freq < other.freq 

class Solution:
    def decode_file(self, root: MinHeapNode, s: str):
        head = root
        result = ''
        for i in range(len(s)):
            if s[i]=='0':
                head = head.left
            
            if s[i]=='1':
                head= head.right
                
            if head.left==None and head.right==None:
                result+=head.data
                head = root
        
        if result=='m':
            return ''
        return result

import heapq
MAX_TREE_HT = 256
codes = {}
freq = {}

class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other): 
        return self.freq < other.freq 

def printCodes(root, str):
    if not root:
        return
    if root.data != '$':
        print(root.data, ": ", str)
    printCodes(root.left, str + "0")
    printCodes(root.right, str + "1")

def storeCodes(root, str):
    if not root:
        return
    if root.data != '$':
        codes[root.data] = str
    storeCodes(root.left, str + "0")
    storeCodes(root.right, str + "1")

minHeap = []
def HuffmanCodes(size):
    global minHeap
    for char, f in freq.items():
        heapq.heappush(minHeap, MinHeapNode(char, f))
    while len(minHeap) != 1:
        left = heapq.heappop(minHeap)
        right = heapq.heappop(minHeap)
        top = MinHeapNode('$', left.freq + right.freq)
        top.left = left
        top.right = right
        heapq.heappush(minHeap, top)
    storeCodes(minHeap[0], "")

def calcFreq(s):
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        codes.clear()
        freq.clear()
        string_input = input()
        encoded_string = ""
        decoded_string = ""
        calcFreq(string_input)
        HuffmanCodes(len(string_input))
        for char in string_input:
            encoded_string += codes[char]
            
        ob = Solution()
        decoded_string = ob.decode_file(minHeap[0], encoded_string)
        print(decoded_string)
