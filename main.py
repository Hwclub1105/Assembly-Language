#Assembly Language
instruction_set = {'ADD':'0000','SUB':'0001','MOV':'0010','LDR':'0011','OUT':'0100','HAlT':'0101','BGT':'0110','BLT':'0111','BEQ':'1000','B':'1001','CMP':'1010','STR':'1011'}
memory = {'m0':'', 'm1' : '', 'm2' : '', 'm3' : ''}
temp_CMP = []
register = {'r0':'', 'r1' : '', 'r2' : '', 'r3' : ''}
branches = []

def I0000(R0, R1, R2): #ADD
    register[R0] = register[R1] + register[R2]

def I0001(R0, R1, R2): #SUB
    register[R0] = register[R1] - register[R2]

def I0010(): #MOV
    pass

def I0011(R0, M0): #LDR
    register[R0] = memory[M0]
    
    
def I1010(R0,R1,temp_CMP): #CMP
    if register[R0] > register[R1]:
        temp_CMP.append("G")
    elif register[R0] < register[R1]:
        temp_CMP.append("L")
    else:
        temp_CMP.append("E")

def I0110(branch): #BGT
    if temp_CMP[-1] == 'G':
        branches.append(branch)
        
def I0111(branch): #BLT
    if temp_CMP[-1] == 'L':
        branches.append(branch)
        
def I1000(branch): #BEQ
    if temp_CMP[-1] == 'E':
        branches.append(branch)
        
def I1011(R1,M1): #STR
    memory[M1] = register[R1]
    
def Assemble(codefile):
    with open(codefile, 'r') as file:
        for _ in range(len(file.readlines())):
            print(file.read())
            line = file.readline()
            print(line)
            if ':' not in line:
                print(True)
        


Assemble('code.txt')

