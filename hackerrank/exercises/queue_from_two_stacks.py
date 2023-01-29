# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

# In this challenge, you must first implement a queue using two stacks.
# Then process q queries, where each query is one of the following 3 types:
# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.

class Queue:
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
        
    def enqueue(self,data:int):
        self.stack_in.append(data)
    
    def dequeue(self):
        if(not self.stack_out):
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if(self.stack_out):    
            return self.stack_out.pop()
        return
    
    def first(self):
        if(not self.stack_out):
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        print(self.stack_out[-1])
            

if __name__ == '__main__':
    q=int(input())
    operations=[]
    queue=Queue()
    for _ in range(q):
        operations.append(list(map(int, input().split())))
    for o in operations:
        #print(o)
        if(o[0]==1):
            #enqueue
            queue.enqueue(o[1])
        elif(o[0]==2):
            #dequeue
            queue.dequeue()
        elif(o[0]==3):
            #print first element
            queue.first()