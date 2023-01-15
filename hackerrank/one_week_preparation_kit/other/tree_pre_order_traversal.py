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
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

# Complete the preOrder function in the editor below, which has one parameter: 
# a pointer to the root of a binary tree. It must print the values in the tree's 
# preorder traversal as a single line of space-separated values.

class PreOrderSolve():
    def __init__(self):
        self.output=[]
        
    def pre_order(self,node:Node):
        self.output.append(str(node.info))
        if(node.left):
            self.pre_order(node.left)
        if(node.right):
            self.pre_order(node.right)
    
    def get_result(self):
        return self.output   

def preOrder(root):
    #Write your code here
    solution=PreOrderSolve()
    solution.pre_order(root)
    print(" ".join(solution.get_result()))

    


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)