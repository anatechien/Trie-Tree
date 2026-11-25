
class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.eh_fim_de_palavra = False #atributo pra identificar o nó filho
        self.contador = 0 


class Trie:
    def __init__(self):
        raiz = NoTrie()
        self.atual = raiz


    #a cada char novo adicionado a arvore arrumar os ponteiros para os proximos nós
    #colocar a palavra inteira apenas como filho
    def inserir():
        #busca o nó com o ultimo char da palavra que queremos inserir

        #vê se tem o atributo self.eh_fim_de_palavra

        #busca o prox char no dicionário de ponteiros
        #se tiver avança para o prox nó (self.atual = prox nó)
        #se não adiciona o prox char no dicionário de ponteiros
            #adiciona o resto da palavra nos nós
            #adiciona o prox char no dicionário de ponteiros
            #se for o  ultimo char
                #adiciona self.eh_fim_de_palavra
                #adiciona a palavra inteira como nó filho

    #Encontra o nó do ultimo char
    #percorre cada uma das arvores que sobrou e guarda cada uma em uma lista de sugestões
    #algoritmo p percorrer as árvores que sobraram: pre-ordem (tanto faz)
    def buscar(self, palavra):
        #verifica se tem o char nos ponteiros da raiz
            #se tem avança para o nó do char
            #se o nó tem o atributo self.eh_fim_de_palavra então percorre todas as árvores em pre-ordem
                #cada arvore é o resto de palavra entao cada arvore é um elemento dentro da lista de sugestões.

        #"raiz" passa a ser o nó filho (nó atual) e fazemos a verificação dnv recurssivamente
