# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

#queue by using two stacks
class Queue_Stacks:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def enqueue(self,data:int):
        self.s1.append(data)

    def fill_s2(self):
        while(self.s1):
                self.s2.append(self.s1.pop())
        
    def dequeue(self):
        if(self.s2):
            self.s2.pop()
        else:
            self.fill_s2()
            if(self.s2):
                self.s2.pop()
                
    def print_front(self):
        if(self.s2):
            print(self.s2[-1])
        else:
            print(self.s1[0])


if __name__ == '__main__':
    q=int(input())
    queries=[]
    
    for _ in range(q):
        queries.append(list(map(int, input().strip().split())))
        
    queue=Queue_Stacks()
    for qu in queries:
        if(qu[0]==1):
            queue.enqueue(qu[1])
        elif(qu[0]==2):
            queue.dequeue()
        elif(qu[0]==3):
            queue.print_front()
        else:
            raise Exception
    