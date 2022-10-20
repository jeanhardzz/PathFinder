import sys
from sistemanpc import SistemaNPC

def main():
    lst = sys.argv[1:]
    
    npc = SistemaNPC()
    npc.Leitura(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])
    npc.IniciaAgente()

if __name__ == "__main__":
    main()