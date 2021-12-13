# Mega-tic-tac-toe
Este projeto foi requerido pelo professor Fabio Kon na disciplina 'MAC0216 - Técnicas de Programação I' na Universidade de São Paulo (USP). 
O objetivo é fazer um 'Mega Jogo-da-velha' usando programação orientada a objetos (POO).

> Status: Em desenvolvimento

## Desenvolvedores:
- Nome: Alxélio Ribeiro Esteves - NUSP: 11796980

- Nome: Augusto Lima Jardim - NUSP: 11810918

- Nome: Gilvane da Silva Souza - NUSP: 10258726
## Tecnologias utilizadas:
 Tecnologia   | Versão
:----------:  | :--------:
Python        | 3.*
pytest        | 6.2.5
git           | 2.23.0


## Descrição:
&nbsp;&nbsp;O trabalho consiste em uma implementação orientada a objetos em Python do **Ultimate Tic-Tac-Toe** (https://en.wikipedia.org/wiki/Tic-tac-toe_variants).  A ideia é que um macro-tabuleiro é composto por 9 micro-tabuleiros de jogo da velha dispostos no formato de um grande jogo da velha (3x3). Os jogadores podem escolher jogar em qualquer lugar do macro-tabuleiro, uma jogada por vez, de forma alternada. Quando um jogador ganha um dos micro-tabuleiros, aquele micro-tabuleiro é marcado inteiro como pertencente ao jogador que o venceu. Ganha o jogo quem ganhar o jogo da velha no macro-tabuleiro.<br></br>
&nbsp;&nbsp;Foram implementados os seguintes jogadores:
1) Jogador humano: digita as jogadas no teclado do computador;
2) Jogador estabanado: sempre joga numa posição aleatória do tabuleiro;
3) Jogador come-crú: sempre escolhe a primeira posição livre do tabuleiro;

## Funcionamento e como rodar o programa:
&nbsp;&nbsp;Quando o jogo se inicia, o programa pergunta qual será o tipo do 1º jogador e qual será o tipo do 2º jogador. Por exemplo, deve ser possível ter um jogo entre 2 humanos ou entre dois jogadores automatizados ou qualquer outra combinação possível.
&nbsp;&nbsp;No jogo há um macro-tabuleiro de jogo-da-velha e cada 'espaço' nesse tabuleiro é um micro-tabuleiro de jogo-da-velha. Para saber em qual tabuleiro você está jogando, é válido pensar como se o tabuleiro fosse uma matriz, então o tabuleiro do canto superior esquerdo é o tabuleiro de posição [0][0], o da direita é [0][1] e assim por diante.



