# -*- coding: utf-8 -*-
import pytest
from EP4 import *


@pytest.fixture
def microTabuleiroVazio():
    return MicroTabuleiro(0,0)

@pytest.fixture
def macroTabuleiro():
    return MacroTabuleiro()

@pytest.fixture
def macroTabuleiroAcabado(macroTabuleiro):
    macro = macroTabuleiro
    macro.configuracaoDoTabuleiro[0][0] = "X"
    macro.configuracaoDoTabuleiro[0][1] = "X"
    macro.configuracaoDoTabuleiro[0][2] = "X"
    return macro
    
@pytest.fixture
def tabuleiroComDiagonalPrincipalPreenchida(microTabuleiroVazio):
    tabuleiro = microTabuleiroVazio
    tabuleiro.configuracaoDoTabuleiro[0][0] = "X"
    tabuleiro.configuracaoDoTabuleiro[1][1] = "X"
    tabuleiro.configuracaoDoTabuleiro[2][2] = "X"
    return tabuleiro

@pytest.fixture
def tabuleiroComDiagonalSecundariaPreenchida(microTabuleiroVazio):
    tabuleiro = microTabuleiroVazio
    tabuleiro.configuracaoDoTabuleiro[0][2] = "X"
    tabuleiro.configuracaoDoTabuleiro[1][1] = "X"
    tabuleiro.configuracaoDoTabuleiro[2][0] = "X"
    return tabuleiro

@pytest.fixture
def tabuleiroAleatorio(microTabuleiroVazio):
    tabuleiro = microTabuleiroVazio
    tabuleiro.configuracaoDoTabuleiro[0][1] = "O"
    tabuleiro.configuracaoDoTabuleiro[2][0] = "O"
    tabuleiro.configuracaoDoTabuleiro[2][2] = "O"
    return tabuleiro

@pytest.fixture
def usuario():
    return Usuario()

@pytest.fixture
def jogador1():
    return Jogador("X")

@pytest.fixture
def jogador2():
    return Jogador("O")

@pytest.fixture
def jogadorHumano():
    return JogadorHumano("X")

@pytest.fixture
def jogadorEstabanado():
    return JogadorEstabanado("X")

@pytest.fixture
def jogadorComeCru():
    return JogadorComeCru("X")


class TestaMicroTabuleiro: 
    # Testa se cada posição do tabuleiro foi iniciada vazia
    def test_tabuleiro_vazio_pos00(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(0,0)
    def test_tabuleiro_vazio_pos01(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(0,1)
    def test_tabuleiro_vazio_pos02(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(0,2)
    def test_tabuleiro_vazio_pos10(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(1,0)
    def test_tabuleiro_vazio_pos11(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(1,1)
    def test_tabuleiro_vazio_pos12(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(1,2)
    def test_tabuleiro_vazio_pos20(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(2,0)
    def test_tabuleiro_vazio_pos21(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(2,1)
    def test_tabuleiro_vazio_pos22(self, microTabuleiroVazio):
        assert microTabuleiroVazio.verificaPosicaoVazia(2,2)
        
    def testa_diagonal_principal(self, tabuleiroComDiagonalPrincipalPreenchida):
        assert tabuleiroComDiagonalPrincipalPreenchida.verificaDiagonalPrincipal("X") == True
        
    def testa_diagonal_principal_dando_false(self, tabuleiroAleatorio, jogador2):
        simbolo = jogador2.simboloDoJogador
        assert tabuleiroAleatorio.verificaDiagonalPrincipal(simbolo) == False
        
    def testa_diagonal_secundaria(self, tabuleiroComDiagonalSecundariaPreenchida):
        assert tabuleiroComDiagonalSecundariaPreenchida.verificaDiagonalSecundaria("X") == True
        
    def testa_se_ganhou_micro_tabuleiro(self, tabuleiroAleatorio, jogador2):
        tabuleiro = tabuleiroAleatorio
        assert tabuleiro.verificaSeGanhouTabuleiro((0,1), jogador2) == False

    

class TestaMacroTabuleiro:
    def testa_se_criou_macro_tabuleiro(self, macroTabuleiro):
        macro = macroTabuleiro
        assert macro.ehMacro == True
        
    def testa_se_macro_tabuleiro_acabou(self, macroTabuleiro, usuario, jogador1):
        macro = macroTabuleiro
        usuario.venceuJogo(jogador1, macroTabuleiro)
        assert macroTabuleiro.tabuleiroAcabou
        
    def testa_se_macro_tabuleiro_acabou_v2(self, macroTabuleiroAcabado, jogador1):
        macro = macroTabuleiroAcabado
        macro.verificaSeGanhouTabuleiro((0,1), jogador1)
        assert macro.tabuleiroAcabou == True
        
    def testa_se_marcou_vitoria_de_micro(self, macroTabuleiro, jogador1):
        macro = macroTabuleiro
        macro.marcaVitoria((0,0), jogador1)
        assert macro.configuracaoDoTabuleiro[0][0] == "X"


def testaCriacaoDoArrayDeTabuleiros(usuario, microTabuleiroVazio):
    # Aqui estamos simulando com 9 tabuleiros iguais mas no jogo são 9 diferentes
    listaDeMicroTabuleiros = [[microTabuleiroVazio, microTabuleiroVazio, microTabuleiroVazio], 
                              [microTabuleiroVazio, microTabuleiroVazio, microTabuleiroVazio], 
                              [microTabuleiroVazio, microTabuleiroVazio, microTabuleiroVazio]]
    usuario.criaArrayDeTabuleiros(listaDeMicroTabuleiros)
    assert len(usuario.arrayDeTabuleiros) == 3
    
def testaCriacaoDeJogadorHumano(jogadorHumano):
    assert jogadorHumano.tipoDeJogador == "humano"

class TestaCriacaoDeJogadores:
    def testaCriacaoDeJogadorHumano(self,usuario):
        jogador = usuario.cria_jogador(1, "X")
        assert jogador.tipoDeJogador == 'humano'
        
    def testaCriacaoDeJogadorEstabanado(self,usuario):
        jogador = usuario.cria_jogador(2,"X")
        assert jogador.tipoDeJogador == 'estabanado'
    
    def testaCriacaoDeJogadorComeCru(self,usuario):
        jogador = usuario.cria_jogador(3,"X")
        assert jogador.tipoDeJogador == 'comecru'
    
def testa_fazJogada(usuario, microTabuleiroVazio, jogador1):
    jogador1.fazJogada(usuario, microTabuleiroVazio, (0,0), (0,0))
    assert microTabuleiroVazio.configuracaoDoTabuleiro[0][0] == "X"
        
    
        