#!/bin/python3

import math
import os
import random
import re
import sys

"""
There is a given list of strings where each string contains only lowercase letters from a-j, inclusive.
The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, 
print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

Note if two strings are identical, they are prefixes of each other.
"""


#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class Node:
    def __init__(self, letter:str,level:int):
        self.nodes=dict()
        self.letter=letter
        self.level=level
        self.terminated=False
        
    def is_empty(self):
        if self.nodes:
            return False
        return True
    
    def is_leaf(self):
        if(self.terminated):
            return True
        return False
    
    def set_terminated(self):
        self.terminated=True
    
    def is_edge_in_dict(self, letter:str):
        if(letter in self.nodes):
            return True
        return False
        
    def get_edge_node(self, letter:str):
        return self.nodes[letter]
    
    def set_edge_node(self, letter:str,level:int):
        self.nodes[letter]=Node(letter, level)
        
    def get_letter(self):
        return self.letter
    
    def get_level(self):
        return self.level
    
        
class Node_Tree:
    def __init__(self):
        self.nodes=dict()
        self.exit_word=""
    
    def build_tree(self,words)->bool:
        for word in words:
            if(self.add_word(word)):
                return True
        return False

    def generate_roots(self,letter:str)->Node:
        i=0
        if(letter not in self.nodes):
            self.nodes[letter]=Node(letter,i)
        node=self.nodes[letter]
        return node
                
    def add_word(self,word:str)->bool:
        node=self.generate_roots(word[0])

        #generate edges
        for i in range(1,len(word)):
            if(node.is_leaf()):
                #bad set prev_word=abc word=abcd
                self.exit_word=word
                return True
            if(not node.is_edge_in_dict(word[i])):
                node.set_edge_node(word[i],i)
            node=node.get_edge_node(word[i])

        #set leaf nodes
        if(not node.is_leaf()):
            node.set_terminated()
        else:
            #bad set prev_word=a word=a
            self.exit_word=word
            return True
        
        #check current word isn't a prefix to a prev word
        if(not node.is_empty()):
            #bad set prev_word=abcd word=abc
            self.exit_word=word
            return True
        return False

        
def noPrefix(words):
    # Write your code here
    node_tree=Node_Tree()
    if(node_tree.build_tree(words)):
        print("BAD SET")
    else:
        print("GOOD SET")
    print(node_tree.exit_word)
        

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
