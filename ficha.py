#Joshua Silva, Analise e desenvolvimento de softwares
import itertools
from os import remove
import poplib
import random

CEEEREBROS = 'ceeerebros'
CONST_TIRO = 'T'
CONST_MORTE = 3
CONST_CEREBRO = 'C'
CONST_PASSOS = 'P'
CONST_MAXIMO_JOGADORES = 6 # constante ultilizada para regra do jogo
CONST_MINIMO_JOGADORES = 2

#bloco de condições de quantidade de jogadores
quantidadeJogador = 0
while True:
    nJogadores = input("informe a quantidade de jogadores: ")
    nJogadores = int(nJogadores)
    print (nJogadores)
    if nJogadores < CONST_MINIMO_JOGADORES or nJogadores > CONST_MAXIMO_JOGADORES:
        print("quantidade incorreta, informe a quantidade de jogadores correta: ")
    else:
        quantidadeJogador = nJogadores
        break
    
#inscrição jogadores
nomes = []
for i in range(nJogadores):
    nome = input("Digite o nome: ")
    if nome == "sair":
        break
    nomes.append(nome)
jogadores = nomes
print(jogadores)

#inicio
print('Que comecem os jogos HAHAHAHAHAHA')

#rounds 

    #turno

#resultado

# #dados
# dadoVerde6 = [CONST_CEREBRO,CONST_PASSOS,CONST_CEREBRO,CONST_TIRO,CONST_PASSOS,CONST_CEREBRO]
# for i in range(1):
#     dado6 = random.choice(dadoVerde6)
#     #print(dado6)
# dadoAmarelo4 = [CONST_TIRO,CONST_PASSOS,CONST_CEREBRO,CONST_TIRO,CONST_PASSOS,CONST_CEREBRO]
# for i in range(1):
#     dado4 = random.choice(dadoAmarelo4)
#    # print(dado4)
# dadoVermelho3 = [CONST_TIRO,CONST_PASSOS,CONST_TIRO,CONST_CEREBRO,CONST_PASSOS,CONST_TIRO]
# for i in range(1):
#     dado3 = random.choice(dadoVermelho3)
#     #print(dado3)
#dadoVerde6 = random.choice("CPCTPC")
#print (dadoVerde6)
#dadoAmarelo4 = random.choice("TPCTPC")
#print (dadoAmarelo4)
#dadoVermelho3 = random.choice("TPTCPT")
# #print (dadoVermelho3)

# tubo = list(itertools.chain(dado6, dado4, dado3))
# print(tubo)
# resultadoRoll = [list(itertools.chain(tubo))]
# if countP == 1 or countP > 1:#passos
#     countP = CONST_PASSOS.count(CONST_PASSOS)
#     print(countP)
#     for str in range(3):
#         jogarNovamente = input('dejesa jogar novamente os dados? ')
#         if jogarNovamente == 'sim':
#             print(tubo)
#         elif jogarNovamente == 'nao' or 'n' or 'não':
#             break

# elif resultadoRoll <= countC:#cerebro
#     remove(CONST_CEREBRO)
# #2
