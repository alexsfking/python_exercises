import math

class Handshakes():
    def __init__(self) -> None:
        max_people=100
        self.handshakes_list=[]
        for i in range(0,max_people+1):
            self.handshakes_list.append(math.comb(i,2)) # pairs

    def get_min(self,handshakes:int)->int:
        for i in range(len(self.handshakes_list)):
            if(handshakes<=self.handshakes_list[i]):
                return i

hs=Handshakes()

def get_participants(handshakes):
    return hs.get_min(handshakes)


print(get_participants(7))