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

"""
***Chat-GPT***
This code defines two classes, `Node` and `BinarySearchTree`. The `Node` class
represents a single node in a binary tree, and the `BinarySearchTree` class
represents the entire binary search tree. 

The `preOrder` function takes a pointer to the root node of a binary tree as its
input and prints the values in the tree's preorder traversal as a single line of
space-separated values.

The preorder traversal of a binary tree visits the root node first, followed by
the left subtree, and then the right subtree. The `preOrder` function uses a
stack to keep track of the nodes that still need to be visited. It initializes
the stack with the root node and then enters a loop.

In each iteration of the loop, the function pops the top node from the stack,
appends its value to an output list, and then checks if it has a right child or
a left child. If it has a right child, the right child is added to the stack,
and if it has a left child, the left child is added to the stack. 

The loop continues until the stack is empty, which means all the nodes in the
tree have been visited. Finally, the function joins the output list using a
space separator and prints it to the console.

The `BinarySearchTree` class has a `create` method that takes a value as input
and adds it to the binary search tree. If the root node is None, the new node
becomes the root node. If the value is less than the current node's value, it
moves to the left subtree. If the value is greater than the current node's
value, it moves to the right subtree. The `create` method continues until it
finds an empty spot to insert the new node.
"""

def preOrder(root):
    #Write your code here
    stack=[root]
    out=[]
    while(stack):
        node=stack.pop()
        out.append(node.info)
        if(node.right):
            stack.append(node.right)
        if(node.left):
            stack.append(node.left)
    print(" ".join(map(str,out)))


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)