#!/bin/python3
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Implement a simple text editor. The editor initially contains an empty string, S. 
# Perform Q operations of the following 4 types:
# 1     append - Append string W to the end of S.
# 2     delete - Delete the last k characters of S.
# 3     print - Print the kth character of S.
# 4     undo - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

class Text_Editor():
    def __init__(self):
        self.operations=[]
        self.stack=[]
        self.s=[]
    
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
        if(allow_undo):
            self.stack.append(["2",len(w)])
        for c in w:
            self.s.append(c)
        
    
    def delete_k(self,k:int,allow_undo:bool):
        if(allow_undo):
            out=[]
            for _ in range(k):
                out.append(self.__delete())
            self.stack.append(["1","".join(out[::-1])])
        else:
            for _ in range(k):
                self.__delete()
        
    def __delete(self)->str:
        #if(not self.s): return
        return self.s.pop()
    
    def print_k(self,k:int):
        #string=self.s_cumulative[index]
        print(self.s[k-1])
    
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
        
