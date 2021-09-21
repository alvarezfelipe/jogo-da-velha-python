telaInicial = '''
Bem-vindo ao tradicional jogo da velha!

As regras são as mesmas que você já conhece.
Para jogar, basta escolher um número de 1 a 9, de acordo com o mostrado abaixo:

     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     

'''
jogador = ''
pc = ''
comeca = ''
p1,p2,p3,p4,p5,p6,p7,p8,p9 = ' ',' ',' ',' ',' ',' ',' ',' ',' '
jogada = 0

print(telaInicial)

#Escolhendo com qual jogará
print('Quer ser o X (xis) ou O (letra o = bolinha)? ')

while jogador != 'O' and jogador != 'X':
    jogador = input('Digite X ou O e pressione Enter: ').strip().upper()
    if jogador != 'O' and jogador != 'X':
        print('Escolha inválida!! Tente novamente')

if jogador == 'O':
    pc = 'X'
    print('\nComputador diz: Ora, escolheu O, então o X é meu!! \n')
else:
    pc = 'O'
    print('\nComputador diz: Escolheu o X. Então o O é meu... \n')

while comeca != 'EU' and comeca != 'PC':
    comeca = input('Digite EU para vc começar ou PC, para que eu comece: ').strip().upper()
    if comeca != 'EU' and comeca != 'PC':
        print('Escolha inválida!! Tente novamente')

if comeca == 'EU':    
    print('\nComputador diz: Você joga primeiro. \n')
else:    
    print('\nComputador diz: Eu começo... \n')

def atualizarTela():
    global p1,p2,p3,p4,p5,p6,p7,p8,p9
    tela = '''
     |     |   
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
    '''.format(p1,p2,p3,p4,p5,p6,p7,p8,p9)
    print(tela)

def jogadaJogador():
    global jogada

    while True:
        try:
            jogada = int(input('Digite a posição'))