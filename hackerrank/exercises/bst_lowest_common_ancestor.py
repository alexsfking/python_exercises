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

'''
You are given pointer to the root of the binary search tree and two values v1
and v2. You need to return the lowest common ancestor (LCA) of v1 and v2 in the
binary search tree.

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

from queue import Queue

def modify_tree(root:Node)->dict[int, Node]:
    queue=Queue()
    queue.put(root)
    root.ancestor=None
    root.level=0
    value_to_node_dict=dict()
    while(not queue.empty()):
        node:Node=queue.get()
        value_to_node_dict[node.info]=node
        if(node.left):
            node.left.ancestor=node
            node.left.level=node.level+1
            queue.put(node.left)
        if(node.right):
            node.right.ancestor=node
            node.right.level=node.level+1
            queue.put(node.right)
    return value_to_node_dict

def lca(root, v1, v2)->Node:
    #Enter your code here
    value_to_node_dict:dict[int, Node]=modify_tree(root)
    node1:Node=value_to_node_dict[v1]
    node2:Node=value_to_node_dict[v2]
    while(node1.level<node2.level):
        node2=node2.ancestor
    while(node2.level<node1.level):
        node1=node1.ancestor
    while(node1!=node2):
        node1=node1.ancestor
        node2=node2.ancestor
    return node1


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
