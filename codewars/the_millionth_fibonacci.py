from collections import deque
import sys
sys.set_int_max_str_digits(1_000_000)
import cProfile
import time

closest_multiple_of_100 = lambda x: round(x / 100) * 100

class Fibonacci():
    def __init__(self) -> None:
        self.fib_dict={0:0,1:1,2:1}
        self.last=5000
        self.increment=100
        self.temp_list_size=102
        self.maximum_fib=2000000
        for i in range(3,self.last+1):
            self.fib_dict[i]=self.fib_dict[i-1]+self.fib_dict[i-2]

    def calc_one_hundred(self):
        temp = [0] * 2
        temp[0]=self.fib_dict[self.last-1]
        temp[1]=self.fib_dict[self.last]
        for i in range(2,self.temp_list_size):
            temp.append(temp[-1]+temp[-2])
        self.fib_dict[self.last+self.increment-1]=temp[-2]
        self.fib_dict[self.last+self.increment]=temp[-1]
        self.last+=self.increment

    def calc_backwards(self,closest_mult,n):
        temp=deque()
        temp.append(self.fib_dict[closest_mult])
        temp.append(self.fib_dict[closest_mult-1])
        for _ in range(closest_mult-n):
            temp.append(temp[0]-temp[1])
            temp.popleft()
        return(temp[-1])

    def calc_forwards(self,closest_mult,n):
        temp=deque()
        temp.append(self.fib_dict[closest_mult-1])
        temp.append(self.fib_dict[closest_mult])
        for _ in range(n-closest_mult+1):
            temp.append(temp[0]+temp[1])
            temp.popleft()
        return(temp[-1])

    def get_fib(self,n):
        if(n>self.last):
            while(self.last<n):
                self.calc_one_hundred()
        if(n>-1):
            if(n in self.fib_dict):
                return self.fib_dict[n]
            else:
                closest_mult=closest_multiple_of_100(n)
                if(closest_mult>n):
                    return self.calc_backwards(closest_mult,n)
                else:
                    return self.calc_forwards(closest_mult,n)
        else:
            #negative
            return -self.get_fib(-n) if n % 2 ==0 else self.get_fib(-n)

fibonacci=Fibonacci()

def fib(n):
    return fibonacci.get_fib(n)

def main():
    a=103256
    prev_time = time.time()  # Get the initial time
    for i in range(0,9):
        print(a+a*i," ",hash(fib(a+a*i)))
        current_time = time.time()
        time_elapsed = current_time - prev_time
        print(f"Time elapsed: {time_elapsed:.2f} seconds")
        prev_time = current_time
    for j in range(0,11):
        print(900000+j*10000," ",hash(fib(900000+j*10000)))
        current_time = time.time()
        time_elapsed = current_time - prev_time
        print(f"Time elapsed: {time_elapsed:.2f} seconds")
        prev_time = current_time

if __name__ == "__main__":
    start_time = time.time()
    cProfile.run('main()', sort='cumulative')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total Execution Time: {execution_time:.4f} seconds")
