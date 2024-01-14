'''
### kyu 6 ###
There is a queue for the self-checkout tills at the supermarket. Your task is
write a function to calculate the total time required for all the customers to
check out!

Input
customers: an array of positive integers representing the queue. Each integer
represents a customer, and its value is the amount of time they require to check
out.
n: a positive integer, the number of checkout tills.

Output
The function should return an integer, the total time required.

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12

Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list)
proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified
above.

P.S. The situation in this kata can be likened to the
more-computer-science-related idea of a thread pool, with relation to running
multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
'''

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls +=1
        return func(*args, **kwargs)
    
    wrapper.calls = 0

    def get_call_count():
        return wrapper.calls
    
    wrapper.get_call_count = get_call_count
    return wrapper
    

class Supermarket_Queue:
    def __init__(self, customer_times:list[int], n_tills:int) -> None:
        self.customer_times = customer_times[::-1]
        self.n_tills = n_tills
        self.tills_list = [Till() for _ in range(n_tills)]

    def allocate_customers(self):
        for till in self.tills_list:
            if till.is_free() and len(self.customer_times):
                till.new_customer(self.customer_times.pop())

    @count_calls
    def move_time_forward(self):
        for till in self.tills_list:
            till.decrement_time()

    def start_day(self):
        while len(self.customer_times):
            self.allocate_customers()
            self.move_time_forward()

class Till:
    def __init__(self, transaction_time:int = 0) -> None:
        self.transaction_time = transaction_time
    
    def is_free(self) -> bool:
        if self.transaction_time > 0:
            return False
        return True
        
    def new_customer(self, transaction_time:int):
        self.transaction_time = transaction_time

    def decrement_time(self):
        self.transaction_time -= 1

def queue_time(customer_times:list[int], n_tills:int) -> int:
    supermarket = Supermarket_Queue(customer_times, n_tills)
    supermarket.start_day()
    return supermarket.move_time_forward.get_call_count()

print(queue_time([1,2,3,4,5], 1) == 15)
print(queue_time([1,2,3,4,5], 5) == 5)