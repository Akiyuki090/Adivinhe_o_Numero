'''
Adivinhe o número
'''
import random


print('*' * 30)
print('ADIVINHE O NÚMERO' .center(30))
print('*' * 30)

while True:
    value = int(input('Digite[1] para um jogador ou [2] para dois jogadores: '))
    if value != 1 and value != 2:
        print('ERRO')
        break
    
    if value == 1:
        name = str(input('Digite seu nome: '))
        print(f'Jogador {name} versus IA')
        print('Tente adivinhar o número escolhido pela IA, os valores serão de: 0 até 10.')
        
        number = random.randint(0, 10)
        x = int(input('Digite sua aposta: '))
        if x == number:
            print('Parabéns você acertou: ')
        else:
            print(f'Que pena você errou, o número era: {number}')
        
    else:
        name1 = str(input('Digite seu nome: '))
        name2 = str(input('Digite seu nome: '))

        print(f'Jogador {name1} versus Jogador {name2}')
        print('Tente adivinhar o número escolhido pelo jogador 1, os valores serão de: 0 até 10.')
        
        number = int(input('Escolha o valor: '))
        x = int(input('Digite sua aposta: '))
        if x == number:
            print('Parabéns você acertou: ')
        else:
            print(f'Que pena você errou, o número era: {number}')
    
    ask = str(input('Nova partida [s/n]: '))
    if(ask == 'n'):
        print('Até logo')
        break
