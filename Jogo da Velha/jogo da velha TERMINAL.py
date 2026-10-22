tabuleiro = [
    [" ", " ", " ",],
    [" ", " ", " ",],
    [" ", " ", " ",]
]

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)



def verificar_vitoria(tabuleiro, jogador):
    #linha
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    
    #coluna
    for c in range(3):
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] == jogador:
            return True

    #diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

        
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "❌"

while True:
    mostrar_tabuleiro(tabuleiro)
    print(f'Jogador {jogador_atual}\n')

    try:
        linha = int(input('Linha [0] [1] [2]: '))
        coluna = int(input('Coluna [0] [1] [2]: '))
        print('\n')
    except ValueError:
        print('Digite apenas números.\n')
        continue

    if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
        print('Posição da linha e/ou coluna inválidos! Use apenas 0, 1, 2\n')
        continue

    if tabuleiro[linha][coluna] != " ":
        print('Posição ocupada!\n')
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        print(f'Jogador {jogador_atual} venceu!\n')
        break

    if verificar_empate(tabuleiro):
        mostrar_tabuleiro(tabuleiro)
        print('Empate!\n')
        break

    jogador_atual = "⭕" if jogador_atual == "❌" else "❌"