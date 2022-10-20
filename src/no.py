class No:
    estado = None #tipo Estado
    pai = None #tipo No
    custo = None #tipo float
    profundidade = None # tipo int
    aux_custo = 0
    s_id = None

    def __init__(self,estado,pai,custo,prof,id) -> None:
        self.estado = estado
        self.pai = pai
        self.custo = custo
        self.profundidade = prof
        self.aux_custo = custo
        self.s_id = id
    
    def __str__(self) -> str:  
        p = 'None' 
        if self.pai != None:
            p = self.pai.estado.__str__()

        return self.estado.__str__() +'\n\t' + p + '\n' + str(self.custo) + '\n' + str(self.profundidade)
    
    def AddCusto(self,custo):
        self.aux_custo = self.aux_custo + custo
    
    def __lt__(self, outro):
        return self.aux_custo < outro.aux_custo
    
    def __eq__(self, outro):
        if outro == None:
            return False
        else:
            return ((self.estado.l == outro.estado.l) and (self.estado.c == outro.estado.c))