"""
Given a dictionary of distinct words and an M x N board where every cell has one character. Find all possible words from the dictionary that can be formed by a sequence of adjacent characters on the board. We can move to any of 8 adjacent characters

Note: While forming a word we can move to any of the 8 adjacent cells. A cell can be used only once in one word.
"""

class Solution:
    def wordBoggle(self,board,dictionary):
        n = len(board)
        m = len(board[0])
        
        def dfs(cr , cc , ind , word):
            if word in result:
                return False
            
            if board[cr][cc] != word[ind]:
                return False
                
            elif ind+1 == len(word):
                return True
            
            curChar = board[cr][cc]
            board[cr][cc] = '_'
            
            neigh = [(cr-1 , cc) , (cr-1 , cc+1) , (cr , cc+1) , (cr+1 , cc+1) , (cr+1 , cc),
                     (cr+1 , cc-1) , (cr , cc-1) , (cr-1 , cc-1)]
                     
            for nr , nc in neigh:
                if 0<=nr<n and 0<=nc<m and board[nr][nc]!='_':
                    if dfs(nr , nc , ind+1 , word):
                        board[cr][cc] = curChar  
                        return True

            board[cr][cc] = curChar            
            return False
        result = set()
        
        for word in dictionary:
            for i in range(n):
                for j in range(m):
                    if dfs(i , j , 0 , word):
                        result.add(word)
        return list(result)

if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        N=int(input())
        dictionary=[x for x in input().strip().split()]
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        board=[]
        for _ in range(R):
            board.append( [x for x in input().strip().split()] )
        obj = Solution()
        found = obj.wordBoggle(board,dictionary)
        if len(found) is 0:
            print(-1)
            continue
        found.sort()
        for i in found:
            print(i,end=' ')
        print()
