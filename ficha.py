#Joshua Silva, Analise e desenvolvimento de softwares
from asyncore import read
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
    listaJogadores.append(nome)
jogadores = listaJogadores
print(jogadores)

#inicio

#dados
dadoVerde6 = random.choice("CPCTPC")
#print (dadoVerde6)
dadoAmarelo4 = random.choice("TPCTPC")
#print (dadoAmarelo4)
dadoVermelho3 = random.choice("TPTCPT")
# #print (dadoVermelho3)

listaDados = [
dadoVerde6,dadoVerde6,dadoVerde6,dadoVerde6,dadoVerde6,dadoVerde6,
dadoAmarelo4, dadoAmarelo4, dadoAmarelo4, dadoAmarelo4,
dadoVermelho3,dadoVermelho3,dadoVermelho3]

print('Que comecem os jogos!!')
#rounds 
jogadorAtual = 0;
dadosSorteados = [];
tiros = 0;
cerebros = 0;
passos = 0;

while True:
    print("TURNO DO JOGADOR ", listaJogadores[jogadorAtual]);
    
    for i in 0 3  1:
        numSorteado = random.choices(0, 12)
        dadoSorteado = listaDados[numSorteado]

    if  (dadoSorteado == 'CPCTPC'):
        corDado ='VERDE'

    elif (dadoSorteado == 'TPCTPC'):
        corDado = 'AMARELO'

    elif  (dadoSorteado == 'TPTCPT'):
        corDado = 'VERMELHO'
        break

print("Dado sorteado: ", corDado);

dadosSorteados[i] = dadoSorteado;

print("As faces sorteadas foram: ")

for dadoSorteado in dadosSorteados:
    numFaceDado = random.choices(0, 5);
if dadoSorteado[numFaceDado] == "C":
    print("- cerebros (você comeu um cerebro)");
    cerebros = cerebros + 1;
elif dadoSorteado[numFaceDado] == "T":
    print("- TIRO (você levou um tiro)");
    tiros = tiros + 1;
elif dadoSorteado[numFaceDado] == "P":
    print("- PASSOS (uma vitima escapou)");
    passos = passos + 1;

print("SCORE ATUAL: ");
print("cerebros: ", cerebros);
print("TIROS: ", tiros);

print("AVISO: você deseja continuar jogando dados? (s=sim / n=não)");


continuarTurno = input('continuar Turno:');

if continuarTurno == 'n':
    jogadorAtual = jogadorAtual + 1;
    dadosSorteados = [];
    tiros = 0;
    cerebros = 0;
    passos = 0;

if (jogadorAtual == range(listaJogadores)):
    print("Finalizando protótipo do jogo...");

else:
    print("Iniciando mais uma rodada do turno atual...");
    dadosSorteados = [];
