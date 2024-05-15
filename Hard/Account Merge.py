"""
Given a list of accounts of size n where each element accounts [ i ] is a list of strings, where the first element account [ i ][ 0 ]  is a name, and the rest of the elements are emails representing emails of the account.
Geek wants you to merge these accounts. Two accounts belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts have the same name.
After merging the accounts, return the accounts in the following format: The first element of each account is the name, and the rest of the elements are emails in sorted order.

Note: Accounts themselves can be returned in any order.
"""

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def findparent(self, nod):
        if self.parent[nod] != nod:
            self.parent[nod] = self.findparent(self.parent[nod])
        return self.parent[nod]

    def unionbysize(self, u, v):
        u_par = self.findparent(u)
        v_par = self.findparent(v)

        if u_par == v_par:
            return

        if self.size[u_par] < self.size[v_par]:
            self.parent[u_par] = v_par
            self.size[v_par] += self.size[u_par]
        else:
            self.parent[v_par] = u_par
            self.size[u_par] += self.size[v_par]


class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        ds = DisjointSet(n)
        merge_email_nod = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]

                if mail not in merge_email_nod:
                    merge_email_nod[mail] = i
                else:
                    ds.unionbysize(merge_email_nod[mail], i)

        merge_email = {}
        for mail, node in merge_email_nod.items():
            root_node = ds.findparent(node)
            if root_node not in merge_email:
                merge_email[root_node] = []
            merge_email[root_node].append(mail)

        ans = []
        for i in range(n):
            if i not in merge_email:
                continue
            merge_email[i].sort()
            name = accounts[i][0]
            temp = [name] + merge_email[i]
            ans.append(temp)
        return ans

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
