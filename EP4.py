# -*- coding: utf-8 -*-
class microTabuleiro():
    """
    Esta classe representa um micro tabuleiro do Mega-jogo-da-velha.
    """
    '''
    #Armazena a quantidade de linhas.
    __linhas = 3
    #Método getter do atributo "linhas".
    @property
    def linhasDoTabuleiro (self):
        return self.__linhas
    
    #Métoodo setter do atributo "linhas".
    @linhasDoTabuleiro.setter
    def linhasDoTabuleiro (self, novaQuantidadeDeLinhas):
        self.__linhas = novaQuantidadeDeLinhas     
        
    #Armazena a quantidade de colunas.
    __colunas = 3
    #Método getter do atributo "colunas".
    @property
    def colunasDoTabuleiro (self):
        return self.__colunas
    #Métoodo setter do atributo "colunas".
    @colunasDoTabuleiro.setter
    def colunasDoTabuleiro (self, novaQuantidadeDeColunas):
        self.__colunas = novaQuantidadeDeColunas
    '''
    
    def __init__(self, pos_linha, pos_coluna):
        ''' (int, int) -> None
        Método construtor da classe microTabuleiro.
        RECEBE os inteiros pos_linha e pos_coluna que representam a posição [pos_linha][pos_coluna]
        do micro-tabuleiro no macro-tabuleiro       
        '''
        self.pos_lin = pos_linha
        self.pos_col = pos_coluna
    
    #Armazena o caractere que representa o vencedor de uma instância desta classe.
    __vencedor = ""
    #Método getter do atributo "vencedor".
    @property
    def vencedorDoJogo (self):
        return self.__vencedor
    
    #Métoodo setter do atributo "vencedor".
    @vencedorDoJogo.setter
    def vencedorDoJogo (self, novoVencedor):
        self.__vencedor = novoVencedor
        
    #Armazena a configuração do jogo.
    __configuracaoDoTabuleiro = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]
        
    #Método getter do atributo "configuracao".
    @property
    def configuracaoDoTabuleiro (self):
        return self.__configuracaoDoTabuleiro
    
    #Métoodo setter do atributo "configuracao".
    @configuracaoDoTabuleiro.setter
    def configruacaoDoTabuleiro (self, novaConfiguracao):
        self.__configuracaoDoTabuleiro.copy(novaConfiguracao) 

    #Este método imprime a configuraçao atual do jogo da velha 3x3.
    def imprimirConfiguracaoDoJogo (self):
        #Imprime a primeira linha do tabuleiro.
        print("\t {} | {} | {} ".format(self.__configuracaoDoTabuleiro[0][0], self.__configuracaoDoTabuleiro[0][1], self.__configuracaoDoTabuleiro[0][2]))
        print('\t---+---+---')
        #Imprime a segunda linha do tabuleiro.
        print("\t {} | {} | {} ".format(self.__configuracaoDoTabuleiro[1][0], self.__configuracaoDoTabuleiro[1][1], self.__configuracaoDoTabuleiro[1][2]))
        print('\t---+---+---')
        #Imprime a terceira linha do tabuleiro.
        print("\t {} | {} | {} \n".format(self.__configuracaoDoTabuleiro[2][0], self.__configuracaoDoTabuleiro[2][1], self.__configuracaoDoTabuleiro[2][2]))
        print(f"   Tabuleiro[{self.pos_lin}][{self.pos_col}]")
    
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
    
class Jogador:
    '''
    Representação mais básica de um tipo de jogador
    '''
    def __init__(self, numeroDoJogador):
        if numeroDoJogador == 1:
            self.simboloDoJogador = "X"
            self.vezDeJogar = True
        else:
            self.simboloDoJogador = "O"
            self.vezDeJogar = False
            
        
class JogadorHumano(Jogador):
    '''
    Classe que repesenta um jogador do tipo "humano".
    Esse tipo de jogador é controlado por um humano e digita as jogados no teclado do computador.
    '''
    def faz_jogada():
        qualMicroTabuleiro = input("Em qual tabuleiro você quer jogar?")
        qualLinha, qualColuna = int(input("Qual é a sua jogada?")
        
        
    

#class JogadorEstabanado(Jogador):
 #   '''
  #  Classe que representa um jogador do tipo "estabanado".
   # Esse tipo de jogador é controlado pelo computador e sempre joga numa posição aleatória do tabuleiro.
    #'''
    #def faz_jogada():
     #   pass
    
    
    
    
#class JogadorComeCru(Jogador):
 #   '''Classe que representa um jogador do tipo "come-crú".
  #  Esse tipo de jogador é controlado pelo computador e sempre joga na primeira posição livre do tabuleiro.
   # '''
       



def explica_jogadores():
    '''(None) --> None
    Essa função serve exclusivamente para descrever o comportamento de cada jogador
    '''
    print("\nJogador humano: digita as jogadas no teclado do computador.")
    print("Jogador estabanado: sempre joga numa posição aleatória do tabuleiro.")
    print("Jogador come-crú: sempre escolhe a primeira posição livre do tabuleiro.")
    return

## fazer a função 'imprima(x, y)' para imprimir o tabuleiro de posição x,y 
## fazer a função 'imprimaMacro() para imprimir o macro tabuleiro

## ========================================================================================================== ##

def main():
    print("Bem-vindo(a) ao Mega Jogo da Velha!\n")
    print("Abaixo estão listados os tipos de jogadores:")
    print("1. Jogador humano\n2. Jogador estabanado\n3. Jogador come-crú")
    
    escolheu_jogadores = False
    
    # enquanto o usuário não escolher os jogadores, não sai do loop
    while not escolheu_jogadores:
        comando = int(input("Se você quiser escolher os jogadores, digite '0'. Se quiser ler a descrição dos jogadores, digite '1': "))
        #escolhe os jogadores
        if comando == 0: 
            jogador_um = input("Escolha o tipo do Jogador 1 (X): ")
            jogador_dois = input("Escolha o tipo do Jogador 2 (O): ")
            escolheu_jogadores = True
        # chama a função que explica cada jogador
        elif comando == 1:
            explica_jogadores()
        else:
            print("\nComando inválido!")
            
    # Aqui são criados o macro-tabuleiro e os 9 micro-tabuleiros
    



# Para chamar a função main automaticamente
if __name__ == '__main__':
    main()