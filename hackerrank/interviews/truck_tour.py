"""
Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0
to (N-1) (both inclusive). You have two pieces of information corresponding to each of the
petrol pump: (1) the amount of petrol that particular petrol pump will give, and (2) the
distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at 
any of the petrol pumps. Calculate the first point from where the truck will be able to
complete the circle. Consider that the truck will stop at each of the petrol pumps. The truck
will move one kilometer for each litre of the petrol.
"""

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#
def first(elem):
    return elem[0]

def calculate(petrolpumps:list,index:int)->bool:
    i=index
    petrol=0
    length=len(petrolpumps)
    while(i!=index-1):
        petrol=petrol+(petrolpumps[i][0]-petrolpumps[i][1])
        if(petrol<0):
            return False
        i+=1
        if(i==length):
            i=0
    petrol=petrol+(petrolpumps[i][0]-petrolpumps[i][1])
    if(petrol<0):
        return False
    return True

 
 
def truckTour(petrolpumps):
 # Write your code here
 for i in range(len(petrolpumps)):
    if(petrolpumps[i][0]>=petrolpumps[i][1]):
        if(calculate(petrolpumps,i)):
            return(i)
 raise Exception
