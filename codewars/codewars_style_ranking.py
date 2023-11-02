# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User:
    def __init__(self) -> None:
        self.rank_index=0
        self.available_ranks=[-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.inital_progress=0
        self.progress_threshold=100
        self.set_rank()
        self.progress=self.inital_progress
    
    def set_rank(self):
        self.rank=self.available_ranks[self.rank_index]

    def inc_progress(self, rank:int):
        #print(rank,':',self.rank,self.rank_index,self.progress)
        if(rank<self.available_ranks[0] or rank>self.available_ranks[-1] or rank==0):
            raise NotImplementedError
        if(self.rank_index==len(self.available_ranks)-1):
            self.progress=0
            return
        
        rank_difference=self.available_ranks.index(self.rank)-self.available_ranks.index(rank)
        if(rank_difference<0):
            self.progress+=10*pow(rank_difference,2)
        elif(rank_difference==0):
            self.progress+=3
        elif(rank_difference==1):
            self.progress+=1
        while(self.progress>=self.progress_threshold):
            if(self.rank_index==len(self.available_ranks)-1):
                self.progress=0
                self.set_rank()
                return
            self.rank_index+=1
            self.progress-=self.progress_threshold
        if(self.rank_index==len(self.available_ranks)-1):
            self.progress=0
        self.set_rank()

