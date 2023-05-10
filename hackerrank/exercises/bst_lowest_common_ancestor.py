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


def find_ancestor(ancestors_dict:dict,v1,v2):
    if(ancestors_dict[v1] != None):
        v1_current_set:set=ancestors_dict[v1]
        v1_set=v1_current_set.copy()
    else:
        return v1
    if(ancestors_dict[v2] != None):
        v2_current_set:set=ancestors_dict[v2]
        v2_set=v2_current_set.copy()
    else:
        return v2

    while(len(v1_current_set) or len(v2_current_set)):
        if(v1_set.intersection(v2_set)):
            return max(v1_set.intersection(v2_set))
        else:
            temp_set=set()
            for i in v1_current_set:
                if(ancestors_dict[i]!=None):
                    temp_set.update(ancestors_dict[i])
            v1_current_set=temp_set
            temp_set=set()
            for i in v2_current_set:
                if(ancestors_dict[i]!=None):
                    temp_set.update(ancestors_dict[i])
            v2_current_set=temp_set

            v1_set=v1_set.union(v1_current_set)
            v2_set=v2_set.union(v2_current_set)
    return None

def lca(root, v1, v2):
    #Enter your code here
    ancestors_dict=dict()
    stack=[root]
    ancestors_dict[root]=None
    node_value_dict=dict()
    while(stack):
        node:Node=stack.pop()
        node_value_dict[node.info]=node
        if(node.right):
            stack.append(node.right)
            if(node.right in ancestors_dict):
                ancestors_dict[node.right].add(node)
            else:
                ancestors_dict[node.right]={node}
        if(node.left):
            stack.append(node.left)
            if(node.left in ancestors_dict):
                ancestors_dict[node.left].add(node)
            else:
                ancestors_dict[node.left]={node}
    out=find_ancestor(ancestors_dict,node_value_dict[v1],node_value_dict[v2])
    if(out==None):
        return root
    else:
        return out


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
