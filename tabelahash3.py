#TABELA HASH - MÉTODO DE COLISÃO: ENCADEAMENTO EXTERNO - UTILIZANDO TODOS OS DÍGITOS DA CHAVE NA INSERÇÃO

#bibliotecas:
import random #números aleatórios
import pandas as pd #gerar tabela excel
import time #para utilizar temporizadores

#classe da Tabela

class TabelaHash:
     def __init__(self):
          self.vetor = [0] * 9 #criação de um vetor com 9 posições iguais a 0

     def inserir_elemento(self, elemento): #método para inserir chaves
        resto = elemento % 9 #calcula o resto

        if self.vetor[resto] == 0: #se a posição de acordo com o resto estiver vazia, insere a chave
            self.vetor[resto] = elemento
            print(f'Chave: {elemento} inserida na posição {resto}')
        else: #se a posição já estiver ocupada
            if not isinstance(self.vetor[resto], list): #verifica se já existe uma lista naquela posição, caso não tenha, cria a lista
                self.vetor[resto] = [self.vetor[resto]]
            self.vetor[resto].append(elemento) #insere a chave
            print(f'Chave: {elemento} inserida na posição {resto}')

     def buscar_elemento(self, elemento):  # método para buscar um elemento
          resto = elemento % 9 #calcula o resto
          for i, chave_lista in enumerate(self.vetor[resto]):
            if chave_lista == elemento:  # se o elemento for encontrado na lista
                print(f'O elemento {elemento} está no índice: {resto}, e está na posição: {i} dentro do índice')
                return

     def criar_tabela_excel(self): #método para criação da tabela excel
        dados = []
        for i, item in enumerate(self.vetor):
            if isinstance(item, list):
                dados.append([i, item])
            else:
                dados.append([i, [item]])
        
        df = pd.DataFrame(dados, columns=['Índice', 'Valores'])
        df.to_excel("tabela_hash_3.xlsx", index=False)

     def contar_elementos(self): #método para contar os elementos por posição
        contador_elementos = []
        for i, item in enumerate(self.vetor):
            if isinstance(item, list):
                contador_elementos.append(len(item))
            else:
                contador_elementos.append(1)
        return contador_elementos
     
#criação da tabela hash
tabela = TabelaHash()


tempo_inicial_inserir = time.time() #inicia o temporizador para inserção

#geração e inserção das chaves
print('Inserção de chaves: ')
for _ in range(1000):
    numero_aleatorio = random.randint(10000, 99999) #gerando as chaves aleatórias
    tabela.inserir_elemento(numero_aleatorio)

tempo_final_inserir = time.time() #finaliza o temporizador
tempo_total_inserir = tempo_final_inserir - tempo_inicial_inserir #calcula o tempo total
print(f'Tempo de inserção de 1000 chaves: {tempo_total_inserir} segundos')

#Busca de chave aleatória
print('Busca de chave aleatória:')
posicao_aleatoria = random.randint(0, 8)#gera uma posição aleatória do vetor entre as 9 disponíveis
chave_aleatoria = random.choice(tabela.vetor[posicao_aleatoria])#depois de escolher a posição, agora escolher uma chave dentro da lista naquela posição

tempo_inicial_busca =  time.perf_counter()  #inicia o temporizador para busca
tabela.buscar_elemento(chave_aleatoria) #busca a chave
tempo_final_busca =  time.perf_counter()  #finaliza o temporizador
tempo_total_busca = tempo_final_busca - tempo_inicial_busca #calcula o tempo total
print(f'Tempo de busca da chave: {tempo_total_busca} segundos')



#contagem de elementos por posição
print('Número de elementos por posição:')
contagem_elementos = tabela.contar_elementos()
for i, count in enumerate(contagem_elementos):
    print(f'Posição {i}: {count} elementos')

#criação da tabela
tabela.criar_tabela_excel()
print('A tabela HASH está no arquivo: tabela_hash_3.xlsx')