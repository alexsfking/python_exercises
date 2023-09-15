import re

class SimpleAssembler():
    def __init__(self,instructions:list) -> None:
        index:int=0
        self.registers=dict()
        self.valid_int_pattern = re.compile(r'^[+-]?\d+$')
        while(index<len(instructions)):
            match instructions[index][:3]:
                case "mov":
                    self.mov(instructions[index][4:])
                case "inc":
                    self.inc(instructions[index][4])
                case "dec":
                    self.dec(instructions[index][4])
                case "jnz":
                    index=self.jnz(index,instructions[index][4:])
            index+=1

    def inc(self,register:str)->None:
        self.registers[register]+=1

    def dec(self,register:str)->None:
        self.registers[register]-=1

    def mov(self,instruction:str)->None:
        register,register_or_constant=instruction.split()
        if(self.is_valid_int(register_or_constant)):
            self.registers[register]=int(register_or_constant)
        else:
            self.registers[register]=self.registers[register_or_constant]

    def jnz(self,index,instruction:str)->int:
        register_or_constant_x,register_or_constant_y=instruction.split()
        if(self.is_valid_int(register_or_constant_x)):
            if(int(register_or_constant_x)==0):
                return index
        elif(self.registers[register_or_constant_x]==0):
            return index
        if(self.is_valid_int(register_or_constant_y)):
            index+=int(register_or_constant_y)-1
        else:
            index+=self.registers[register_or_constant_y]-1
        return index

    def is_valid_int(self,s:str)->bool:
        return bool(self.valid_int_pattern.match(s))

def simple_assembler(program:list)->dict:
    assembler=SimpleAssembler(program)
    return assembler.registers