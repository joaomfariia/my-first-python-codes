from rich import print
import os
from time import sleep

# Contador
votos_bolsonaro = 0
votos_lula = 0

while True:

    print('*'*26)
    print(f'[on blue]Total Bolsonaro: {votos_bolsonaro}')
    print(f'[on red]Total Lula: {votos_lula}')
    print('*'*26)

    try:
        voto = int(input(f'Escolha sua opção de voto{os.linesep}1 - Bolsonaro{os.linesep}2 - Lula{os.linesep}Seu voto:'))

        if voto == 1:
            votos_bolsonaro += 1
        elif voto == 2:
            votos_lula += 1
        else:
            pass

    except:
        print("Digite apenas 1 ou 2.")
        sleep(1.5)

    os.system('cls')