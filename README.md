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
&nbsp;&nbsp;O trabalho consiste em uma implementação orientada a objetos em Python do **Ultimate Tic-Tac-Toe** (https://en.wikipedia.org/wiki/Tic-tac-toe_variants).  A ideia é que um macro-tabuleiro é composto por 9 micro-tabuleiros de jogo da velha dispostos no formato de um grande jogo da velha (3x3). Os jogadores podem escolher jogar em qualquer lugar do macro-tabuleiro, uma jogada por vez, de forma alternada e desde que a jogada for válida (ou seja, se o lugar estiver 'vazio'). Quando um jogador ganha um dos micro-tabuleiros, este é marcado inteiro como pertencente ao jogador que o venceu. Ganha o jogo quem ganhar o jogo da velha no macro-tabuleiro.<br></br>

#### Foram implementados os seguintes jogadores:
1) Jogador humano: digita as jogadas no teclado do computador;
2) Jogador estabanado: sempre joga numa posição aleatória do tabuleiro;
3) Jogador come-crú: sempre escolhe a primeira posição livre do tabuleiro;<br></br>

&nbsp;&nbsp;Para saber em qual tabuleiro você está jogando, é válido pensar como se o tabuleiro fosse uma matriz, então o tabuleiro do canto superior esquerdo é o tabuleiro de posição [0][0], o que está à direita deste é [0][1] e assim por diante.<br></br>
&nbsp;&nbsp;A cada rodada será disposto um menu com as opções possíveis, sendo elas:
1) Imprimir algum micro-tabuleiro (O jogador deverá digitar '1')
2) Imprimir o macro-tabuleiro (O jogador deverá digitar '2')
3) Fazer jogada (O jogador deverá apertar a tecla 'Enter')<br></br>

Se o jogador humano escolher a opção 1, ele deverá, em seguida, digitar a tupla que representa a posição do micro-tabuleiro que ele quer ver (por exemplo '0, 2'); se escolher a opção 2, o macro-tabuleiro será impresso na saída de dados, e se ele apertar a tecla 'Enter', fará a sua jogada digitando uma tupla representando a posição do micro-tabuleiro no macro-tabuleiro e em seguida outra tupla representando a posição onde ele quer fazer a jogada dele no micro-tabuleiro.<br></br>
&nbsp;&nbsp;Em caso de empate em algum dos micro-tabuleiros, esse micro-tabuleiro é reiniciado, ou seja, ele volta a ser totalmente vazio. No caso de empate no macro-tabuleiro, o jogo simplesmente termina com empate.<br></br>
&nbsp;&nbsp;O jogo só acaba se acontecer um dos seguintes eventos:
- Um dos jogadores conseguiu completar uma coluna ou uma linha ou uma diagonal do macro-tabuleiro;
- Não há mais espaços livres no macro-tabuleiro e nenhum dos jogadores venceu (popularmente falando, 'deu zebra').

## Como rodar o programa:
&nbsp;&nbsp;Quando o jogo se inicia, o programa pergunta qual será o tipo do 1º jogador e qual será o tipo do 2º jogador. Por exemplo, deve ser possível ter um jogo entre 2 humanos ou entre dois jogadores automatizados ou qualquer outra combinação possível.<br></br>
&nbsp;&nbsp;No caso do jogador humano, ele deverá apertar a tecla enter para fazer sua jogada ou então escolher uma das opções que são disponibilzadas no começo de cada rodada, como já dito anteriormente. O jogador só passa a vez quando fizer uma jogada válida.




