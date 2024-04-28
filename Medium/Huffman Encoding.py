"""
Given a string S of distinct character of size N and their corresponding frequency f[ ] i.e. character S[i] has f[i] frequency. Your task is to build the Huffman tree print all the huffman codes in preorder traversal of the tree.
Note: While merging if two nodes have the same value, then the node which occurs at first will be taken on the left of Binary Tree and the other one to the right, otherwise Node with less value will be taken on the left of the subtree and other one to the right.
"""

import heapq
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def __lt__(self,other):
        return self.data < other.data

class Solution:
    def traverse(self,root,ans,temp):
        if root.left is None and root.right is None:
            ans.append(temp)
            return
        self.traverse(root.left,ans,temp + "0")
        self.traverse(root.right,ans,temp + "1")
        
    def huffmanCodes(self,S,f,N):
        min_heap = []
        
        for i in f:
            heapq.heappush(min_heap,Node(i))
            
        while len(min_heap) > 1:
            left = heapq.heappop(min_heap)
            right = heapq.heappop(min_heap)
            newNode = Node(left.data + right.data)
            newNode.left = left
            newNode.right = right
            heapq.heappush(min_heap,newNode)
            
        root = heapq.heappop(min_heap)
        ans = []
        temp = ""
        self.traverse(root,ans,temp)
        return ans

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S= input()
        N= len(S);
        f= [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.huffmanCodes(S,f,N)
        for i in ans:
            print(i, end = " ")
        print()
