# IAMenorCaminhoNPC
Este projeto  tem como finalidade propor uma resolução para o problema Path-Finding.

# Execução

Para executar este projeto basta abrir um ambiente python e executar:
    python pathfinder.py [caminho_para_arquivo_mapa] [metodo] xi yi xf yf

Onde:

- pathfinder.py é o arquivo principal

- caminho_para_arquivo_mapa é o caminho para abrir o arquivo mapa

- metodo é a escolha de qual algoritmo, são eles: BFS,IDS,UCS,Greedy e Astar

- (xi,yi) é um conjunto do tipo (coluna,linha) que representa o ponto inicial no mapa

- (xf,yf) é um conjunto do tipo (coluna,linha) que representa o ponto final no mapa

exemplo de execução:
    python pathfinder.py mapa.map BFS 1 1 3 1

Executa o arquivo principal, usando o mapa.map como mapa e o método de busca BFS. Bem como o ponto inicial (1,1) e final (3,1).


