#TABELA HASH - MÉTODO DE COLISÃO SONDAGEM LINEAR - UTILIZANDO OS 3 ÚLTIMOS DÍGITOS DA CHAVE NA INSERÇÃO

#bibliotecas:
import random #números aleatórios
import pandas as pd #gerar tabela excel
import time #para utilizar temporizadores

#classe da Tabela
class TabelaHash:
     def __init__(self):
        self.tamanho = 1000 
        self.lista = [[] for _ in range(self.tamanho)] #criação da lista com 1000 posições

     def inserir_elemento(self, elemento): #método para inserir elementos
        chave = elemento % 1000  #irá utilizar apenas os 3 últimos dígitos da chave
        resto = chave % 9 #calcula o resto

        if self.lista[resto] == []: #verifica se a posição de acordo com o resto está vazia
            self.lista[resto] = elemento
            print(f'Chave: {elemento} inserida na posição {resto}')
        else: #se a posição já estiver ocupada
            for i in range(resto, len(self.lista)): #procura a próxima posição livre e insere a chave
                 if self.lista[i] == []:
                        self.lista[i] = elemento
                        print(f'Chave: {elemento} inserida na posição {i}')
                        return i  #para não continuar percorrendo a lista
                 
     def busca_elemento(self, elemento): #método para buscar elemento
        chave = elemento % 1000  #irá utilizar apenas os 3 últimos digitos da chave
        resto = chave % 9 #calcula o resto

        if self.lista[resto] == elemento: #verifica se a chave está na posição de acordo com o seu resto da divisão
            print(f'Chave: {elemento} está na posição {resto}')
        else: #se a posição já estiver ocupada com outra chave que não seja a desejada
            for i in range(resto, len(self.lista)): #procura nas próximas posições a chave 
                 if self.lista[i] == elemento:
                        print(f'Chave: {elemento} está no índice {i}')
                        return i  #para não continuar percorrendo a lista
         
            
     def criar_tabela_excel(self): #método para criação da tabela excel
        dados = []
        for i, item in enumerate(self.lista):
            if isinstance(item, list):
                dados.append([i, item])
            else:
                dados.append([i, [item]])
        
        df = pd.DataFrame(dados, columns=['Índice', 'Valores'])
        df.to_excel("tabela_hash_2.xlsx", index=False)


#criação da tabela hash
tabela = TabelaHash()

tempo_inicial_inserir = time.time() #inicia o temporizador para inserção

#geração e inserção das chaves
print('Inserção de chaves: ')
for _ in range(1000):
    numero_aleatorio = random.randint(10000, 99999)
    tabela.inserir_elemento(numero_aleatorio)

tempo_final_inserir = time.time() #finaliza o temporizador
tempo_total_inserir = tempo_final_inserir - tempo_inicial_inserir #calcula o tempo total
print(f'Tempo de inserção de 1000 chaves: {tempo_total_inserir} segundos')

#Busca de chave aleatória
print('Busca de chave aleatória:')
elemento_test = tabela.lista[random.randint(0, 999)] #um elemento aleatório é escolhido
tempo_inicial_busca =  time.perf_counter()  #inicia o temporizador para busca
tabela.busca_elemento(elemento_test) #realiza a busca
tempo_final_busca =  time.perf_counter()  #finaliza o temporizador
tempo_total_busca = tempo_final_busca - tempo_inicial_busca #calcula o tempo total
print(f'Tempo de busca da chave: {tempo_total_busca} segundos')


#criação da tabela
tabela.criar_tabela_excel()
print('A tabela HASH está no arquivo: tabela_hash_2.xlsx')