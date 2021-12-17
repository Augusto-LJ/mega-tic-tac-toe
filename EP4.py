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
        '''(Usuario, int, int) --> Jogador
        Esse método é responsável por criar os jogadores. 
        RECEBE um objeto Usuario e dois int, que são , respectivamente, o número que representa o
        tipo de jogador e o número que distingue o Jogador 1 do Jogador 2.
        '''
        if tipoDoJogador == 1:
            return JogadorHumano(numeroDoJogador)
        elif tipoDoJogador == 2:
            return JogadorEstabanado(numeroDoJogador)
        else:
            return JogadorComeCru(numeroDoJogador)

class Tabuleiro:
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
        self.posicoesVazias = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        

    def imprimirConfiguracaoDoJogo (self):
        '''(Tabuleiro) --> None
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
            
        
    def verificaPosicaoVazia (self, linhaDaJogada, colunaDaJogada):
        '''(Tabuleiro, int, int) --> bool
        Verifica se na instância desta classe a posição (linhaDaJogada, colunaDaJogada) está vazia.
        Retorna 'True' caso a posição esteja vazia e 'False' caso contrário.
        '''
        return self.configuracaoDoTabuleiro[linhaDaJogada][colunaDaJogada] == " "
    
    
    def verificaDiagonalPrincipal (self, simboloDoJogador):
        '''(Tabuleiro, str) --> bool
        Retorna True se a diagonal principal possui apenas o símbolo 'simboloDoJogador' e
        False caso contrário.
        '''
        # Armazena os valores que estão na diagonal principal do tabuleiro
        valoresDiagonalPrincipal = [self.__configuracaoDoTabuleiro[0][0],
                                    self.__configuracaoDoTabuleiro[1][1],
                                    self.__configuracaoDoTabuleiro[2][2]]
        # Percorre toda a lista valoresDiagonalPrincipal
        for i in range(3):
            # Caso haja um valor diferente do simbolo do jogador,
            if valoresDiagonalPrincipal[i] != simboloDoJogador:
                # Retorna False
                return False   
        # Se percorrer toda a lista e não tiver nenhum valor diferente, retorna True
        return True
    
    
    def verificaDiagonalSecundaria (self, simboloDoJogador):
        '''(Tabuleiro, str) --> bool
        Retorna True se a diagonal secundária possui apenas o símbolo 'simboloDoJogador' e
        False caso contrário.
        '''
        #Armazena os valores que estão na diagonal secundária do tabuleiro.
        valoresDiagonalSecundaria = [self.__configuracaoDoTabuleiro[0][2],
                                     self.__configuracaoDoTabuleiro[1][1],
                                     self.__configuracaoDoTabuleiro[2][0]]
        # Percorre toda a lista valoresDiagonalSecundaria
        for i in range(3):
            # Caso haja um valor diferente do simbolo do jogador,
            if valoresDiagonalSecundaria[i] != simboloDoJogador:
                #Retorna False
                return False
        # Se percorrer toda a lista e não tiver nenhum valor diferente, retorna True
        return True
    
    
    def verificaLinha(self, numeroDaLinha, simboloDoJogador):
        '''(Tabuleiro, int, str) --> bool
        Retorna True se a linha de numero 'numeroDaLinha' de um objeto do tipo Tabuleiro
        possui apenas o símbolo 'simboloDoJogador' e False caso contrário.
        '''
        # Lista que armazena os valores da linha numeroDaLinha
        valoresDaLinha = [self.configuracaoDoTabuleiro[numeroDaLinha][0], 
                          self.configuracaoDoTabuleiro[numeroDaLinha][1], 
                          self.configuracaoDoTabuleiro[numeroDaLinha][2]]
        # Varre toda a lista valoresDaLinha
        for valor in range(3):
            # Caso haja um valor diferente do simbolo do jogador,
            if valoresDaLinha[valor] != simboloDoJogador:
                # Retorna False
                return False
        # Se percorrer toda a lista e não tiver nenhum valor diferente, retorna True
        return True
    
    
    def verificaColuna(self, numeroDaColuna, simboloDoJogador):
        '''(Tabuleiro, int, str) --> bool
        Retorna True se a coluna de numero 'numeroDaColuna' de um objeto do tipo Tabuleiro
        possui apenas o símbolo 'simboloDoJogador' e False caso contrário.
        '''
        # Lista que armazena os valores da coluna numeroDaColuna
        valoresDaColuna = [self.configuracaoDoTabuleiro[0][numeroDaColuna], 
                           self.configuracaoDoTabuleiro[1][numeroDaColuna], 
                           self.configuracaoDoTabuleiro[2][numeroDaColuna]]
        # Varre toda a lista valoresDaColuna
        for valor in range(3):
            # Caso haja um valor diferente do simbolo do jogador,
            if valoresDaColuna[valor] != simboloDoJogador:
                # Retorna False
                return False
        # Se percorrer toda a lista e não tiver nenhum valor diferente, retorna True
        return True
    

class microTabuleiro(Tabuleiro):
    '''
    Essa classe representa um micro-tabuleiro do Mega-Jogo-da-Velha.
    Herda métodos da classe 'Tabuleiro'.
    '''
    def __init__(self, pos_linha, pos_coluna):
        ''' (microTabuleiro, int, int) -> None
        Método construtor da classe microTabuleiro. Herda métodos da classe Tabuleiro.
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
        '''(macroTabuleiro) --> None
        Método construtor da classe macroTabuleiro. Herda métodos da classe Tabuleiro.
        '''
        # Para herdar
        Tabuleiro.__init__(self)
        self.eh_macro = True
    

class Jogador:
    '''
    Representação mais básica de um tipo de jogador
    '''
    def __init__(self, numeroDoJogador):
        '''(Jogador, int) --> None
        Método construtor da classe Jogador.
        '''
        if numeroDoJogador == 1:
            self.simboloDoJogador = "X"
        else:
            self.simboloDoJogador = "O"
            
        self.vezDeJogar = False
        self.microTabuleirosDisponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
        
    def quaisTabuleirosDisponiveis(self):
        '''(Jogador) --> list
        Esse método retorna a lista dos tabuleiros que ainda estão disponíveis.
        '''
        return self.tabuleirosDisponiveis
        
    
class JogadorHumano(Jogador):
    '''
    Classe que repesenta um jogador do tipo "humano".
    Esse tipo de jogador é controlado por um humano e digita as jogados no teclado do computador.
    '''
    def escolheJogada(self):
        '''(JogadorHumano) --> tuple, int, int
        Esse método define a jogada que será feita pelo Jogador humano.
        RETORNA a tupla qualMicroTabuleiro, que indica em qual micro-tabuleiro a jogada será feita, e
        os inteiros qualLinha e qualColuna que indicam onde a jogada será feito no micro-tabuleiro.
        '''
        # Determina em qual micro-tabuleiro a jogada será feita
        qualLinhaDoMacro = int(input("Digite qual linha do macro-tabuleiro você quer jogar: "))
        qualColunaDoMacro = int(input("Digite qual coluna do macro-tabuleiro você quer jogar: "))
        qualMicroTabuleiro = qualLinhaDoMacro, qualColunaDoMacro
        # Determina em qual posição do micro-tabuleiro a jogada será feita
        qualLinha = int(input("Digite qual linha do micro-tabuleiro você quer jogar: "))
        qualColuna = int(input("Digite qual colunaa do micro-tabuleiro você quer jogar: "))
        
        return qualMicroTabuleiro, qualLinha, qualColuna    


class JogadorEstabanado(Jogador):
    '''
    Classe que representa um jogador do tipo "estabanado".
    Esse tipo de jogador é controlado pelo computador e sempre joga numa posição aleatória do tabuleiro.
    '''
    def escolheMicroTabuleiro(self):
        '''(JogadorEstabanado) --> tuple
        Esse método retorna
        '''
        # Define em qual micro-tabuleiro vai jogar usando o módulo random
        return random.choice(self.microTabuleirosDisponiveis)
    
    def escolhePosicaoNoMicro(self, microTabuleiro):
        '''(JogadorEstabanado, microTabuleiro) --> tuple
        RECEBE um objeto do tipo microTabuleiro
        RETORNA uma tupla que representa a jogada a ser feita.
        Além disso, atualiza a lista das posições vazias de um objeto do tipo microTabuleiro.
        '''
        # Define a jogada aleatoriamente
        jogada = random.choice(microTabuleiro.posicoesVazias)
        indiceDaJogada = microTabuleiro.posicoesVazias.index(jogada)
        # Tira essa posição da lista das posicoes vazias
        del microTabuleiro.posicoesVazias[indiceDaJogada]
                    
        return jogada
    
    
    def fazJogada():
        
        pass
    
    
class JogadorComeCru(Jogador):
    '''
    Classe que representa um jogador do tipo "come-crú".
    Esse tipo de jogador é controlado pelo computador e sempre joga na primeira posição livre do tabuleiro.
    '''
    def escolheMicroTabuleiro(self):
        '''(JogadorComeCru) --> tuple
        Esse método retorna o primeiro micro-tabuleiro disponível.
        '''
        # Define em qual micro-tabuleiro a jogada será feita
        qualMicroTabuleiro = self.microTabuleirosDisponiveis[0]
        return qualMicroTabuleiro
        
        
    def escolheJogada(self, microTabuleiro):
        '''(JogadorComeCru, microTabuleiro) --> tuple
        Esse método retorna o primeiro espaço vazio de um objeto do tipo microTabuleiro.
        '''
        # Define a posição no micro-tabuleiro onde a jogada será feita
        jogada = microTabuleiro.posicoesVazias[0]
        indiceDaJogada = microTabuleiro.posicoesVazias.index(jogada)
        # Tira essa posição da lista das posicoes vazias
        del microTabuleiro.posicoesVazias[indiceDaJogada]
        
        return jogada
       

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
    macro_tabuleiro = macroTabuleiro()
        # Micro-tabuleiros. Os números contidos no nome representam a posição (no formato (x, y)) no macro-tabuleiro
    micro_tabuleiro_00,micro_tabuleiro_01,micro_tabuleiro_02=microTabuleiro(0,0),microTabuleiro(0,1),microTabuleiro(0,2)
    micro_tabuleiro_10,micro_tabuleiro_11,micro_tabuleiro_12=microTabuleiro(1,0),microTabuleiro(1,1),microTabuleiro(1,2)
    micro_tabuleiro_20,micro_tabuleiro_21,micro_tabuleiro_22=microTabuleiro(2,0),microTabuleiro(2,1),microTabuleiro(2,2)
    
    
    # Enquanto ninguém vencer o macro-tabuleiro ou não tiver mais jogadas possíveis, não sai do loop
    while not macro_tabuleiro.tabuleiroAcabou or len(macro_tabuleiro.posicoesVazias) > 0:
        return


'''
# Para chamar a função main automaticamente
if __name__ == '__main__':
    main()
'''
