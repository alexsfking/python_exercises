import re

class SimpleAssembler():
    def __init__(self,instructions:list[str]) -> None:
        self.registers_dict=dict()
        self.labels_dict=dict()
        self.valid_int_pattern = re.compile(r'^[+-]?\d+$')
        self.label_pattern = re.compile(r'^[^\s]+:$')
        self.instruction_set = {
            "mov": self.mov,
            "inc": self.inc,
            "dec": self.dec,
            "add": self.add,
            "sub": self.sub,
            "mul": self.mul,
            "div": self.div,
            "jmp": self.jmp,
            "cmp": self.cmp,
            "je": self.je,
            "jge": self.jge,
            "jg": self.jg,
            "jle": self.jle,
            "jl": self.jl,
            "ret": self.ret,
            "msg": self.msg,
            "end": self.end,
            "call": self.call,
        }
        self.parse_instructions(instructions)

    def parse_instructions(self,instructions:list[str]):
        index:int=0
        while(index<len(instructions)):
            return_string,return_value=self.parse_instruction(instructions[index],index)
            if(return_string or return_value):
                match return_string:
                    case 'jmp':
                        index=self.labels_dict[return_value]-1
                    case 'cmp':
                        compare=return_value
                        raise NotImplementedError
                    case 'call':
                        raise NotImplementedError
                    case 'ret':
                        raise NotImplementedError
            index+=1

    def parse_instruction(self,instruction:str,index):
        if not instruction or instruction.startswith(';'):
            return index
        parts=instruction.split()
        if(len(parts)<2):
            if(len(parts)==1 and self.is_label(parts[0])):
                self.set_label(parts[0][:-1],index)
            return index
        
        if(parts[0] in self.instruction_set):
            self.instruction_set[parts[0]](parts[1:])
        else:
            raise NotImplementedError
        
    def is_label(self, possible_label: str) -> bool:
        return bool(self.label_pattern.match(possible_label))

    def set_label(self,new_label:str,index:int):
        self.labels_dict[new_label]=index

    def inc(self,parts:list[str])->None:
        self.registers_dict[parts[0]]+=1

    def dec(self,parts:list[str])->None:
        self.registers_dict[parts[0]]-=1

    def mov(self,parts:list[str])->None:
        if(self.is_valid_int(parts[1])):
            self.registers_dict[parts[0]]=int(parts[1])
        else:
            self.registers_dict[parts[0]]=self.registers_dict[parts[1]]

    def add(self,parts:list[str])->None:
        if(parts[1] in self.registers_dict):
            self.registers_dict[parts[0]]+=self.registers_dict[parts[1]]
        else:
            self.registers_dict[parts[0]]+=int(parts[1])

    def sub(self, parts:list[str])->None:
        if(parts[1] in self.registers_dict):
            self.registers_dict[parts[0]]-=self.registers_dict[parts[1]]
        else:
            self.registers_dict[parts[0]]-=int(parts[1])

    def mul(self,parts:list[str])->None:
        if(parts[1] in self.registers_dict):
            self.registers_dict[parts[0]]*=self.registers_dict[parts[1]]
        else:
            self.registers_dict[parts[0]]*=int(parts[1])

    def div(self,parts:list[str])->None:
        if(parts[1] in self.registers_dict):
            self.registers_dict[parts[0]]//=self.registers_dict[parts[1]]
        else:
            self.registers_dict[parts[0]]//=int(parts[1])

    def jmp(self,parts:list[str])->None:
        raise NotImplementedError
        
    def cmp(self,parts:list[str])->None:
        raise NotImplementedError
    
    def jne(self,parts:list[str])->None:
        raise NotImplementedError
    
    def je(self,parts:list[str])->None:
        raise NotImplementedError

    def jge(self,parts:list[str])->None:
        raise NotImplementedError

    def jg(self,parts:list[str])->None:
        raise NotImplementedError

    '''
        def jle(self,parts:list[str])->None:

        def jl(self,parts:list[str])->None:

        def call(self,parts:list[str])->None:

        def ret(self,parts:list[str])->None:

        def msg(self,parts:list[str])->None:
        
    '''


    '''
    def jnz(self,index,instruction:str)->int:
        register_or_constant_x,register_or_constant_y=instruction.split()
        if(self.is_valid_int(register_or_constant_x)):
            if(int(register_or_constant_x)==0):
                return index
        elif(self.registers_dict[register_or_constant_x]==0):
            return index
        if(self.is_valid_int(register_or_constant_y)):
            index+=int(register_or_constant_y)-1
        else:
            index+=self.registers_dict[register_or_constant_y]-1
        return index
    '''
        
    def is_valid_int(self,s:str)->bool:
        return bool(self.valid_int_pattern.match(s))

def simple_assembler(program:list)->dict:
    assembler=SimpleAssembler(program)
    return assembler.registers_dict