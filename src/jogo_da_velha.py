# IMPORTANDO AS BIBLIOTECAS QUE USAREMOS NO 'GAME'.
import random  # Gera jogadas aleatórias para o computador no modo single player.
import time    # Utilizada para pausas no jogo (não usada atualmente, mas pode ser útil).
import os      # Biblioteca para comandos no sistema operacional, usada para limpar a tela.

# Cabeçalho do jogo
# CRIAMOS UMA VARIÁVEL PARA ARMAZENAR O CABEÇALHO DO NOSSO JOGO
cabecalho = '''
# =====================================================
#                  JOGO DA VELHA v0.001
# =====================================================
#  Bem-vindo ao jogo da velha! Dois jogadores (X e O)
#  se enfrentam para preencher uma linha, coluna ou
#  diagonal com três de seus símbolos consecutivos.
#  Divirta-se e que vença o melhor!!!   devmoisessantos
# =====================================================
'''

# Função para exibir o tabuleiro
def exibir_tabuleiro():  # DEFINIMOS O NOME DA NOSSA FUNÇÃO QUE EXIBE O TABULEIRO
    print("\n")  # ADICIONA UMA QUEBRA DE LINHA ANTES DO TABULEIRO
    for i in range(3):  # LOOP QUE PASSA POR 3 LINHAS (0 A 2) DO TABULEIRO
        linha = " | ".join(tabuleiro[i * 3:(i + 1) * 3])  # EXIBE UMA LINHA DO TABULEIRO COM SEPARADORES
        print(f" {linha} ")  # IMPRIME A LINHA FORMATADA
        if i < 2:  # SE NÃO FOR A ÚLTIMA LINHA, ADICIONA O SEPARADOR VISUAL ABAIXO
            print("---|---|---")
    print("\n")  # ADICIONA QUEBRA DE LINHA APÓS O TABULEIRO

# Tabuleiro global
tabuleiro = [" " for _ in range(9)]  # TABULEIRO GLOBAL VAZIO PARA ARMAZENAR AS JOGADAS

# Função para verificar vitória
def verificar_vitoria(simbolo):  # FUNÇÃO PARA VERIFICAR SE HÁ VENCEDOR
    combinacoes_vencedoras = [  # LISTA DE COMBINAÇÕES VENCEDORAS
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
        (0, 4, 8), (2, 4, 6)              # Diagonais
    ]
    for combinacao in combinacoes_vencedoras:  # VERIFICA SE TODAS AS POSIÇÕES DE UMA COMBINAÇÃO TEM O MESMO SÍMBOLO
        if all(tabuleiro[i] == simbolo for i in combinacao):
            return True  # RETORNA VERDADEIRO SE HOUVER VITÓRIA
    return False  # RETORNA FALSO SE NÃO HOUVER VITÓRIA

# Função para limpar a tela
def limpar_tela():  # LIMPA A TELA NO TERMINAL, DEPENDENDO DO SISTEMA OPERACIONAL
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para o menu inicial
def menu():
    print(cabecalho)  # IMPRIME O CABEÇALHO DO JOGO
    while True:
        print('''  # MENU PRINCIPAL COM OPÇÕES DO JOGO
Menu Principal:
1. Instruções
2. Jogar Sozinho (Modo Single)
3. Jogar com Amigo
4. Sobre
5. Sair
        ''')
        exibir_tabuleiro()  # EXIBE O TABULEIRO NUMERADO
        escolha = input("Escolha uma opção: ")  # RECEBE A OPÇÃO DO JOGADOR
        limpar_tela()  # LIMPA A TELA APÓS ESCOLHA

        if escolha == "1":
            show_info()  # EXIBE INSTRUÇÕES DO JOGO
        
        elif escolha == "2":
            iniciar_jogo("single")  # INICIA O MODO SINGLE PLAYER
        
        elif escolha == "3":
            iniciar_jogo("duo")  # INICIA O MODO DE DOIS JOGADORES
        
        elif escolha == "4":
            print("\nJogo da Velha - Versão 0.001\nDesenvolvido por devmoisessantos")  # EXIBE INFORMAÇÕES SOBRE O JOGO
        
        elif escolha == "5":
            print("Saindo do jogo. Até logo!")  # MENSAGEM DE SAÍDA
            break  # ENCERRA O LOOP E SAI DO JOGO
    
        else:
            print("Opção inválida. Tente novamente.")  # MENSAGEM PARA OPÇÃO INVÁLIDA
        
        input("Pressione qualquer tecla para continuar...")  # PAUSA APÓS CADA SELEÇÃO DO MENU
        limpar_tela()  # LIMPA A TELA PARA EXIBIR O MENU NOVAMENTE

def show_info():  # EXIBE AS INSTRUÇÕES DO JOGO
    print("Instruções: Preencha uma linha, coluna ou diagonal com três símbolos (X ou O) para vencer!")
    exibir_tabuleiro()  # EXIBE O TABULEIRO

# Função para iniciar o jogo no modo escolhido
def iniciar_jogo(modo):
    global tabuleiro
    tabuleiro = [str(i) for i in range(9)]  # INICIA O TABULEIRO NUMERADO
    while True:
        limpar_tela()  # LIMPA A TELA
        exibir_tabuleiro()  # EXIBE O TABULEIRO ATUALIZADO
        if modo == "single":
            jogar_single()  # CHAMA O MODO SINGLE PLAYER
        elif modo == "duo":
            jogar_duo()  # CHAMA O MODO DE DOIS JOGADORES
        if input("Deseja jogar novamente? (s/n): ").lower() != "s":  # PERGUNTA SE QUER JOGAR NOVAMENTE
            break  # SAI DO JOGO SE A RESPOSTA FOR "N"

# Função para o modo single player
def jogar_single():
    global tabuleiro
    tabuleiro = [" " for _ in range(9)]  # INICIA O TABULEIRO VAZIO PARA O JOGO
    while True:
        # Jogada do jogador
        try:
            posicao = int(input("Escolha sua posição (0-8): "))  # PEDE AO JOGADOR PARA ESCOLHER UMA POSIÇÃO
            if posicao < 0 or posicao > 8:  # VERIFICA SE A POSIÇÃO É VÁLIDA
                print("Posição inválida. Escolha entre 0 e 8.")
                continue
        except ValueError:
            print("Por favor, insira um número válido.")  # VALIDA SE A ENTRADA É UM NÚMERO INTEIRO
            continue

        if tabuleiro[posicao] == " ":  # VERIFICA SE A POSIÇÃO ESTÁ VAZIA
            tabuleiro[posicao] = "X"  # JOGADOR MARCA A POSIÇÃO COM "X"
        else:
            print("Essa posição já está ocupada!")  # MENSAGEM SE A POSIÇÃO ESTIVER OCUPADA
            continue
        exibir_tabuleiro()  # ATUALIZA O TABULEIRO

        # Verifica se o jogador venceu
        if verificar_vitoria("X"):  # VERIFICA SE O JOGADOR VENCEU
            print("Parabéns! Você venceu!")
            break

        # Jogada aleatória do computador
        posicoes_disponiveis = [i for i, v in enumerate(tabuleiro) if v == " "]  # LISTA DE POSIÇÕES DISPONÍVEIS
        if posicoes_disponiveis:
            jogada_computador = random.choice(posicoes_disponiveis)  # COMPUTADOR ESCOLHE UMA POSIÇÃO ALEATÓRIA
            tabuleiro[jogada_computador] = "O"  # MARCA A POSIÇÃO COM "O"
            print(f"Computador jogou na posição: {jogada_computador}")
            exibir_tabuleiro()  # ATUALIZA O TABULEIRO

            # Verifica se o computador venceu
            if verificar_vitoria("O"):  # VERIFICA SE O COMPUTADOR VENCEU
                print("O computador venceu! Tente novamente.")
                break
        else:
            print("Empate! Não há mais jogadas disponíveis.")  # MENSAGEM DE EMPATE
            break

# Função para o modo de dois jogadores
def jogar_duo():
    global tabuleiro
    tabuleiro = [" " for _ in range(9)]  # INICIA O TABULEIRO VAZIO PARA O JOGO .
    while True:
        for jogador in ["X", "O"]:  # ALTERNATIVA ENTRE OS JOGADORES X E O
            try:
                posicao = int(input(f"Jogador {jogador}, escolha sua posição (0-8): "))  # RECEBE A POSIÇÃO DO JOGADOR
                if posicao < 0 or posicao > 8:
                    print("Posição inválida. Escolha entre 0 e 8.")  # VALIDA A POSIÇÃO
                    continue
            except ValueError:
                print("Por favor, insira um número válido.")  # VALIDA A ENTRADA NUMÉRICA
                continue

            if tabuleiro[posicao] == " ":  # VERIFICA SE A POSIÇÃO ESTÁ DISPONÍVEL
                tabuleiro[posicao] = jogador  # MARCA A POSIÇÃO COM O SÍMBOLO DO JOGADOR ATUAL
                exibir_tabuleiro()  # EXIBE O TABULEIRO
                if verificar_vitoria(jogador):  # VERIFICA SE O JOGADOR ATUAL VENCEU
                    print(f"Jogador {jogador} venceu! Parabéns!")
                    return  # TERMINA O JOGO SE HOUVER UM VENCEDOR
            else:
                print("Essa posição já está ocupada. Tente outra.")  # MENSAGEM SE A POSIÇÃO JÁ ESTIVER OCUPADA

# Executa o menu principal
menu()  # INICIA O JOGO CHAMANDO O MENU PRINCIPAL
