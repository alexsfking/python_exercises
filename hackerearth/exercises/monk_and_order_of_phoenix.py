'''
Voldemort has a big army, so he has maintained his people in N rows to fight
Harry's army. Each row contains the heights of the fighters and is sorted in
non-decreasing order from the start to end, except for the first row, which may
contain the heights of the fighters in any arbitary order, as it contains all
the legendry fighters.

During the war, at any time, Voldemort can remove a fighter from any row, and
can also add any new fighter to any row (maintaining the non-decreasing order of
heights. except in the first row).
'''

class Army():
    def __init__(self) -> None:
        self.get_inputs()
        self.perform_operations()

    def get_inputs(self):
        self.n_number_of_stacks=int(input())
        self.heights_of_fighters:list[list[int]]=[]
        self.x_size_of_the_stack=[]
        for i in range(self.n_number_of_stacks):
            self.heights_of_fighters.append(list(map(int,input().split())))
            self.x_size_of_the_stack.append(self.heights_of_fighters[i].pop(0))
        self.q_number_of_operations=int(input())
        self.operations=[]
        for _ in range(self.q_number_of_operations):
            line=list(map(int,input().split()))
            self.operations.append(line)

    def perform_operations(self):
        for operation in self.operations:
            v=operation[0]
            if(v==0):
                self.operation_zero(operation[1])
            elif(v==1):
                self.operation_one(operation[1],operation[2])
            elif(v==2):
                self.operation_two()
            else:
                raise Exception

    #remove last fighter from kth stack
    def operation_zero(self,k:int):
        self.heights_of_fighters[k-1].pop()

    # insert one fighter in the kth stack, maintaining order if k!=1
    def operation_one(self,k:int,h:int):
        k-=1
        if(k==0):
            self.heights_of_fighters[k].append(h)
        else:
            left = 0
            right = len(self.heights_of_fighters[k]) - 1

            # Binary search to find the insertion position
            while left <= right:
                mid = (left + right) // 2
                if self.heights_of_fighters[k][mid] == h:
                    # If the number already exists, insert it after the last occurrence
                    while mid < len(self.heights_of_fighters[k]) and self.heights_of_fighters[k][mid] == num:
                        mid += 1
                    self.heights_of_fighters[k].insert(mid, h)
                    return
                elif self.heights_of_fighters[k][mid] < h:
                    left = mid + 1
                else:
                    right = mid - 1

            # If the number is not found, insert it at the appropriate position
            self.heights_of_fighters[k].insert(left, h)
            return

    def operation_two(self):
        temp=-1
        for i in range(self.n_number_of_stacks):
            if(self.n_number_of_stacks<=len(self.heights_of_fighters[i])):
                smallest=float('inf')
                for j in range(len(self.heights_of_fighters[i])):
                    if(self.heights_of_fighters[i][j]>temp and self.heights_of_fighters[i][j]<smallest):
                        smallest=self.heights_of_fighters[i][j]
                if(smallest!=float('inf')):
                    temp=smallest
                else:
                    print("NO")
                    return
            else:
                print("NO")
                return
        print("YES")
        return

voldemorts_army=Army()


