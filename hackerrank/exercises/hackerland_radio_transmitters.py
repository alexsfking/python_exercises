#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

class Transmitters():
    def __init__(self, houses:list, transmitter_range:int):
        self.houses=houses
        self.locations=[] #transmitters house
        self.locations_address=[] #array indicies for transmitter house
        self.transmitter_range=transmitter_range
    
    def set_transmitter(self,house:int):
        self.locations.append(house)
        
    def get_last_transmitter(self)->int:
        return self.locations[-1]
        
    def set_transmitter_index(self,index:int):
        self.locations_address.append(index)    
        
    def get_last_transmitter_index(self)->int:
        return self.locations_address[-1]    
        
    def get_number_houses(self)->int:
        return len(self.houses)
        
    def is_in_range(self,house:int)->bool:
        if(self.get_last_transmitter()<house):
            if(self.get_last_transmitter()+self.transmitter_range>=house):
                return True
        elif(self.get_last_transmitter()>house):
            if(self.get_last_transmitter()-self.transmitter_range<=house):
                return True
        elif(self.get_last_transmitter()==house):
                return True
        return False
    
    def first_index_not_in_range(self)->int:
        for i in range(self.get_last_transmitter_index()+1,self.get_last_transmitter_index()+1+self.transmitter_range*2):
            if(not self.is_in_range(self.houses[i])):
                return i 
    
    def is_transmitter_provide_coverage(self,h_index:int,t_index:int)->bool:
        if(h_index>=t_index):
            raise ValueError("h_index must be less than t_index")
        if(self.houses[h_index]<self.houses[t_index]-self.transmitter_range):
            return False
        return True
                
    def place_transmitter(self)->bool:
        start=self.first_index_not_in_range()
        end=start+1+self.transmitter_range
        if(end>=self.get_number_houses()):
            self.set_transmitter_index(start)
            self.set_transmitter(self.houses[start])
            return False
        for i in range(start+1,end):
            if(not self.is_transmitter_provide_coverage(start,i)):
                self.set_transmitter_index(i-1)
                self.set_transmitter(self.houses[i-1])
                return True
        else:
                self.set_transmitter_index(i-1)
                self.set_transmitter(self.houses[i-1])
                return True           
        
            
    def place_first_transmitter(self)->bool:
        start=0
        end=start+1+self.transmitter_range
        if(end>=self.get_number_houses()):
            self.set_transmitter_index(start)
            self.set_transmitter(self.houses[start])
            return False
        for i in range(start+1,end):
            if(not self.is_transmitter_provide_coverage(start,i)):
                self.set_transmitter_index(i-1)
                self.set_transmitter(self.houses[i-1])
                return True
        else:
                self.set_transmitter_index(i)
                self.set_transmitter(self.houses[i])
                return True
    
    def result(self)->int:
        return len(self.locations)
            
    def calculate(self):
        self.place_first_transmitter()
        while(self.place_transmitter()):
            pass
        print(self.locations)
        return self.result()
        

def hackerlandRadioTransmitters(x, k):
    transmitters = Transmitters(sorted(list(set(x))),k)
    print(transmitters.houses)
    return transmitters.calculate()        
        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    #fptr.write(str(result) + '\n')

    #fptr.close()
