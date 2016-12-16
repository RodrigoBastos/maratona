# Concurso de Contos
Fonte: Maratona de Programação da SBC 2012

## Descrição

Machado gosta muito de escrever. Já escreveu muitos contos, resenhas, relatos de viagens que fez,
além de um pequeno romance. Agora Machado quer participar de um concurso de contos, que tem
regras muito rígidas sobre o formato de submissão do conto.

As regras do concurso especificam o número máximo de caracteres por linha, o número máximo de
linhas por página, além de limitar o número total de páginas. Adicionalmente, cada palavra deve ser
escrita integralmente em uma linha (ou seja, a palavra não pode ser separada silabicamente em duas
linhas). Machado quer escrever um conto com o maior número de palavras possível, dentro das regras
do concurso, e precisa de sua ajuda.

Dados o número máximo de caracteres por linha, o número máximo de linhas por página, e as
palavras do conto que Machado está escrevendo, ele quer saber o número mínimo de páginas que seu
conto utilizaria seguindo as regras do concurso.


## Entrada

 - A primeira linha de um caso de teste contém três inteiros N, L e C, que indicam, respectivamente,
o número de palavras do conto de Machado, o número máximo de linhas por página e o número máximo
de caracteres por linha.
 - O conto de Machado é inovador e não contém nenhum caractere além de letras maiúsculas e minúsculas e
 espaços em branco, sem letras acentuadas e sem cedilha.
 - A segunda linha contém o conto de Machado, composto de N palavras separadas por espaços em branco;
 há espaço em branco somente entre duas palavras, e entre duas palavras há exatamente um espaço em branco.


## Saída

 - Para cada caso de teste imprima uma única linha, contendo um único número inteiro, indicando o
   número mínimo de páginas que o conto de Machado ocupa, considerando as regras do concurso.

## Restrições

 - 2 ≤ N ≤ 1000
 - 1 ≤ L ≤ 30
 - 1 ≤ C ≤ 70
 - 1 ≤ comprimento de cada palavra ≤ C

## Exemplos


| Primeira Linha | Segunda Linha                                                                         | Saída |
|----------------|---------------------------------------------------------------------------------------|-------|
| 14 4 20        | Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral  | 2     |
| 16 3 30        | No dia seguinte entrou a dizer de mim nomes feios e acabou alcunhando me Dom Casmurro | 1     |
| 5 2 2          | a de i de o                                                                           | 3     |
| 5 2 2          | a e i o u                                                                             | 3     |



