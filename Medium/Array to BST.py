"""Given a sorted array. Convert it into a Height balanced Binary Search Tree (BST). Find the preorder traversal of height balanced BST. If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.
Height balanced BST means a binary tree in which the depth of the left subtree and the right subtree of every node never differ by more than 1.
"""

class Solution:
    def solve(self,nums,st,lst):
        if st>lst:
            return 
        mid=(st+lst)//2
        self.ans.append(nums[mid])
        self.solve(nums,st,mid-1)
        self.solve(nums,mid+1,lst)
        
    def sortedArrayToBST(self, nums):
        st=0
        lst=len(nums)-1
        self.ans=[]
        self.solve(nums,st,lst)
        return self.ans

T=int(input())
for i in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    obj = Solution()
    ans = obj.sortedArrayToBST(nums)
    for _ in ans:
        print(_, end = " ")
    print()
