class SmartTrafficLight:
    def __init__(self, st1:tuple, st2:tuple):
        self.order=[]
        if(st1[0]==st2[0]):
            return
        self.order.append(st2[1])
        self.order.append(st1[1])
        if(st1[0]<st2[0]):
            self.order.reverse()
        
    def turngreen(self):
        if(len(self.order)>0):
            return self.order.pop()
        else:
            return None