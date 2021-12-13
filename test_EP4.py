# -*- coding: utf-8 -*-
import pytest
from EP4 import *


@pytest.fixture
def tabuleiroVazio():
    t = microTabuleiro(0,0)
    return t

class TestaMicroTabuleiro: 
    # Testa se cada posição do tabuleiro foi iniciada vazia
    def test_tabuleiro_vazio_pos00(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[0][0] == " "
    def test_tabuleiro_vazio_pos01(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[0][1] == " "
    def test_tabuleiro_vazio_pos02(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[0][2] == " "
    def test_tabuleiro_vazio_pos10(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[1][0] == " "
    def test_tabuleiro_vazio_pos11(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[1][1] == " "
    def test_tabuleiro_vazio_pos12(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[1][2] == " "
    def test_tabuleiro_vazio_pos20(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[2][0] == " "
    def test_tabuleiro_vazio_pos21(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[2][1] == " "
    def test_tabuleiro_vazio_pos22(self, tabuleiroVazio):
        assert tabuleiroVazio.configuracaoDoTabuleiro[2][2] == " "
    
        