#!/bin/python3

import math
import os
import random
import re
import sys

'''
***Chat-GPT***
This Python script is a solution to a problem in Hackerrank called "No Prefix
Set". The problem statement asks to determine whether a given set of words can
be represented without any prefix. A prefix is a sequence of characters at the
beginning of a word that can be extended to form another word in the set.

The script defines two classes, `Node` and `Trie_Root`, and two functions,
`word_to_nodes` and `noPrefix`, which work together to solve the problem.

The `Node` class represents a node in a trie data structure, which is used to
efficiently store and search for strings. Each node contains a character, a
dictionary of edges to other nodes, and a flag indicating whether it represents
the end of a word. The class has the following methods:

- `__init__(self, character:str)`: Constructor method that creates a new node
  with the given character and initializes its properties.
- `get_character(self)->str`: Method that returns the character of the node.
- `add_edge(self, node:'Node')`: Method that adds an edge to the given node to
  the dictionary of edges of the current node.
- `get_edge(self, character:str)->'Node'`: Method that returns the node pointed
  to by the edge with the given character.
- `is_terminating(self)->bool`: Method that returns True if the node represents
  the end of a word.
- `set_terminating(self)`: Method that sets the flag indicating that the node
  represents the end of a word.

The `Trie_Root` class represents the root of a trie data structure. It contains
a dictionary of edges to nodes. The class has the following methods:

- `__init__(self)`: Constructor method that initializes the dictionary of edges.
- `add_edge(self,node:Node)`: Method that adds an edge to the given node to the
  dictionary of edges of the root.
- `get_edge(self, character:str)->Node`: Method that returns the node pointed to
  by the edge with the given character.

The `word_to_nodes` function takes a `Trie_Root` object and a word string as
inputs and adds the characters of the word to the trie as nodes. If a node
already exists for a character, it is used, and if not, a new node is created.
If a node representing the end of a word is encountered, the function returns
True, indicating that the word is a prefix of another word in the set. The
function returns False if the word is successfully added to the trie without
being a prefix of another word. The function has the following steps:

- Initialize a `Node` variable `node` to the node in the trie representing the
  first character of the word. If the node doesn't exist, create it and add it
  to the root of the trie.
- Loop through the remaining characters of the word:
    - If the current node represents the end of a word, return True.
    - Get the node pointed to by the edge with the current character. If the node
    doesn't exist, create it and add it to the current node.
    - Set `node` to the next node.
- If the current node represents the end of a word or was already seen before,
  return True. Otherwise, set the flag indicating that the node represents the
  end of a word and return False.

The `noPrefix` function takes a list of word strings as input and checks if each
word is a prefix of another word in the set by calling the `word_to_nodes`
function for each word. If a word is found to be a prefix of another word, the
function prints "BAD SET" and the offending word, and returns. Otherwise, the
function prints "GOOD SET".
'''

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class Node:
    def __init__(self, character:str):
        self.__character:str=character
        self.__edges:dict[str, 'Node']=dict()
        self.__terminating:bool=False

    def get_character(self)->str:
        return self.__character

    def add_edge(self, node:'Node'):
        self.__edges[node.get_character()]=node

    def get_edge(self, character:str)->'Node':
        return self.__edges.get(character)

    def is_terminating(self)->bool:
        return self.__terminating
    
    def set_terminating(self):
        self.__terminating=True

class Trie_Root:
    def __init__(self):
        self.__edges:dict[str, 'Node']=dict()
    
    def add_edge(self,node:Node):
        self.__edges[node.get_character()]=node

    def get_edge(self, character:str)->Node:
        return self.__edges.get(character)

def word_to_nodes(root:Trie_Root, word:str)->bool:
    node:Node=root.get_edge(word[0:1])
    seen_before:bool=True
    if(node==None):
        node=Node(word[0:1])
        root.add_edge(node)
        seen_before=False
    for i in range(1,len(word)):
        if(node.is_terminating()):
            return True
        next_node:Node=node.get_edge(word[i:i+1])
        if(next_node==None):
            next_node=Node(word[i:i+1])
            node.add_edge(next_node)
            seen_before=False
        node=next_node
    if(node.is_terminating() or seen_before):
        return True
    node.set_terminating()
    return False


def noPrefix(words:list[str])->None:
    # Write your code here
    root:Trie_Root=Trie_Root()
    for word in words:
        if(word_to_nodes(root, word)):
            print("BAD SET")
            print(word)
            return   
        
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
