#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class Node:
    def __init__(self, character:str):
        self.__character=character
        self.__edges:dict[str, 'Node']=dict()
        self.__terminating=False

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

#if
def word_to_nodes(root:Trie_Root, word:str)->bool:
    node=root.get_edge(word[0:1])
    seen_before=True
    if(node==None):
        node=Node(word[0:1])
        root.add_edge(node)
        seen_before=False
    for i in range(1,len(word)):
        if(node.is_terminating()):
            return True
        next_node=node.get_edge(word[i:i+1])
        if(next_node==None):
            next_node=Node(word[i:i+1])
            node.add_edge(next_node)
            seen_before=False
        node=next_node
    if(node.is_terminating() or seen_before):
        return True
    node.set_terminating()
    return False


def noPrefix(words)->None:
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
