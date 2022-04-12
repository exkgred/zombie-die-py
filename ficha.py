#Joshua Silva, Analise e desenvolvimento de softwares
from asyncore import read
import itertools
from lib2to3.pytree import convert
from os import remove
import poplib
import random
from timeit import repeat

CEEEREBROS = 'ceeerebros'
CONST_TIRO = 'T'
CONST_MORTE = 3
CONST_CEREBRO = 'C'
CONST_PASSOS = 'P'
CONST_MAXIMO_JOGADORES = 6 # constante ultilizada para regra do jogo
CONST_MINIMO_JOGADORES = 2
DADO_VERDE_6 = "CPCTPC"
DADO_AMARELHO_4 = "TPCTPC"
DADO_VERMELHO_3 = "TPTCPT"
LISTA_DADOS = [
DADO_VERDE_6,DADO_VERDE_6,DADO_VERDE_6,DADO_VERDE_6,DADO_VERDE_6,DADO_VERDE_6,
DADO_AMARELHO_4, DADO_AMARELHO_4, DADO_AMARELHO_4, DADO_AMARELHO_4,
DADO_VERMELHO_3,DADO_VERMELHO_3,DADO_VERMELHO_3]

class Jogador:
    nome = ''
    dados = []
    cerebros = 0
    tiros = 0
    passos = 0 

def rolarDado(corDadoRepeticao): 
    if corDadoRepeticao != '':
        faceDado = random.choice (corDadoRepeticao)
        return faceDado, corDadoRepeticao;
    numSorteado = random.randrange(0, 13)
    dadoSorteado = LISTA_DADOS[numSorteado] 
    faceDado = random.choice(dadoSorteado)
    return faceDado, dadoSorteado;

def converterCor (corDado): 
    if  (corDado == DADO_VERDE_6):
        corDado1 ='VERDE'

    elif (corDado == DADO_AMARELHO_4):
        corDado1 = 'AMARELO'

    else:
        corDado1 = 'VERMELHO' 
    return corDado1;

def contabilizarResultados(listaJogadores):
    for jogador in listaJogadores:
        if jogador.cerebros >= 13:
            return jogador.nome 
    return ''
def derrota(listaJogadores):
    for jogador in listaJogadores:
        if jogador.tiros == 3:
            return jogador.nome
    return ''

print("Seja bem-vindo ao jogo Zombie Dice!");
#bloco de condições de quantidade de jogadores
quantidadeJogador = 0
while True:
    nJogadores = input("informe a quantidade de jogadores: ")
    nJogadores = int(nJogadores)
    print (nJogadores)
    if nJogadores < CONST_MINIMO_JOGADORES or nJogadores > CONST_MAXIMO_JOGADORES:
        print("AVISO: Você precisa de pelo menos 2 jogadores!")
    else:
        quantidadeJogador = nJogadores
        break
    
#inscrição jogadores
listaJogadores = []
for i in range(nJogadores):
    nome = input("Digite o nome do jogador: " + str (i + 1 ) + ": ");
    if nome == "sair":
        break
    jogador = Jogador()
    jogador.nome = nome
    listaJogadores.append(jogador)
for jogador in listaJogadores:
    print(jogador.nome)

#inicio

print('Que comecem os jogos!!')
#rounds 
jogadorAtual = 0;
dadosAtuais =['', '', '']


while True: #turno

    print("TURNO DO JOGADOR " + listaJogadores[jogadorAtual].nome);
    passos = 0
    for index, value in enumerate (dadosAtuais):
        faceDado, corDado = rolarDado(value)
        print(faceDado, converterCor(corDado))
        listaJogadores[jogadorAtual].dados.append((faceDado,corDado))
        if faceDado =='T':
            listaJogadores[jogadorAtual].tiros+= 1
            dadosAtuais [index] = ''
        elif faceDado == 'C':
            listaJogadores[jogadorAtual].cerebros+= 1
            dadosAtuais [index] = ''
        else: 
            listaJogadores[jogadorAtual].passos+=1
            passos+=1
            dadosAtuais [index] = corDado
        
    print('Quantidade de '+ listaJogadores[jogadorAtual].nome +' cerebros '  + str (listaJogadores[jogadorAtual].cerebros))
    if passos > 0:

        continuarTurno = input(listaJogadores[jogadorAtual].nome + ' dejesa continuar rolando?')
        if continuarTurno == 'sim':
            continue
          
    dadosAtuais = ['', '', '']
    jogadorAtual+=1
    if jogadorAtual >= len(listaJogadores):
        jogadorAtual = 0
            # vencedor = contabilizarResultados(listaJogadores)
            # if vencedor != '':
            #     print(vencedor + ' você é o vencedor')
            #     break
    input('Digite qualquer tecla para proximo jogador')