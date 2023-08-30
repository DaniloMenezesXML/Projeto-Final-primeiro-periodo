import random
import os
from time import sleep

humano = 0
pc = 0
soma = 0


def pontuacao():
    print(f'O placar está Jogador {humano} x {pc} Máquina')
    print('Quem chegar a 5 primeiro ganha!')

def iniciar():
    
    print('='*20)
    print('-----BEM VINDO-----')
    print('--------AO---------')
    print('-------JOGO--------')
    print('--------DA---------')
    print('-----PURRINHA-----')
    print('='*20)
    print('Regras do jogo:Você deve escolher um numero de 1 a 3 e tentar adivinhar qual a soma entre o que você escolheu e o seu adversário')
    print('Bora começar!')
    

iniciar()



jogar = True

while jogar == True:
        
    
    jogada = []
        
        
    maoH = int(input('Escolha um numero pra sua mão entre 0 e 3: '))
    if maoH > 3:
        print('Numero inválido! Somente um número entre 0 e 3!')
        continue
    jogada.append(maoH)
    maoPC = random.randint(0,3)
    jogada.append(maoPC)
    soma = sum(jogada)
    opcaoH = int(input('Informe a sua opçao entre 0 e 6: '))
    if opcaoH > 6:
        print('Numero inválido! Somente um número entre 0 e 6!')
        continue
    if maoPC == 0:
        opcaoPC = random.randint(0,3)
    elif maoPC == 1:
        opcaoPC = random.randint(1,4)
    elif maoPC == 2:
        opcaoPC = random.randint(2,5)
    elif maoPC == 3:
        opcaoPC = random.randint(3,6)    
        
        
    print(f'O jogo deu {soma}')
    print(f'O jogador colocou {maoH} e a Máquina colocou {maoPC}')
    print(f'O jogador chutou {opcaoH} e a Maquina chutou {opcaoPC}! Vamos ver quem ganhou!')
    sleep(3)
    os.system('cls')
    if opcaoH == soma and opcaoPC == soma:
        pc = pc+1
        humano = humano +1
        print('Os dois acertaram!Os dois ganharam pontos!')
        pontuacao()
    elif opcaoPC == soma:
        print('A maquina acertou!Ganhou um ponto!')
        pc = pc+1
        pontuacao()
        sleep(5)
        os.system('cls')
        if pc > 4:
            print(f'A máquina ganhou')
            jogar = False
    elif opcaoH == soma:
        print('Você acertou Jogador!Ganhou um ponto!')
        humano = humano +1
        pontuacao()
        sleep(5)
        os.system('cls')
        if humano > 4:
            print(f'Você ganhou Jogador')
            jogar = False
    else:
        print('Ninguem pontuou! Segue o baile!')
        pontuacao()
        sleep(5)
        os.system('cls')

    










    

 


