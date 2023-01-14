#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
from bisect import bisect_left

class Text_Editor():
    def __init__(self):
        self.operations=[]
        self.stack=[]
        self.s=[]
        self.s_cumulative=[]
    
    def add_operation(self, op:list):
        self.operations.append(op)
    
    def num_operations(self)->int:
        return(len(self.operations))
        
    def get_operation(self, op:int)->list:
        if(op<self.num_operations()):
            return(self.operations[op])
        else:
            return []
        
    def append(self,w:str,allow_undo:bool):
        if(self.s_cumulative):
            self.s_cumulative.append(self.s_cumulative[-1]+len(w))
        else:
            self.s_cumulative.append(len(w))
        if(allow_undo):
            self.stack.append(["2",len(w)])
        self.s.append(w)
    
    def delete_k(self,k:int,allow_undo:bool):
        for _ in range(k):
            self.delete(allow_undo)
        
    def delete(self,allow_undo:bool):
        #if(not self.s): return
        while(not len(self.s[-1])):
            self.s.pop()
            self.s_cumulative.pop()
        #if(not self.s): return
        if(allow_undo):
            self.stack.append(["1", self.s[-1]])
        self.s[-1]=self.s[-1][:-1]
        self.s_cumulative[-1]-=1
        if(self.s_cumulative[-1]==0):
            self.s_cumulative.pop()
            self.s.pop()
    
    def print_k(self,k:int):
        index=self.find_lt(k)
        #string=self.s_cumulative[index]
        try:
            print(self.s[index][k-1])
        except Exception as e:
            print(e)
            print(self.s[index],k-1)
    
    def find_lt(self,x:int):
        #rightmost value < x
        #print(self.s_cumulative,x)
        i=bisect_left(self.s_cumulative,int(x))
        if(i):
            return(i-1)
        return 0   
    
    def undo(self,allow_undo:bool):
        op=self.stack.pop()
        if(op[0]=="1"):
            #append
            self.append(op[1],allow_undo)
        elif(op[0]=="2"):
            #delete
            self.delete_k(int(op[1]),allow_undo)
        else:
            raise Exception()
        
        

if __name__ == '__main__':
    q=int(input())
    text_editor=Text_Editor()
    allow_undo=True
    for _ in range(q):
        text_editor.add_operation(input().split())
    for index in range(0,text_editor.num_operations()):
        op=text_editor.get_operation(index)
        if(not op):
            break
        elif(op[0]=="1"):
            #append
            text_editor.append(op[1],allow_undo)
        elif(op[0]=="2"):
            #delete
            text_editor.delete_k(int(op[1]),allow_undo)
        elif(op[0]=="3"):
            #print
            text_editor.print_k(int(op[1]))
        elif(op[0]=="4"):
            #undo
            text_editor.undo(False)
        else:
            raise Exception()
        
