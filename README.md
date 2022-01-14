## OBI (Olimpíadas Brasileiras de Informática) 🚀

Abaixo está realizado os algoritmos em Python que eu mesmo elaborei durante a primeira fase da olímpiada. ✅
<hr></hr>


### Xadrez: ♟
```
 No tabuleiro de xadrez, a casa na linha 1, coluna 1 (canto superior esquerdo) é sempre branca e as cores das casas se alternam entre branca e preta, de acordo com o padrão conhecido como... xadrez! Dessa forma, como o tabuleiro tradicional tem oito linhas e oito colunas, a casa na linha 8, coluna 8 (canto inferior direito) será também branca. Neste problema, entretanto, queremos saber a cor da casa no canto inferior direito de um tabuleiro com dimensões quaisquer: L linhas e C colunas. No exemplo da figura, para L=6 e C=9, a casa no canto inferior direito será preta!

Entrada
A primeira linha da entrada contém um inteiro L indicando o número de linhas do tabuleiro. A segunda linha da entrada contém um inteiro C representando o número de colunas.

Saída
Imprima uma linha na saída. A linha deve conter um inteiro, representando a cor da casa no canto inferior direito do tabuleiro: 1, se for branca; e 0, se for preta.

Restrições
1 ≤ L ≤ 1000
1 ≤ C ≤ 1000

```

### Escadinha: ⏬

```
Dizemos que uma sequência de números é uma escadinha, se a diferença entre números consecutivos é sempre a mesma. Por exemplo, "2, 3, 4, 5" e "10, 7, 4" são escadinhas. Note que qualquer sequência com apenas um ou dois números também é uma escadinha!

Neste problema estamos procurando escadinhas em uma sequência maior de números. Dada uma sequência de números, queremos determinar quantas escadinhas existem. Mas só estamos interessados em escadinhas tão longas quanto possível. Por isso, se uma escadinha é um pedaço de outra, consideramos somente a maior. Por exemplo, na sequência "1, 1, 1, 3, 5, 4, 8, 12" temos 4 escadinhas diferentes: "1, 1, 1", "1, 3, 5", "5, 4" e "4, 8, 12".

Entrada
A primeira linha da entra contém um inteiro N indicando o tamanho da sequência de números. A segunda linha contém N inteiros definindo a sequência.

Saída
Imprima uma linha contendo um inteiro representando quantas escadinhas existem na sequência

Restrições
1 ≤ N ≤ 1000
O valor dos números da sequência está entre -106 e 106 inclusive.
```

### Pirâmide: △

```
No depósito da fábrica, encostada numa parede, existe uma matriz de N linhas por N colunas de caixas empilhadas. Cada caixa possui um peso inteiro positivo associado. O inspetor da fábrica precisa retirar algumas caixas da matriz de modo a deixar uma espécie de pirâmide de caixas satisfazendo as seguintes restrições:

Se uma caixa está na pirâmide, a caixa imediatamente abaixo dela também deve estar na pirâmide;
Na i-ésima linha de caixas (a linha 1 é a do topo da matriz), a pirâmide deve ter exatamente i caixas consecutivas.
Dados os pesos de todas as caixas na matriz, seu programa deve calcular o peso total mínimo que uma pirâmide poderá ter, se o inspetor retirar algumas caixas segundo as restrições acima.

Entrada
A primeira linha da entrada contém um inteiro N, indicando a dimensão da matriz. As N linhas seguintes contêm, cada uma, N inteiros representando os pesos das caixas em cada linha da matriz de caixas.

Saída
Seu programa deve produzir uma única linha, contendo um inteiro, indicando o peso total mínimo que a pirâmide poderá ter.

Restrições
1 ≤ N ≤ 100
Os valor dos elementos da matriz está entre 1 e 100, inclusive.

Informações sobre a pontuação
Para um conjunto de casos de testes valendo 20 pontos, N ≤ 20.
```
