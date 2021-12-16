# -*- coding: utf-8 -*-

# Importar modulos
import random

## ================================================================================================================== ##

class Usuario():
    '''
    Esta classe representa o usuário do programa. Cria os jogadores e gerencia os tabuleiros.
    '''
    
    def escolhe_jogadores(self):
        '''(Usuario) --> None
        Essa função define o tipo dos 2 jogadores.
        '''
        # Indica se a pessoa já escolheu os jogadores ou não
        escolheu_jogadores = False
        # Variáveis que serão retornadas no final
        escolha_do_jogador_um = None
        escolha_do_jogador_dois = None      
        # Lista com as possíveis escolhas que um usuário pode fazer
        possiveis_escolhas = [1,2,3]
        
        # enquanto o usuário não escolher os jogadores, não sai do loop
        while not escolheu_jogadores:
            # escolhe o jogador 1
            while escolha_do_jogador_um not in possiveis_escolhas:
                escolha_do_jogador_um = int(input("Escolha o tipo do Jogador 1 (X): "))
                if escolha_do_jogador_um not in possiveis_escolhas:
                    print("Comando inválido!")
            # escolhe o jogador 2
            while escolha_do_jogador_dois not in possiveis_escolhas:        
                escolha_do_jogador_dois = int(input("Escolha o tipo do Jogador 2 (O): "))
                if escolha_do_jogador_dois not in possiveis_escolhas:
                    print("Comando inválido!")
                escolheu_jogadores = True
        return escolha_do_jogador_um, escolha_do_jogador_dois
    
    def cria_jogador(self, tipoDoJogador, numeroDoJogador):
        if tipoDoJogador == 1:
            return JogadorHumano(numeroDoJogador)
        elif tipoDoJogador == 2:
            return JogadorEstabanado(numeroDoJogador)
        else:
            return JogadorComeCru(numeroDoJogador)

class Tabuleiro():
    """
    Esta classe representa um tabuleiro qualquer do Mega-jogo-da-velha.
    """   
    
    def __init__(self):
        ''' (Tabuleiro) -> None
        Método construtor da classe Tabuleiro.
        RECEBE os inteiros pos_linha e pos_coluna que representam a posição [pos_linha][pos_coluna]
        do micro-tabuleiro no macro-tabuleiro e um str 'tipo', que indica se é um micro-tabuleiro ou macro-tabuleiro.
        '''
        self.configuracaoDoTabuleiro = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]
        self.tabuleiroAcabou = False
        

    #Este método imprime a configuraçao atual do jogo da velha 3x3.
    def imprimirConfiguracaoDoJogo (self):
        '''
        Imprime na saída de dados o micro-tabuleiro ou o macro-tabuleiro que chamou a função.
        '''
        #Imprime a primeira linha do tabuleiro.
        print("\n\t {} | {} | {} ".format(self.configuracaoDoTabuleiro[0][0], self.configuracaoDoTabuleiro[0][1], self.configuracaoDoTabuleiro[0][2]))
        print('\t---+---+---')
        #Imprime a segunda linha do tabuleiro.
        print("\t {} | {} | {} ".format(self.configuracaoDoTabuleiro[1][0], self.configuracaoDoTabuleiro[1][1], self.configuracaoDoTabuleiro[1][2]))
        print('\t---+---+---')
        #Imprime a terceira linha do tabuleiro.
        print("\t {} | {} | {} \n".format(self.configuracaoDoTabuleiro[2][0], self.configuracaoDoTabuleiro[2][1], self.configuracaoDoTabuleiro[2][2]))
        
        #Checa se é macro-tabuleiro ou micro-tabuleiro
        if self.eh_macro:
            print(f"   Macro-Tabuleiro")
        else:
            print(f"Micro-Tabuleiro[{self.pos_lin}][{self.pos_col}]")
        
        
    #Verifica se na instância desta classe a posição (linhaDaJogada, colunaDaJogada) está vazia.
    #Retorna True caso a posição esteja vazia e a jogada for feita e False caso contrário.
    def verificaPosicaoVazia (self, linhaDaJogada, colunaDaJogada, simboloDoJogador):
        if self.colunasDoTabuleiroGetter[linhaDaJogada][colunaDaJogada] == " ":
            self.__configuracaoDoTabuleiro[linhaDaJogada][colunaDaJogada] = simboloDoJogador
            return True
        return False
    #Verifica se a diagonal principal possúi apenas um símbolo identificador (X ou O)
    #Retorna True caso haja somente um tipo de símbolo e False caso contrário.
    def verificarDiagonalPrincipal (self, simboloDoJogador):
        valoresDiagonalPrincipal = [self.__configuracaoDoTabuleiro[0][0], self.__configuracaoDoTabuleiro[1][1], self.__configuracaoDoTabuleiro[2][2]]
        for i in range (len (valoresDiagonalPrincipal)):
            if valoresDiagonalPrincipal[i] != simboloDoJogador:
                return False      
        return True
    
    #Mesma função que "verificarDiagonalPrincipal", mas agora para a diagonal secundária.
    def verificarDiagonalSecundaria (self, simboloDoJogador):
        #Armazena os valores que estão na diagonal secundária do tabuleiro.
        valoresDiagonalSecundaria = [self.__configuracaoDoTabuleiro[0][2], self.__configuracaoDoTabuleiro[1][1], self.__configuracaoDoTabuleiro[2][0]]
        #Percorre a lista acima.
        for i in range (len (valoresDiagonalSecundaria)):
            #Caso haja algum valor diferente do qual o simbolo do jogador pertence.
            if valoresDiagonalSecundaria[i] != simboloDoJogador:
                #Retorna 0 e sai da função.
                return False
        #Retorna 1 caso contrário.
        return True
    
    #Verifica se a primeira linha do tabuleiro possui apenas um símbolo identificador (X ou O)
    #Retorna 1 caso haja somente um tipo de símbolo e 0 caso contrário.
    def verificarPrimeiraLinha (self, simboloDoJogador):
        #Armazena os valores contidos na primeira linha do tabuleiro.
        valoresPrimeiraLinha = [self.__configuracaoDoTabuleiro[0][0], self.__configuracaoDoTabuleiro[0][1], self.__configuracaoDoTabuleiro[0][2]]
        #Percorre a lista acima e verifica se há um valor diferente do qual equivale o simbolo do jogador passado como parâmetro.
        for valor in range (len (valoresPrimeiraLinha)):
            #Caso haja um valor diferente do simbolo do jogador.
            if valoresPrimeiraLinha[valor] != simboloDoJogador:
                #Sai da função e retorna 0.
                return False
        #Retorna 1 caso contrário.
        return True
    
    #Verifica se a segunda linha do tabuleiro possui apenas um símbolo identificador (X ou O).
    #Retorna 1 caso haja somente um tipo de símbolo e 0 caso contrário.
    def verificarSegundaLinha (self, simboloDoJogador):
        #Armazena os valores contidos na primeira linha do tabuleiro.
        valoresSegundaLinha = [self.__configuracaoDoTabuleiro[1][0], self.__configuracaoDoTabuleiro[1][1], self.__configuracaoDoTabuleiro[1][2]]
        #Percorre a lista acima e verifica se há um valor diferente do qual equivale o simbolo do jogador passado como parâmetro.
        for valor in range (len (valoresSegundaLinha)):
            #Caso haja algum valor diferente de simbolo do jogador.
            if valoresSegundaLinha[valor] != simboloDoJogador:
                #Sai da função e retorna 0.
                return False
        #Retorna 1 caso contrário.
        return True
    
    #Verifica se a terceira linha do tabuleiro possúi apenas um símbolo identificador (X ou O).
    #Retorna 1 caso haja somente um tipo de símbolo e 0 caso contrário.
    def verificarTerceiraLinha (self, simboloDoJogador):
        #Armazena os valores contidos na primeira linha do tabuleiro.
        valoresTerceiraLinha = [self.__configuracaoDoTabuleiro[2][0], self.__configuracaoDoTabuleiro[2][1], self.__configuracaoDoTabuleiro[2][2]]
        #Percorre a lista acima e verifica se há um valor diferente do qual equivale o simbolo do jogador passado como parâmetro.
        for valor in range (len (valoresTerceiraLinha)):
            #Caso haja algum valor diferente na lista que difira do símbolo do jogador.
            if valoresTerceiraLinha[valor] != simboloDoJogador:
                #Sai da função e retorna 0.
                return False
        #Retorna 1 caso contrário.
        return True
    
    #Verifica se a primeira coluna do tabuleiro possui apenas um símbolo identificador (X ou O).
    #Retorna 1 caso haja somente um tipo de símbolo e 0 caso contrário.
    def verificarPrimeiraColuna (self, simboloDoJogador):
        #Armazena os valores contidos na primeira coluna do tabuleiro.
        valoresPrimeiraColuna = [self.__configuracaoDoTabuleiro[0][0], self.__configuracaoDoTabuleiro[0][1], self.__configuracaoDoTabuleiro[0][2]]
        #Percorre a lista dos valores da primeira coluna.
        for valor in range (len (valoresPrimeiraColuna)):
            #Caso haja um valor diferente do símbolo do jogador.
            if valoresPrimeiraColuna[valor] != simboloDoJogador:
                #Sai da função e retorna 0.
                return False
        #Retorna 1 caso contrário.
        return True
    
    #Verifica se a segunda coluna do tabuleiro possui apenas um símbolo identificador (X ou O).
    #Retorna 1 caso haja somente um tipo de símbolo e 0 caso contrário.
    def verificarSegundaColuna (self, simboloDoJogador):
        #Armazena os valores contidos na segunda coluna do tabuleiro.
        valoresSegundaColuna = [self.__configuracaoDoTabuleiro[1][0], self.__configuracaoDoTabuleiro[1][1], self.__configuracaoDoTabuleiro[1][2]]
        #Percorre a lista dos valores da segunda coluna.
        for valor in range (len (valoresSegundaColuna)):
            #Caso haja um valor diferente do símbolo do jogador.
            if valoresSegundaColuna[valor] != simboloDoJogador:
                #Sai da função e retorna 0.
                return False
        #Retorna 1 caso contrário.
        return True

    #Verifica se a terceira coluna do tabuleiro possui apenas um símbolo identificador (X ou O).
    #Retorna 1 caso haja somente um tipo de símbolo e 0 caso contrário.
    def verificarTerceiraColuna (self, simboloDoJogador):
        #Armazena os valores contidos na terceira coluna do tabuleiro.
        valoresTerceiraColuna = [self.__configuracaoDoTabuleiro[2][0], self.__configuracaoDoTabuleiro[2][1], self.__configuracaoDoTabuleiro[2][2]]
        #Percorre a lista dos valores da terceira coluna.
        for valor in range (len (valoresTerceiraColuna)):
            #Caso haja um valor diferente do símbolo do jogador.
            if valoresTerceiraColuna[valor] != simboloDoJogador:
                #Sai da função e retorna 0.
                return False
        #Retorna 1 caso contrário.
        return True

class microTabuleiro(Tabuleiro):
    '''
    Essa classe representa um micro-tabuleiro do Mega-Jogo-da-Velha.
    Herda métodos da classe 'Tabuleiro'.
    '''
    def __init__(self, pos_linha, pos_coluna):
        ''' (microTabuleiro, int, int) -> None
        Método construtor da classe Tabuleiro.
        RECEBE os inteiros pos_linha e pos_coluna que representam a posição [pos_linha][pos_coluna]
        do micro-tabuleiro no macro-tabuleiro.
        '''
        # para herdar
        Tabuleiro.__init__(self)
        # posição do micro-tabuleiro no macro-tabuleiro
        self.pos_lin = pos_linha
        self.pos_col = pos_coluna
        # para saber se é micro ou macro
        self.eh_macro = False
        
class macroTabuleiro(Tabuleiro):
    '''
    Essa classe representa um macro-tabuleiro do Mega-Jogo-da-Velha.
    Herda métodos da classe 'Tabuleiro'.
    '''
    def __init__(self):
        # para herdar
        Tabuleiro.__init__(self)
        self.eh_macro = True
    

class Jogador:
    '''
    Representação mais básica de um tipo de jogador
    '''
    def __init__(self, numeroDoJogador):
        if numeroDoJogador == 1:
            self.simboloDoJogador = "X"
        else:
            self.simboloDoJogador = "O"
            
        self.vezDeJogar = False
        self.tabuleirosDisponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
class JogadorHumano(Jogador):
    '''
    Classe que repesenta um jogador do tipo "humano".
    Esse tipo de jogador é controlado por um humano e digita as jogados no teclado do computador.
    '''
    def escolheJogada(self):
        # Determina em qual micro-tabuleiro a jogada será feita
        qualMicroTabuleiro = input("Em qual tabuleiro você quer jogar?")
        # Determina em qual posição do micro-tabuleiro a jogada será feita
        qualLinha, qualColuna = int(input("Qual é a sua jogada?"))
        return qualMicroTabuleiro, qualLinha, qualColuna    

class JogadorEstabanado(Jogador):
    '''
    Classe que representa um jogador do tipo "estabanado".
    Esse tipo de jogador é controlado pelo computador e sempre joga numa posição aleatória do tabuleiro.
    '''
    def escolheJogada(self):
        # Define qual micro-tabuleiro, usando o módulo random
        qualMicroTabuleiro = random.choice(self.tabuleirosDisponiveis)
        # Define qual lugar do micro-tabuleiro a jogada será feita
        
        
                    
    
    
    
    
class JogadorComeCru(Jogador):
    '''Classe que representa um jogador do tipo "come-crú".
    Esse tipo de jogador é controlado pelo computador e sempre joga na primeira posição livre do tabuleiro.
    '''
    def escolheJogada(self):
        pass
       
    

## fazer a função 'imprima(x, y)' para imprimir o tabuleiro de posição x,y 
## fazer a função 'imprimaMacro() para imprimir o macro tabuleiro

## ========================================================================================================== ##

def main():
    ''' 
    Função principal do programa, inicializa o jogo.
    '''
    print("Bem-vindo(a) ao Mega Jogo da Velha!\n")
    print("Abaixo estão listados os tipos de jogadores:")
    print("1. Jogador humano\n2. Jogador estabanado\n3. Jogador come-crú")
    
    # Cria a instância que representa o usuário
    usuario = Usuario()
    
    # Escolhe o tipo dos dois jogadores
    numero_jogador_um, numero_jogador_dois = usuario.escolhe_jogadores() 
    
    # Cria os dois jogadores
    jogador_um = usuario.cria_jogador(numero_jogador_um, 1)
    jogador_dois = usuario.cria_jogador(numero_jogador_dois, 2)
    
    # Decide aleatoriamente qual jogador vai começar, sorteando '1' ou '2'
    numero_de_quem_comeca = random.randrange(1,3)
    if numero_de_quem_comeca == 1:
        jogador_um.vezDeJogar = True
    else:
        jogador_dois.vezDeJogar = True
    
    # Aqui são criados o macro-tabuleiro e os 9 micro-tabuleiros
        # Macro-tabuleiro:
    macro_tabuleiro = macroTabuleiro()
        # Micro-tabuleiros. Os números contidos no nome representam a posição (no formato (x, y)) no macro-tabuleiro
    micro_tabuleiro_00 = microTabuleiro(0,0)
    micro_tabuleiro_01 = microTabuleiro(0,1)
    micro_tabuleiro_02 = microTabuleiro(0,2)
    micro_tabuleiro_10 = microTabuleiro(1,0)
    micro_tabuleiro_11 = microTabuleiro(1,1)
    micro_tabuleiro_12 = microTabuleiro(1,2)
    micro_tabuleiro_20 = microTabuleiro(2,0)
    micro_tabuleiro_21 = microTabuleiro(2,1)
    micro_tabuleiro_22 = microTabuleiro(2,2)
    
    
    
    
    
    # Enquanto ninguém vencer o macro-tabuleiro, não sai do loop
    while not macro_tabuleiro.tabuleiroAcabou:
        return
        
    
    
    
t = microTabuleiro(0,0)
jog = JogadorEstabanado(1)
jog.escolheJogada()


'''
# Para chamar a função main automaticamente
if __name__ == '__main__':
    main()
'''
