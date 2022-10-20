from estado import Estado
from no import No

class Agente:
    no_i = None #tipo no
    estado_i = None #tipo Estado
    estado_f = None #tipo Estado
    mapa = None #tipo matriz de int   
    cutoff = No(Estado(-1,-1),None,-1,-1,-1)  
    expandidos = 0 
    s_id = 0  

    def __init__(self,mapa,li,ci,lf,cf) -> None:
        self.estado_i = Estado(li,ci)
        self.estado_f = Estado(lf,cf)
        self.mapa = mapa

        self.no_i = No(self.estado_i,None,self.GetCusto(self.estado_i),0,self.s_id)                
        self.s_id = self.s_id + 1

    def GetCusto(self,estado):
        c = self.mapa[estado.l][estado.c]

        if c == '.':
            return 1.0

        if c == ';':
            return 1.5

        if c == '+':
            return 2.5
        
        if c == 'x':
            return 6.0

        if c == '@':
            return -1
        
    def ShowBorda(self):
        print("Borda:")
        print("---------")
        for no in self.borda:
            print(no)
            print("---------")
    
    def FuncSucessora(self,no):
        l_filhos = []
        max_l = len(self.mapa)
        max_c = len(self.mapa[0])
        estado_no = no.estado
        l = estado_no.l
        c = estado_no.c

        if l == self.estado_f.l and c == self.estado_f.c:
            self.sucesso = 1

        #CIMA        
        if l-1 >= 0:     
            novo_estado = Estado(l-1,c)
            custo = self.GetCusto(novo_estado)            
            if(custo != -1):                                
                f_cima = No(novo_estado,no,custo,no.profundidade + 1,self.s_id)
                self.s_id = self.s_id + 1
                l_filhos.append(f_cima)
        
        #BAIXO
        if l+1 <= max_l-1:            
            novo_estado = Estado(l+1,c)
            custo = self.GetCusto(novo_estado)
            if(custo != -1):                                
                f_baixo = No(novo_estado,no,custo,no.profundidade + 1,self.s_id)
                self.s_id = self.s_id + 1
                l_filhos.append(f_baixo)
        
        #DIREITA
        if c+1 <= max_c-1:            
            novo_estado = Estado(l,c+1)
            custo = self.GetCusto(novo_estado)
            if(custo != -1):                                
                f_direita = No(novo_estado,no,custo,no.profundidade + 1,self.s_id)
                self.s_id = self.s_id + 1
                l_filhos.append(f_direita)                
        
        #ESQUERDA
        if c-1 >= 0:            
            novo_estado = Estado(l,c-1)
            custo = self.GetCusto(novo_estado)            
            if(custo != -1):                                
                f_esquerda = No(novo_estado,no,custo,no.profundidade + 1,self.s_id)
                self.s_id = self.s_id + 1
                l_filhos.append(f_esquerda)

        return l_filhos


    def BFS(self):
        if self.GetCusto(self.no_i.estado) != -1 and self.GetCusto(self.estado_f) != -1:
            path_custo = 0
            s = self.BFS_helper(self.no_i)
            if s != None:
                path = []
                no = s    

                path_custo = path_custo + no.custo
                path.append(no)        
                while no.pai != None:
                    no = no.pai
                    path_custo = path_custo + no.custo
                    path.insert(0,no)
                                
                s = ""
                for p in path:
                    s = s + p.estado.__str__() + " "
                
                path_custo = path_custo - self.no_i.custo
                print(path_custo,s)
                #print(self.expandidos)

    
    def BFS_helper(self,no):
        borda = [] #Nesse caso a borda/fronteira é uma fila
        visitados = []        

        if no.estado == self.estado_f:
            return no

        borda.append(no)  

        while len(borda) > 0:
            no = borda.pop(0)
            visitados.append(no)

            self.expandidos = self.expandidos + 1
            filhos = self.FuncSucessora(no)
            for filho in filhos:                
                if filho not in visitados and filho not in borda:                    
                    if filho.estado == self.estado_f:
                        return filho
                    borda.append(filho)
        
        return None

    def BuscaBorda(self,no,borda):
        for p in borda:
            if no.estado.l == p.estado.l:
                if no.estado.c == p.estado.c:
                    return True
        return None

    def UCS(self):
        if self.GetCusto(self.no_i.estado) != -1 and self.GetCusto(self.estado_f) != -1:
            s = self.UCS_helper(self.no_i)
            if s != None:
                custo = s.aux_custo - self.no_i.custo

                path = []
                no = s    
                
                path.append(no)        
                while no.pai != None:
                    no = no.pai            
                    path.insert(0,no)
                
                s = ""
                for p in path:
                    s = s + p.estado.__str__() + " "
                
                print(custo,s)
                #print(self.expandidos)
    
    def UCS_helper(self,no):
        borda = []
        visitados = []
        
        
        borda.append(no)         
        while len(borda) > 0 :            
            borda.sort()
            no = borda.pop(0)        

            if no.estado == self.estado_f:                
                return no
            
            visitados.append(no)
            self.expandidos = self.expandidos + 1
            filhos = self.FuncSucessora(no)
            for filho in filhos:
                filho.AddCusto(filho.pai.aux_custo)
                if filho not in visitados and filho not in borda:
                    borda.append(filho)
                else:
                    for i in range(len(borda)):
                        if borda[i] == filho and filho < borda[i]:
                            borda[i] = filho

        return None

    def IDS(self):
        if self.GetCusto(self.no_i.estado) != -1 and self.GetCusto(self.estado_f) != -1:
            l = 0            
            result = self.cutoff            
            while result == self.cutoff:
                result = self.IDS_helper(self.no_i,l)                 
                l = l + 1            
            
            if result != None:                
                path_custo = 0
                path = []
                no = result    

                path_custo = path_custo + no.custo
                path.append(no)        
                while no.pai != None:
                    no = no.pai
                    path_custo = path_custo + no.custo
                    path.insert(0,no)
                
                s = ""
                for p in path:
                    s = s + p.estado.__str__() + " "
                
                path_custo = path_custo - self.no_i.custo
                print(path_custo,s)
                #print(self.expandidos)

    def IDS_helper(self,no,l):
        borda = []
        visitados = []
        borda.append(no)
        result = None
        
        while len(borda) > 0:            
            no = borda.pop()                        

            if no.estado == self.estado_f:
                return no
            visitados.append(no)
            
            if no.profundidade < l:
                result = self.cutoff

            else:
                self.expandidos = self.expandidos + 1
                filhos = self.FuncSucessora(no)
                for filho in filhos:
                    if filho not in visitados and filho not in borda:                    
                        borda.append(filho)
        return result
    
    def Greedy(self):
        if self.GetCusto(self.no_i.estado) != -1 and self.GetCusto(self.estado_f) != -1:            
            result = self.Greedy_helper(self.no_i)                 
                         
            if result != None:                
                path_custo = 0
                path = []
                no = result    

                path_custo = path_custo + no.custo
                path.append(no)        
                while no.pai != None:
                    no = no.pai
                    path_custo = path_custo + no.custo
                    path.insert(0,no)
                
                s = ""
                for p in path:
                    s = s + p.estado.__str__() + " "
                
                path_custo = path_custo - self.no_i.custo
                print(path_custo,s)
                #print(self.expandidos)
    
    def Greedy_helper(self,no):
        borda = []
        visitados = []        
        result = None
        borda.append(no)
        
        while len(borda) > 0:
            
            menor = 0
            for i in range(1,len(borda),1):
                if self.DistObjetivo(borda[i].estado) < self.DistObjetivo(borda[menor].estado):
                    menor = i

            no = borda.pop(menor)                        
            if no.estado == self.estado_f:
                return no

            visitados.append(no)

            self.expandidos = self.expandidos + 1
            filhos = self.FuncSucessora(no)
            for filho in filhos:
                if filho not in visitados and filho not in borda:                    
                    borda.append(filho)
        return result


    def DistObjetivo(self,estado):
        xl = self.estado_f.l - estado.l
        yc = self.estado_f.c - estado.c

        d2 = pow(xl,2) + pow(yc,2)

        return pow(d2,0.5)
    
    def Astar(self):
        if self.GetCusto(self.no_i.estado) != -1 and self.GetCusto(self.estado_f) != -1:
            s = self.Astar_helper(self.no_i)
            if s != None:
                path_custo = 0
                path = []
                no = s    

                path_custo = path_custo + no.custo
                path.append(no)        
                while no.pai != None:
                    no = no.pai
                    path_custo = path_custo + no.custo
                    path.insert(0,no)
                
                s = ""
                for p in path:
                    s = s + p.estado.__str__() + " "
                
                path_custo = path_custo - self.no_i.custo
                print(path_custo,s)
                #print(self.expandidos)
    
    def Astar_helper(self,no):
        borda = []
        visitados = []
        borda.append(no)  

        while len(borda) > 0 :            
            menor = 0
            for i in range(1,len(borda),1):
                if self.DistObjetivo(borda[i].estado) + borda[i].aux_custo < self.DistObjetivo(borda[menor].estado) + borda[menor].aux_custo:
                    menor = i

            no = borda.pop(menor)            

            if no.estado == self.estado_f:                
                return no
            
            visitados.append(no)
            self.expandidos = self.expandidos + 1
            filhos = self.FuncSucessora(no)
            for filho in filhos:
                filho.AddCusto(filho.pai.aux_custo)
                if filho not in visitados and filho not in borda:
                    borda.append(filho)
                else:
                    for i in range(len(borda)):
                        if borda[i].estado == filho.estado and filho.aux_custo < borda[i].aux_custo:
                            borda[i] = filho
               

        return None

    
    def Astar_helper2(self,no):
        borda = []
        visitados = []

        g = {}
        f = {}
        pai = {}

        g[(no.estado.l,no.estado.c)] = 0
        f[(no.estado.l,no.estado.c)] = g[(no.estado.l,no.estado.c)] + self.DistObjetivo(no.estado)
        pai[(no.estado.l,no.estado.c)] = None
        
        borda.append(no)

        while len(borda) > 0 :
            menor = 0
            for i in range(1,len(borda),1):
                if f[(borda[i].estado.l,borda[i].estado.c)] < f[(borda[menor].estado.l,borda[menor].estado.c)]:
                    menor = i

            no = borda.pop(menor)

            if no.estado == self.estado_f:
                return no
            
            visitados.append(no)
            self.expandidos = self.expandidos + 1
            filhos = self.FuncSucessora(no)
            for filho in filhos:
                if filho not in visitados:
                    if filho not in borda:
                        g[(filho.estado.l,filho.estado.c)] = g[(no.estado.l,no.estado.c)] + filho.custo
                        f[(filho.estado.l,filho.estado.c)] = g[(filho.estado.l,filho.estado.c)] + self.DistObjetivo(filho.estado)
                        pai[(filho.estado.l,filho.estado.c)] = no
                        borda.append(filho)
                    elif g[(no.estado.l,no.estado.c)] + filho.custo < g[(filho.estado.l,filho.estado.c)]:
                        g[(filho.estado.l,filho.estado.c)] = g[(no.estado.l,no.estado.c)] + filho.custo
                        f[(filho.estado.l,filho.estado.c)] = g[(filho.estado.l,filho.estado.c)] + self.DistObjetivo(filho.estado)
                        pai[(filho.estado.l,filho.estado.c)] = no
           
        return None
        

                    
