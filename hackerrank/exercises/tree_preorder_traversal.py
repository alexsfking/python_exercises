class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Complete the preOrder function in the editor below, which has 1 parameter: a
pointer to the root of a binary tree. It must print the values in the tree's
preorder traversal as a single line of space-separated values.

Input Format
Our test code passes the root node of a binary tree to the preOrder function.

Constraints
1 <= Nodes in the tree <= 500

Output Format
Print the tree's preorder traversal as a single line of space-separated values.
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    #Write your code here
    visited=set()
    stack=[]
    out=[]
    stack.append(root)
    while(stack):
        if(stack[-1] not in visited):
            out.append(stack[-1].info)
            visited.add(stack[-1])
        if(stack[-1].left and stack[-1].left not in visited):
            stack.append(stack[-1].left)
        elif(stack[-1].right and stack[-1].right not in visited):
            stack.append(stack[-1].right)
        else:
            stack.pop()
    print(" ".join(map(str,out)))


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)