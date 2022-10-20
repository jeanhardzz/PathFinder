from agente import Agente

class SistemaNPC:

    path = None
    metodo = None
    inicial_x = None
    inicial_y = None
    final_x = None
    final_y = None
    m = None
    h = None
    w = None
    
    def __init__(self) -> None:
        pass


    def Leitura(self,path,metodo,i_y,i_x,f_y,f_x):
        self.path = path
        self.metodo = metodo
        self.inicial_x = int(i_x)
        self.inicial_y = int(i_y)
        self.final_x = int(f_x)
        self.final_y = int(f_y)
        
        with open(self.path,"r")as arq:            
            txt = arq.readlines()            
            
            w,h = txt[0].split()
            self.w = int(w)
            self.h = int(h)
            
            self.m = [[0 for col in range(self.w)] for row in range(self.h)]            

            lines = txt[1:]
            for i in range(self.h):
                for j in range(self.w):
                    self.m[i][j] = lines[i][j]
    def IniciaAgente(self):        

        agente = Agente(self.m, self.inicial_x, self.inicial_y, self.final_x, self.final_y)        
        if self.metodo == 'BFS':     
            agente.BFS()
        if self.metodo == 'UCS':       
            agente.UCS()
        if self.metodo == 'IDS':       
            agente.IDS()
        if self.metodo == 'Greedy':       
            agente.Greedy()
        if self.metodo == 'Astar':       
            agente.Astar()
        

                
