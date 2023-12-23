from datetime import datetime

def timestamp_decorator(our_function):
    def wrapper(*args):
        start_time = datetime.now()
        print(start_time)
        result = our_function(*args)
        end_time = datetime.now()
        print(end_time)
        print(f'Duration: {end_time - start_time}')
        return result
    return wrapper

@timestamp_decorator
def add(alist:list):
    return sum(alist)

list_a = [9999,22,33,-1,55,88,4444444,850424422]

print(add(list_a))