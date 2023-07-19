from collections import deque

class Goblet_queue():
    def __init__(self,num_schools:int) -> None:
        self.num_schools=num_schools
        self.school_queues_list=[]
        for _ in range(num_schools):
            self.school_queues_list.append(deque())

        self.create_lead_tracker()

    # just track the index of the first student in each school
    # and the number of students from each school
    # if 0 new students at the end
    def create_lead_tracker(self,):
        self.school_queue_lead_indexes=[]
        for _ in range(self.num_schools):
            self.school_queue_lead_indexes.append(-1)

        self.number_students_queue_by_school=[]
        for _ in range(self.num_schools):
            self.number_students_queue_by_school.append(0)

    def calculate_lead_index(self,school:int):
        return max(self.school_queue_lead_indexes)+1

    def operation_enqueue(self, operation:str):
        school,roll=map(int,operation[2:].split())
        self.school_queues_list[school].append(roll)
        self.number_students_queue_by_school[school]+=1
        if(self.school_queue_lead_indexes[school]==-1):
            self.school_queue_lead_indexes[school]=self.calculate_lead_index(school)
        
    def decrement_lead_indexes(self):
        for school in range(self.num_schools):
            if(self.school_queue_lead_indexes[school]!=-1):
                self.school_queue_lead_indexes[school]-=1

    def operation_dequeue(self):
        for school in range(self.num_schools):
            if(self.school_queue_lead_indexes[school]==0):
                self.number_students_queue_by_school[school]-=1
                self.school_queues_list[school].popleft()
                if(self.number_students_queue_by_school[school]==0):
                    self.decrement_lead_indexes()
                    return
                    

    def get_front_of_queue(self)->tuple:
        for i in range(self.num_schools):
            if(self.school_queue_lead_indexes[i]==0):
                return((i,self.school_queues_list[i][0]))

q_operations=int(input())
operations=[]
for _ in range(q_operations):
    operations.append(input().strip())

#due to 1 based indexing schools=5 (1-4, 0 isn't used)
goblet_queue=Goblet_queue(5)
for i in range(len(operations)):
    if(operations[i][0:1]=='E'):
        goblet_queue.operation_enqueue(operations[i])
    else:
        print(*goblet_queue.get_front_of_queue())
        goblet_queue.operation_dequeue()