import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()

    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

"""
Huffman coding assigns variable length codewords to fixed length input
characters based on their frequencies. More frequent characters are assigned
shorter codewords and less frequent characters are assigned longer codewords.
All edges along the path to a character contain a code digit. If they are on the
left side of the tree, they will be a 0 (zero). If on the right, they'll be a 1
(one). Only the leaves will contain a letter and its frequency count. All other
nodes will contain a null instead of a character, and the count of the frequency
of all of it and its descendant characters.

Example 

A - 0
B - 111
C - 1100
D - 1101
R - 10

'0'    : 'A'
'111'  : 'B'
'1100' : 'C'
'1101' : 'D'
'10'   : 'R'

A B    R  A C     A D     A B    R  A
0 111 10 0 1100 0 1101 0 111 10 0
or
01111001100011010111100
"""

"""
***Chat-GPT***
The provided code is an implementation of the Huffman coding algorithm. The
algorithm generates a binary tree that assigns variable length codes to
characters based on their frequencies. The more frequent characters are assigned
shorter codes, and less frequent characters are assigned longer codes.

The code first reads an input string and calculates the frequency of each
character in the input string. Then, it builds a Huffman tree using the priority
queue data structure from the queue module. The tree's construction is done by
iteratively taking the two lowest frequency nodes and creating a new parent node
with the combined frequency. The parent node's left and right children are set
to the two nodes selected. This process continues until a single node, which is
the root of the Huffman tree, remains in the priority queue.

The dfs_hidden function performs a depth-first search of the Huffman tree and
generates a dictionary that maps each character in the input string to its
corresponding Huffman code.

The decodeHuff function takes the Huffman tree's root node and a string of
Huffman codes as input. It first generates a dictionary that maps each Huffman
code to its corresponding character in the Huffman tree by performing a
depth-first search of the tree and keeping track of each node's Huffman code
using a stack data structure. Then, it decodes the Huffman code string into the
original input string by iteratively checking whether the current substring is a
valid Huffman code in the dictionary. If it is, the corresponding character is
appended to the output string, and the start and end indices of the substring
are updated accordingly.

Overall, the code implements the Huffman coding algorithm and demonstrates how
it can be used to encode and decode input strings.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import string

def decodeHuff(root, s):
    #Enter Your Code Here
    #generate a dict of huffman codes
    stack=[root]
    character_set=set(string.printable)
    root.huff=""
    huff_dict=dict()
    while(stack):
        node=stack.pop()
        if(node.data in character_set):
            huff_dict[node.huff]=node.data
        if(node.left):
            stack.append(node.left)
            node.left.huff=node.huff+"0"
        if(node.right):
            stack.append(node.right)
            node.right.huff=node.huff+"1"
    
    #decode string into the input string assumes valid
    start_index=0
    end_index=1
    out=[]
    while(end_index<len(s)):
        if(s[start_index:end_index] in huff_dict):
            out.append(huff_dict[s[start_index:end_index]])
            start_index=end_index
            end_index=start_index+1
        else:
            end_index+=1
    if(start_index<len(s) and s[start_index:] in huff_dict):
        out.append(huff_dict[s[start_index:]])
    print("".join(out))
        

ip = input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
