import tkinter as tk


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


#CORES
cor_fundo = "#1e1e2e"
cor_botao = "#313244"
cor_hover = "#45475a"
cor_texto = "#cdd6f4"
cor_verde = "#a6e3a1"
cor_amarelo = "#f9e2af"
cor_vermelho = "#dc143c"

        
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "❌"

def mostrar_resultado(titulo, mensagem, cor_destaque):
    """Abre uma janela no mesmo estilo do jogo e espera o jogador fechar."""
    popup = tk.Toplevel(janela)
    popup.title('FIM DE JOGO')
    popup.configure(bg=cor_fundo)
    popup.resizable(False, False)
    popup.transient(janela)

    tk.Label(
        popup, text=titulo,
        font=('Consolas', 18, 'bold'),
        bg=cor_fundo, fg=cor_destaque
    ).pack(padx=40, pady=(25, 5))

    tk.Label(
            popup, text=mensagem,
            font=('Consolas', 12),
            bg=cor_fundo, fg=cor_texto
        ).pack(padx=40, pady=(0, 15))

    tk.Button(
        popup, text='Jogar de novo', font=('Consolas', 12, 'bold'),
        bg=cor_botao, fg=cor_texto,
        activebackground=cor_hover, activeforeground=cor_texto,
        relief='flat', bd=0, cursor='hand2', padx=15, pady=5,
        command=popup.destroy
    ).pack(pady=(0, 25))

    #Centraliza o popup em cima da janela do jogo.
    popup.update_idletasks()
    x = janela.winfo_x() + (janela.winfo_width() - popup.winfo_width()) // 2
    y = janela.winfo_y() + (janela.winfo_height() - popup.winfo_height()) // 2
    popup.geometry(f'+{x}+{y}')

    popup.grab_set()    #Bloqueia cliques na janela principal
    janela.wait_window(popup)   #Pausa aqui até o popup ser fechado


def jogar(linha, coluna):
    global jogador_atual

    if tabuleiro[linha][coluna] != " ":
        label_vez.config(text='Posição Ocupada'.upper(), fg=cor_vermelho)
        janela.after(1000, lambda: label_vez.config(
            text=f'Jogador {jogador_atual}', fg=cor_texto
        ))
        return
    
    tabuleiro[linha][coluna] = jogador_atual
    botoes[linha][coluna].config(text=jogador_atual)

    if verificar_vitoria(tabuleiro, jogador_atual):
        mostrar_resultado('FIM DE JOGO', f'Jogador {jogador_atual} venceu!', cor_verde)
        reiniciar()
        return

    if verificar_empate(tabuleiro):
        mostrar_resultado('FIM DE JOGO', 'Empate!', cor_amarelo)
        reiniciar()
        return

    jogador_atual = "⭕" if jogador_atual == "❌" else "❌"
    label_vez.config(text=f'Jogador {jogador_atual}')

def reiniciar():
    global jogador_atual
    jogador_atual = '❌'
    label_vez.config(text=f'Jogador {jogador_atual}')
    for l in range(3):
        for c in range(3):
            tabuleiro[l][c] = " "
            botoes[l][c].config(text=" ")


janela = tk.Tk()
janela.title('Jogo da Velha' )
janela.configure(bg=cor_fundo)
janela.resizable(False, False)

label_vez = tk.Label(
    janela, text=f'Jogador {jogador_atual}',
    font=('Consolas', 16, 'bold'),
    bg=cor_fundo, fg=cor_texto
    )
label_vez.grid(row=0, column=0, columnspan=3, pady=10)

botoes = []
for l in range(3):
    linha_botoes = []
    for c in range(3):
        b = tk.Button(
            janela, text=" ", font=("Arial", 28, "bold"),
            width=4, height=2,
            bg=cor_botao, fg=cor_texto,
            activebackground=cor_hover,
            relief='flat', bd=0, cursor='hand2',
            command=lambda l=l, c=c: jogar(l, c)
        )
        b.grid(row=l + 1, column=c, padx=4, pady=4) # Espaço entre os quadrados
        linha_botoes.append(b)
    botoes.append(linha_botoes)

tk.Button(
    janela, text="Reiniciar", font=('Consolas', 12),
    bg=cor_vermelho, fg="#1e1e2e", relief="flat", cursor="hand2",
    command=reiniciar
).grid(row=4, column=0, columnspan=3, pady=20)

janela.mainloop()