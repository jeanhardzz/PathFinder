class Estado:
    l = None #tipo int
    c = None #tipo int

    def __init__(self,l,c) -> None:
        self.l = l
        self.c = c

    def __str__(self):
        return '(' + str(self.c) + ',' + str(self.l) + ')'
    
    def __eq__(self, outro):
        if outro == None:
            return False
        else:
            return ((self.l == outro.l) and (self.c == outro.c))
    
    #def __lt__(self, outro):
    #    return ((self.l < outro.l) and (self.c < outro.c))