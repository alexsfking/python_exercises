'''
***Chat-GPT***

The given code implements a data structure called the "Goblet Queue," which
manages multiple queues for different schools. Each school has its own queue,
and there is a lead student in each queue whose turn it is to be dequeued. The
Goblet Queue supports two main operations: enqueue and dequeue.

Here's a step-by-step explanation of the code:

    The Goblet_queue class is defined to represent the Goblet Queue. It takes the
    number of schools as input during initialization.

    The Goblet Queue is initialized with the specified number of schools. Separate
    queues are created for each school using the deque data structure from the
    collections module.

    The create_lead_tracker method is used to set up data structures to track the
    lead student in each school's queue and the number of students in each school's
    queue.

    The operation_enqueue method is used to perform the enqueue operation. It adds a
    student to the end of the queue of the specified school. If the school's lead
    index is not set (i.e., no lead student), it calculates the next lead index and
    sets it for that school.

    The decrement_lead_indexes method is called after a dequeue operation. It
    decrements the lead index for all schools that have a lead student.

    The operation_dequeue method is used to perform the dequeue operation. It
    dequeues the lead student from each school's queue, updates the number of
    students in that school, and calls decrement_lead_indexes if necessary.

    The get_front_of_queue method returns a tuple representing the school number and
    the roll (student) number of the lead student at the front of the queue.

    The code takes input for the number of operations and the actual operations to
    be performed on the Goblet Queue. It initializes the Goblet Queue with 5 schools
    and processes each operation accordingly, either enqueueing or dequeueing
    students. If it's a dequeue operation, it prints the lead student's school and
    roll number before dequeuing the student.

Note: The code assumes that the input provided follows the correct format, where
'E' represents an enqueue operation followed by the school number and roll
number, and 'D' represents a dequeue operation. Additionally, the lead student's
index for each school is initialized to -1 when there are no students in the
queue for that school.
'''

from collections import deque

class Goblet_queue():
    def __init__(self,num_schools:int) -> None:
        self.num_schools=num_schools
        self.school_queues_list=[]
        for _ in range(num_schools):
            self.school_queues_list.append(deque())

        self.create_lead_tracker()

    # just track the order of the first student in each school
    # and the number of students from each school
    # if 0 students in lead school after a dequeue
    # decrement each of school_queue_lead_indexes
    def create_lead_tracker(self):
        self.school_queue_lead_indexes=[]
        self.number_students_queue_by_school=[]
        for _ in range(self.num_schools):
            self.school_queue_lead_indexes.append(-1)
            self.number_students_queue_by_school.append(0)

    def calculate_lead_index(self,school:int)->int:
        return max(self.school_queue_lead_indexes)+1

    def operation_enqueue(self, operation:str):
        school,roll=map(int,operation[2:].split())
        self.school_queues_list[school].append(roll)
        self.number_students_queue_by_school[school]+=1
        if(self.school_queue_lead_indexes[school]==-1):
            self.school_queue_lead_indexes[school]=self.calculate_lead_index(school)
        
    def decrement_lead_indexes(self):
        for school in range(1,self.num_schools):
            if(self.school_queue_lead_indexes[school]!=-1):
                self.school_queue_lead_indexes[school]-=1

    def operation_dequeue(self):
        for school in range(1,self.num_schools):
            if(self.school_queue_lead_indexes[school]==0):
                self.number_students_queue_by_school[school]-=1
                self.school_queues_list[school].popleft()
                if(self.number_students_queue_by_school[school]==0):
                    self.decrement_lead_indexes()
                    return
                    

    def get_front_of_queue(self)->tuple:
        for i in range(1,self.num_schools):
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