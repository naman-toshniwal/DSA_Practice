"""
You have n stacks of books. Each stack of books has some nonzero height arr[i] equal to the number of books on that stack ( considering all the books are identical and each book has a height of 1 unit ). In one move, you can select any number of consecutive stacks of books such that the height of each selected stack of books arr[i] <= k. Once such a sequence of stacks is chosen, You can collect any number of books from the chosen sequence of stacks.
What is the maximum number of books that you can collect this way?
"""


class Solution:
    def max_Books(self, n, k, arr):
        n = len(arr)
        start = 0
        curr_sum = 0
        max_books = 0
        
        for i in range(n):
            if arr[i]<=k:
                curr_sum +=arr[i]
                max_books = max(max_books, curr_sum)
            else:
                curr_sum = 0
                start = i + 1

        return max_books

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
