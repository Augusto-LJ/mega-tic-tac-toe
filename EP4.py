# -*- coding: utf-8 -*-
# Importar modulos
import random
import numpy as np
## ================================================================================================================== ##
class Usuario():
    '''
    Esta classe representa o usuário do programa. Cria os jogadores e gerencia os tabuleiros.
    '''
    def criaArrayDeTabuleiros(self, listaDeMicroTabuleiros):
        '''(Usuario, list) --> None
        Essa função recebe uma lista contendo todos os tabuleiros e cria um array
        dessa lista usando o módulo numpy
        '''
        self.arrayDeTabuleiros = np.array(listaDeMicroTabuleiros)
        
        
    def escolhe_jogadores(self):
        '''(Usuario) --> None
        Essa função define o tipo dos 2 jogadores.
        '''
        # Indica se a pessoa já escolheu os jogadores ou não
        escolheu_jogadores = False
        # Variáveis que serão retornadas no final
        escolha_do_jogador_um = escolha_do_jogador_dois = None
        # Lista com as possíveis escolhas que um usuário pode fazer
        possiveis_escolhas = ["1","2","3"]  
        # enquanto o usuário não escolher os jogadores, não sai do loop
        while not escolheu_jogadores:
            # escolhe o jogador 1
            while escolha_do_jogador_um not in possiveis_escolhas:
                escolha_do_jogador_um = input("Escolha o tipo do Jogador 1 (X): ")
                if escolha_do_jogador_um not in possiveis_escolhas:
                    print("Comando inválido!")
            escolha_do_jogador_um = int(escolha_do_jogador_um)
            # escolhe o jogador 2
            while escolha_do_jogador_dois not in possiveis_escolhas:        
                escolha_do_jogador_dois = input("Escolha o tipo do Jogador 2 (O): ")
                if escolha_do_jogador_dois not in possiveis_escolhas:
                    print("Comando inválido!")
            escolha_do_jogador_dois = int(escolha_do_jogador_dois)
            escolheu_jogadores = True
        return escolha_do_jogador_um, escolha_do_jogador_dois
    
    
    def cria_jogador(self, tipoDoJogador, simboloDoJogador):
        '''(Usuario, int, str) --> Jogador
        Esse método é responsável por criar os jogadores. 
        RECEBE um objeto Usuario, o int tipoDoJogador que representa o tipo de jogador,
        e um str 'simboloDoJogador' que indica o símbolo que distingue o Jogador 1 do Jogador 2.
        '''
        if tipoDoJogador == 1:
            return JogadorHumano(simboloDoJogador)
        elif tipoDoJogador == 2:
            return JogadorEstabanado(simboloDoJogador)
        else:
            return JogadorComeCru(simboloDoJogador)
        
    def jogadaDaVez(self, jogador_um, jogador_dois, macroTabuleiro):
        '''(Usuario, Jogador, Jogador) --> None
        Esse método faz o jogador da vez realizar sua jogada
        '''
        # Se for a vez do jogador_um
        if jogador_um.vezDeJogar:
            print("\n ----- Vez do Jogador 1 ----- ")
            qualMicroTabuleiro = jogador_um.escolheMicroTabuleiro()
            # Apelido para o micro-tabuleiro
            microTabuleiro = self.arrayDeTabuleiros[qualMicroTabuleiro]
            if jogador_um.tipoDeJogador == "estabanado" or jogador_um.tipoDeJogador == "comecru":
                qualPosicao = jogador_um.escolhePosicaoNoMicro(microTabuleiro)
                jogador_um.fazJogada(self, microTabuleiro, qualPosicao, qualMicroTabuleiro)

            else:
                qualPosicao = jogador_um.escolhePosicaoNoMicro()
                # Verifica se jogada é válida ou não
                if jogador_um.verificaJogada(microTabuleiro, qualPosicao):
                    jogador_um.fazJogada(self, microTabuleiro, qualPosicao, qualMicroTabuleiro)
                else:
                    print("\nJogada inválida!")
                    self.jogadaDaVez(jogador_um, jogador_dois, macroTabuleiro)
                    return       
            # Faz verificações no micro-tabuleiro jogado recentemente
            if microTabuleiro.verificaSeGanhouTabuleiro(qualPosicao, jogador_um):
                microTabuleiro.posicoesVazias = []
                indice = jogador_um.microTabuleirosDisponiveis.index(qualMicroTabuleiro)
                # Retira esse micro-tabuleiro da lista dos disponíveis
                del jogador_um.microTabuleirosDisponiveis[indice]
                # Marca no macro-tabuleiro
                macroTabuleiro.marcaVitoria(qualMicroTabuleiro, jogador_um)
                if macroTabuleiro.verificaSeGanhouTabuleiro(qualMicroTabuleiro, jogador_um):
                    self.venceuJogo(jogador_um, macroTabuleiro)
        # Se for a vez do jogador_dois
        else:
            print("\n ----- Vez do Jogador 2 ----- ")
            qualMicroTabuleiro = jogador_dois.escolheMicroTabuleiro()
            # Apelido para o micro-tabuleiro
            microTabuleiro = self.arrayDeTabuleiros[qualMicroTabuleiro]
            if jogador_dois.tipoDeJogador == "estabanado" or jogador_dois.tipoDeJogador == "comecru":
                qualPosicao = jogador_dois.escolhePosicaoNoMicro(microTabuleiro)
                jogador_dois.fazJogada(self, microTabuleiro, qualPosicao, qualMicroTabuleiro)
            else:
                qualPosicao = jogador_dois.escolhePosicaoNoMicro()
                # Verifica se jogada é válida ou não
                if jogador_dois.verificaJogada(microTabuleiro, qualPosicao):
                    jogador_dois.fazJogada(self, microTabuleiro, qualPosicao, qualMicroTabuleiro)
                else:
                    print("\nJogada inválida!")
                    self.jogadaDaVez(jogador_um, jogador_dois, macroTabuleiro)
                    return
            # Faz verificações no micro-tabuleiro jogado recentemente
            if microTabuleiro.verificaSeGanhouTabuleiro(qualPosicao, jogador_dois):
                microTabuleiro.posicoesVazias = []
                indice = jogador_dois.microTabuleirosDisponiveis.index(qualMicroTabuleiro)
                # Retira esse micro-tabuleiro da lista dos disponíveis
                del jogador_dois.microTabuleirosDisponiveis[indice]
                # Marca no macro-tabuleiro
                macroTabuleiro.marcaVitoria(qualMicroTabuleiro, jogador_dois)
                if macroTabuleiro.verificaSeGanhouTabuleiro(qualMicroTabuleiro, jogador_dois):
                    self.venceuJogo(jogador_dois, macroTabuleiro)
                
        # Troca a vez
        jogador_um.vezDeJogar = not jogador_um.vezDeJogar
        jogador_dois.vezDeJogar = not jogador_dois.vezDeJogar
        return
    
    def mandaImprimir(self):
        '''(MicroTabuleiro, tuple, Usuario) --> None
        Esse método chama o método 'imprimirTabuleiro' para um dado micro-tabuleiro.
        '''
        # Lista que armazenas as escolhas válidas e possíveis
        possiveis_escolhas = ["0","1","2"]
        escolheu_linha = False
        escolheu_coluna = False
        # Enquanto não escolher a linhas
        while not escolheu_linha:
            qualLinha = input("Por favor informe a linha onde está o micro-tabuleiro que você quer imprimir: ")
            if qualLinha not in possiveis_escolhas:
                print("Comando inválido!")
            else:
                qualLinha = int(qualLinha)
                escolheu_linha = True
        # Enquanto não escolher a coluna
        while not escolheu_coluna:
            qualColuna = input("Por favor informe a coluna onde está o micro-tabuleiro que você quer imprimir: ")
            if qualColuna not in possiveis_escolhas:
                print("Comando inválido!")
            else:
                qualColuna = int(qualColuna)
                escolheu_coluna = True
        qualLinha, qualColuna = int(qualLinha), int(qualColuna)
        qualMicro = qualLinha, qualColuna
        print(self.arrayDeTabuleiros[(qualMicro)].imprimirTabuleiro())
        return
            
    
    def menuDeOpcoes(self, MacroTabuleiro, jogador_um):
        '''(Usuario, MacroTabuleiro) --> None
        Esse método apresenta um menu de opções que o jogador pode escolher antes
        de prosseguir com o jogo
        '''
        print("\nEscolha uma opção escrevendo o número correspondente: ")
        escolhaDoJogador = None
        while not escolhaDoJogador == 1:
            escolhaDoJogador = input("1) Prosseguir para a jogada\n2) Imprimir macro-tabuleiro\n3) Mostrar micro-tabuleiros disponíveis\n4) Imprimir algum micro-tabuleiro\nO que você gostaria de fazer? ")
            if escolhaDoJogador == "1":   # prosseguir com o jogo
                return
            elif escolhaDoJogador == "2": # imprimir macro-tabuleiro
                strDoMacro = MacroTabuleiro.imprimirTabuleiro()
                print(strDoMacro)
            elif escolhaDoJogador == "3": # mostrar micro-tabuleiros disponíiveis
                print(f'\n Os micro-tabuleiros disponíveis são:\n {jogador_um.microTabuleirosDisponiveis}')
            elif escolhaDoJogador == "4": # imprimir algum micro-tabuleiro
                self.mandaImprimir()
            else:
                print("\nComando inválido!")
                self.menuDeOpcoes(MacroTabuleiro, jogador_um)
                return
        return

    
    def venceuJogo(self, jogador, macroTabuleiro):
        '''(Usuario, Jogador, MacroTabuleiro) --> None
        Esse método sinaliza que algum dos jogadores venceu o jogo, finalizando a partida
        '''
        macroTabuleiro.tabuleiroAcabou = True
        if jogador.simboloDoJogador == "X":
            print("Parabéns JOGADOR 1 por vencer o Mega Jogo da Velha!!")
        else:
            print("Parabéns JOGADOR 2 por vencer o Mega Jogo da Velha!!")
        return


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
        

    def imprimirTabuleiro (self):
        '''(Tabuleiro) --> None
        Imprime na saída de dados o micro-tabuleiro ou o macro-tabuleiro que chamou a função.
        '''
        strDoTabuleiro ="\n\t {} | {} | {} \n\t---+---+---\n\t {} | {} | {} \n\t---+---+---\n\t {} | {} | {} \n".format(self.configuracaoDoTabuleiro[0][0],self.configuracaoDoTabuleiro[0][1],self.configuracaoDoTabuleiro[0][2],self.configuracaoDoTabuleiro[1][0],self.configuracaoDoTabuleiro[1][1],self.configuracaoDoTabuleiro[1][2],self.configuracaoDoTabuleiro[2][0],self.configuracaoDoTabuleiro[2][1],self.configuracaoDoTabuleiro[2][2])
        #Checa se é macro-tabuleiro ou micro-tabuleiro
        if self.ehMacro:
            strDoTabuleiro +="\n  Macro-Tabuleiro"
        else:
            strDoTabuleiro +="\nMicro-Tabuleiro[{}][{}]".format(self.pos_lin, self.pos_col)
            
        return strDoTabuleiro
            
        
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
        valoresDiagonalPrincipal = [self.configuracaoDoTabuleiro[0][0],
                                    self.configuracaoDoTabuleiro[1][1],
                                    self.configuracaoDoTabuleiro[2][2]]
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
        valoresDiagonalSecundaria = [self.configuracaoDoTabuleiro[0][2],
                                     self.configuracaoDoTabuleiro[1][1],
                                     self.configuracaoDoTabuleiro[2][0]]
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
    
    def verificaSeGanhouTabuleiro(self, qualPosicao, jogador):
        '''(Tabuleiro, tuple, Jogador) --> bool
        Verifica se algum dos dois jogadores ganhou o Tabuleiro em questão.
        '''
        diagonalPrincipal = self.verificaDiagonalPrincipal(jogador.simboloDoJogador)
        diagonalSecundaria = self.verificaDiagonalSecundaria(jogador.simboloDoJogador)
        linha = self.verificaLinha(qualPosicao[0], jogador.simboloDoJogador)
        coluna = self.verificaColuna(qualPosicao[1], jogador.simboloDoJogador)
        # Se alguém tiver ganhado o tabuleiro de alguma forma
        if diagonalPrincipal or diagonalSecundaria or linha or coluna:
            # Se for macro-tabuleiro:
            if self.ehMacro:
                self.tabuleiroAcabou = True           
            return True
        return False
            

class MicroTabuleiro(Tabuleiro):
    '''
    Essa classe representa um micro-tabuleiro do Mega-Jogo-da-Velha.
    Herda métodos da classe 'Tabuleiro'.
    '''
    def __init__(self, pos_linha, pos_coluna):
        ''' (MicroTabuleiro, int, int) -> None
        Método construtor da classe MicroTabuleiro. Herda métodos da classe Tabuleiro.
        RECEBE os inteiros pos_linha e pos_coluna que representam a posição [pos_linha][pos_coluna]
        do micro-tabuleiro no macro-tabuleiro.
        '''
        # para herdar
        Tabuleiro.__init__(self)
        # posição do micro-tabuleiro no macro-tabuleiro
        self.pos_lin = pos_linha
        self.pos_col = pos_coluna
        # para saber se é micro ou macro
        self.ehMacro = False
        
        
    def reiniciaMicroTabuleiro(self):
        '''(MicroTabuleiro) --> none
        Esse método 'limpa' todas as posições de um micro-tabuleiro que gerou empate
        '''
        # Laço duplo para percorrer todas as linhas e colunas de um micro-tabuleiro
        for linha in range(3):
            for coluna in range(3):
                self.configuracaoDoTabuleiro[linha][coluna] = " "
        # Atualiza a lista de posições vazias desse micro-tabuleiro
        self.posicoesVazias = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
        
class MacroTabuleiro(Tabuleiro):
    '''
    Essa classe representa um macro-tabuleiro do Mega-Jogo-da-Velha.
    Herda métodos da classe 'Tabuleiro'.
    '''
    def __init__(self):
        '''(MacroTabuleiro) --> None
        Método construtor da classe MacroTabuleiro. Herda métodos da classe Tabuleiro.
        '''
        # Para herdar
        Tabuleiro.__init__(self)
        self.ehMacro = True
    
    def marcaVitoria(self, qualMicroTabuleiro, jogador):
        '''(MacroTabuleiro, tuple) --> None
        Esse método marco no macro-tabuleiro quando algum micro-tabuleiro foi vencido
        '''
        linha, coluna = qualMicroTabuleiro
        self.configuracaoDoTabuleiro[linha][coluna] = jogador.simboloDoJogador
        
        

class Jogador:
    '''
    Representação mais básica de um tipo de jogador
    '''
    def __init__(self, simboloDoJogador):
        '''(Jogador, int) --> None
        Método construtor da classe Jogador.
        '''
        self.simboloDoJogador = simboloDoJogador            
        self.vezDeJogar = False
        self.microTabuleirosDisponiveis = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
        
    def quaisTabuleirosDisponiveis(self):
        '''(Jogador) --> list
        Esse método retorna a lista dos tabuleiros que ainda estão disponíveis.
        '''
        return self.tabuleirosDisponiveis
    
    def fazJogada(self, Usuario, microTabuleiro, qualPosicao, qualMicroTabuleiro):
        '''(Jogador, Usuario, MicroTabuleiro, tuple, tuple) --> None
        Realiza uma jogada de um Jogador em um micro-tabuleiro.
        '''
        # Lugar onde será feita a jogada
        linha, coluna = qualPosicao
        # Qual símbolo será marcado
        simboloDoJogador = self.simboloDoJogador
        if microTabuleiro.verificaPosicaoVazia(linha, coluna):
            # Faz a jogada
            microTabuleiro.configuracaoDoTabuleiro[linha][coluna] = simboloDoJogador
            # Tira a posição qualPosicao da lista de posições vazias
            indiceDaPosicao = microTabuleiro.posicoesVazias.index((qualPosicao))
            del microTabuleiro.posicoesVazias[indiceDaPosicao]
        else:
            print("\nJogada inválida!")
            Usuario.jogadaDaVez(jogador_um, jogador_dois, macroTabuleiro)
            return
        # Se o jogador não for do tipo Humano, imprimir na saída de dados a jogada que foi feita
        if self.tipoDeJogador == "humano":
            print("\nJogada realizada!\n")
        else:
            print(f'\nO computador fez a seguinte jogada: Micro-tabuleiro[{qualMicroTabuleiro[0]}][{qualMicroTabuleiro[1]}]; posição: {qualPosicao}\n')
        return
        
    
class JogadorHumano(Jogador):
    '''
    Classe que repesenta um jogador do tipo "humano".
    Esse tipo de jogador é controlado por um humano e digita as jogados no teclado do computador.
    '''
    def __init__(self, simboloDoJogador):
        '''(JogadorHumano) --> None
        Método construtor da classe JogadorHumano
        '''
        Jogador.__init__(self, simboloDoJogador)
        self.tipoDeJogador = "humano"
        
        
    def escolheMicroTabuleiro(self):
        '''(JogadorHumano) --> tuple
        Esse método determina em qual micro-tabuleiro o usuário quer fazer a jogada.
        RETORNA a tupla qualMicroTabuleiro, que indica em qual micro-tabuleiro a jogada será feita
        '''
        escolheu_linha = False
        escolheu_coluna = False
        # Lista que armazenas as escolhas válidas e possíveis
        possiveis_escolhas = ["0","1","2"]
        # Determina em qual micro-tabuleiro a jogada será feita
        while not escolheu_linha:
            qualLinhaDoMacro = input("Digite qual linha do macro-tabuleiro você quer jogar: ")           
            if qualLinhaDoMacro not in possiveis_escolhas:
                print("Valor inválido!")
            else:
                qualLinhaDoMacro = int(qualLinhaDoMacro)
                escolheu_linha = True
        while not escolheu_coluna:
            qualColunaDoMacro = input("Digite qual coluna do macro-tabuleiro você quer jogar: ")
            if qualColunaDoMacro not in possiveis_escolhas:
                print("Valor inválido!")
            else:
                qualColunaDoMacro = int(qualColunaDoMacro)
                escolheu_coluna = True
        qualMicroTabuleiro = qualLinhaDoMacro, qualColunaDoMacro
        if qualMicroTabuleiro not in self.microTabuleirosDisponiveis:
            print(f'O MicroTabuleiro[{qualLinhaDoMacro}][{qualColunaDoMacro}] está inativo porque algum jogador já ganhou nele.')
            self.escolheMicroTabuleiro()
        return qualMicroTabuleiro
    
    
    def escolhePosicaoNoMicro(self):
        '''(JogadorHumano) --> tuple
        RETORNA a tupla qualPosicao que indica onde a jogada será feito no micro-tabuleiro.
        '''
        escolheu_linha = False
        escolheu_coluna = False
        # Lista que armazenas as escolhas válidas e possíveis
        possiveis_escolhas = ["0","1","2"]
        # Determina em qual posição do micro-tabuleiro a jogada será feita
        while not escolheu_linha:
            qualLinha = input("Digite qual linha do micro-tabuleiro você quer jogar: ")
            if qualLinha not in possiveis_escolhas:
                print("Valor inválido!")
            else:
                qualLinha = int(qualLinha)
                escolheu_linha = True
        while not escolheu_coluna:
            qualColuna = input("Digite qual coluna do micro-tabuleiro você quer jogar: ")
            if qualColuna not in possiveis_escolhas:
                print("Valor inválido!")
            else:
                qualColuna = int(qualColuna)
                escolheu_coluna = True
        qualPosicao = qualLinha, qualColuna
        return qualPosicao

    
    def verificaJogada(self, microTabuleiro, qualPosicao):
        '''(JogadorHumano, MicroTabuleiro, tuple) --> bool
        Verifica se a posição [qualLinha, qualColuna] do MicroTabuleiro está vazia
        RETORNA True se a posição estiver vazia e False caso contrário.
        '''
        linha, coluna = qualPosicao
        return microTabuleiro.verificaPosicaoVazia(linha, coluna)
        
        
class JogadorEstabanado(Jogador):
    '''
    Classe que representa um jogador do tipo "estabanado".
    Esse tipo de jogador é controlado pelo computador e sempre joga numa posição aleatória do tabuleiro.
    '''
    def __init__(self, simboloDoJogador):
        '''(JogadorEstabanado) --> None
        Método construtor da classe JogadorEstabando
        '''
        Jogador.__init__(self, simboloDoJogador)
        self.tipoDeJogador = "estabanado"
    
    
    def escolheMicroTabuleiro(self):
        '''(JogadorEstabanado) --> tuple
        Esse método retorna aleatoriamente um dos micro-tabuleiros disponíveis.
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
        qualPosicao = random.choice(microTabuleiro.posicoesVazias)
        indiceDaJogada = microTabuleiro.posicoesVazias.index(qualPosicao)
        return qualPosicao
    
    
class JogadorComeCru(Jogador):
    '''
    Classe que representa um jogador do tipo "come-crú".
    Esse tipo de jogador é controlado pelo computador e sempre joga na primeira posição livre do tabuleiro.
    '''
    def __init__(self, simboloDoJogador):
        '''(JogadorComeCru) --> None
        Método construtor da classe JogadorComeCru
        '''
        Jogador.__init__(self, simboloDoJogador)
        self.tipoDeJogador = "comecru"
    
    
    def escolheMicroTabuleiro(self):
        '''(JogadorComeCru) --> tuple
        Esse método retorna o primeiro micro-tabuleiro disponível.
        '''
        # Define em qual micro-tabuleiro a jogada será feita
        qualMicroTabuleiro = self.microTabuleirosDisponiveis[0]
        return qualMicroTabuleiro
        
        
    def escolhePosicaoNoMicro(self, microTabuleiro):
        '''(JogadorComeCru, microTabuleiro) --> tuple
        Esse método retorna o primeiro espaço vazio de um objeto do tipo MicroTabuleiro.
        '''
        # Define a posição no micro-tabuleiro onde a jogada será feita
        qualPosicao = microTabuleiro.posicoesVazias[0]
        indiceDaJogada = microTabuleiro.posicoesVazias.index(qualPosicao)
        return qualPosicao
       
def transformaEmClone(jogador_um, jogador_dois):
    '''(Jogador, Jogador) --> None
    Essa função pega o atributo 'microTabuleirosDisponiveis' de dois objetos do tipo 'Jogador'
    e transforma um em um clone do outro
    '''
    jogador_um.microTabuleirosDisponiveis = jogador_dois.microTabuleirosDisponiveis
    
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
    tipo_jogador_um, tipo_jogador_dois = usuario.escolhe_jogadores() 
    # Cria os dois jogadores
    jogador_um, jogador_dois = usuario.cria_jogador(tipo_jogador_um, "X"), usuario.cria_jogador(tipo_jogador_dois, "O")
    # transforma o atributo 'tabuleirosDisponiveis' dos jogadores em clones um do outro
    transformaEmClone(jogador_um, jogador_dois)
    # Determina que o jogador_um vai começar jogando
    jogador_um.vezDeJogar = True
    # Aqui são criados o macro-tabuleiro e os 9 micro-tabuleiros
    macro_tabuleiro = MacroTabuleiro()
        # Micro-tabuleiros. Os números contidos no nome representam a posição (no formato (x, y)) no macro-tabuleiro
    micro00, micro01, micro02 = MicroTabuleiro(0,0), MicroTabuleiro(0,1), MicroTabuleiro(0,2)
    micro10, micro11, micro12 = MicroTabuleiro(1,0), MicroTabuleiro(1,1), MicroTabuleiro(1,2)
    micro20, micro21, micro22 = MicroTabuleiro(2,0), MicroTabuleiro(2,1), MicroTabuleiro(2,2)
    # Lista com todos os objetos do tipo MicroTabuleiro
    listaDeMicroTabuleiros = [[micro00, micro01, micro02], 
                              [micro10, micro11, micro12], 
                              [micro20, micro21, micro22]]
    # Cria array com a lista dos micro-tabuleiros
    usuario.criaArrayDeTabuleiros(listaDeMicroTabuleiros)
    
    # Enquanto ninguém vencer o macro-tabuleiro ou não tiver mais jogadas possíveis, não sai do loop
    while not macro_tabuleiro.tabuleiroAcabou and len(macro_tabuleiro.posicoesVazias) > 0:
        usuario.menuDeOpcoes(macro_tabuleiro, jogador_um)
        usuario.jogadaDaVez(jogador_um, jogador_dois, macro_tabuleiro)
        #verificaMacroTabuleiro()

# Para chamar a função main automaticamente
if __name__ == '__main__':
    main()

