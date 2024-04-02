"""
Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

serialize() : stores the tree into an array a and returns the array.
deSerialize() : deserializes the array to the tree and returns the root of the tree.
Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).
"""

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def serialize(root, A):
    if root==None:
        return A
    q=[root]
    
    while q!=[]:
        currNode=q.pop(0)
        
        if currNode!=None:
            A.append(currNode.data)
        else:
            A.append("#")
        
        if currNode!=None:
            q.append(currNode.left)
            q.append(currNode.right)
    
    return A

def deSerialize(A):
    if len(A)==0:
        return None
    
    if A[0]!="#":
        root=Node(A[0])
    else:
        root=None
    q=[root]
    i=1
    
    while q!=[]:
        node=q.pop(0)
        
        if A[i]!="#":
            node.left=Node(A[i])
            q.append(node.left)
        else:
            node.left=None
        i+=1
        
        if A[i]!="#":
            node.right=Node(A[i])
            q.append(node.right)
        else:
            node.right=None
        i+=1
    return root

from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def buildTree(s):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    q.append(root)
    size = size + 1
    i = 1

    while size > 0 and i < len(ip):
        currNode = q[0]
        q.popleft()
        size = size - 1
        currVal = ip[i]

        if (currVal != "N"):
            currNode.left = Node(int(currVal))
            q.append(currNode.left)
            size = size + 1
        i = i + 1

        if (i >= len(ip)):
            break
        currVal = ip[i]

        if (currVal != "N"):
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root
    
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def _deleteTree(node): 
    if (node == None): 
        return
  
    _deleteTree(node.left) 
    _deleteTree(node.right) 
    node.left=None
    node.right=None
 
def deleteTree(node_ref): 
    _deleteTree(node_ref) 
    node_ref = None
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        A=[]
        serialize(root, A)
        deleteTree(root)
        root = None
        r=deSerialize(A)
        inorder(r)
        print()
